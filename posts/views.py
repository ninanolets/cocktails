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
from django.http import HttpResponseRedirect, HttpResponse
import json
from django.template.loader import render_to_string
from django.contrib import messages
from comments.views import CommentFormView
from django.views import View
from post_likes.views import PostLike
from comment_likes.views import CommentLike



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
        context['profile'] = profile
        return context


    

class PostDisplay(DetailView):
    model = Post
    template_name = 'posts/detail.html'

    # get the comment form to work on the Post detail
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            user = self.request.user
            post = self.get_object()
            
            context['comment_form'] = CommentForm(instance=user)
            context['has_liked_post'] = PostLike.objects.filter(post_id=post.id, user_id=user.id).exists()
            context['has_liked_comment'] = CommentLike.objects.filter(user_id=user.id)
        
        return context
        
        

class PostDetailView(View):

    def get(self, request, *args, **kwargs):
        view = PostDisplay.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = CommentFormView.as_view()
        return view(request, *args, **kwargs)

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'posts/post_form.html'
    fields = ['title', 'sub_title', 'image', 'body']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

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
