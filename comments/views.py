from django.shortcuts import render
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

        context = { 'comment': new_comment }
        template = render_to_string('partials/_comment.html', context)

        return HttpResponse(json.dumps(template), content_type="application/json")
