from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from .models import Post
from accounts.models import Profile
from comments.models import Comment
from comments.forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


class PostListView(ListView):
    model = Post
    template_name = 'posts/index.html'
    context_object_name = 'posts'
    ordering = ['-pub_date']
    paginate_by = 9

class UserListView(ListView):
    model = Post
    template_name = 'posts/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 9

    def get_object(self):
        username = self.kwargs.get('username')
        user = get_object_or_404(User, username=username) 
        return user

    # overriding the get_queryset method you can filter 
    # only the posts linked with the user in the url
    # you have to import User from django.contrib
    # get 404 if hard type on browser something unexistent
    def get_queryset(self):
        user = get_object_or_404(User, username=self.get_object()) 
    #     # the second parameter is so we can get the user from the url
        return Post.objects.filter(user=user).order_by('-pub_date')

    # get context data to be able to use profile instance variables  
    # you gotta update the context so it doesnt override all the context, 
    # just adds it
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        user = self.get_object()
        profile = get_object_or_404(Profile, user=user) 
        context.update({ 'profile': profile })
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/detail.html'
    ordering = ['-pub_date']

    # get the comment form to work on the Post detail
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            data['comment_form'] = CommentForm(instance=self.request.user)
        return data
    
    def post(self, request, *args, **kwargs):
        post = self.get_object()
        new_comment = Comment(body=request.POST.get('body'), 
                            user=self.request.user,
                            post=post)
        new_comment.save()
        # avoid resubmit of data when refresh page with:
        return HttpResponseRedirect(str(post.id))
                   

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'posts/post_form.html'
    fields = ['title', 'image', 'sub_title', 'body']


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'image', 'sub_title', 'body']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    # to make sure the user is the author of the post and
    # the only one able to update their post
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.user


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/' # add this so you can be redirected home after the deletion

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.user
        
    # to confirm the deletion of a post, create posts/poat_confirm_delete.html
