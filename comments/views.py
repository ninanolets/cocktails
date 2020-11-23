from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden
from django.urls import reverse
from django.views.generic import FormView
from django.views.generic.detail import SingleObjectMixin
from posts.models import Post
from comments.forms import CommentForm
from comments.models import Comment
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseForbidden
import json
from django.template.loader import render_to_string
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required


# Handle for here

class CommentFormView(SingleObjectMixin, FormView):
    template_name = 'posts/detail.html'
    form_class = CommentForm
    model = Post

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        # self.object = self.get_object()

        body = request.POST.get('comment')
        post = self.get_object()
        user = self.request.user
        
        new_comment = Comment(body=body, post=post, user=user)
        new_comment.save()

        context = { 
            'comment': new_comment,
            'user': user 
        }
        
        template = render_to_string('partials/_comment.html', context)

        return HttpResponse(json.dumps(template), content_type="application/json")


@login_required(login_url='/accounts/login')
def delete_comment(request, pk, pk_comment):
    comment = get_object_or_404(Comment, pk=pk_comment)
    comment.post = Post.objects.get(pk=pk)
    
    # if request.user == comment.user:
    comment.delete()
    # messages.success(request, 'Successfully Deleted')
    # return redirect('detail')
    return redirect(f'/post/{str(comment.post.id)}')
    # else:
    #     messages.error(request, 'Permission Denied')
    #     return redirect('/post/' + str(comment.post.id))