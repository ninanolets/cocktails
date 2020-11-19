from django.contrib import messages
from .models import CommentLike
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import json


def comment_like(request, pk, comment_pk):
    if request.user.is_anonymous:
        messages.error(request, 'You must be logged in to like comments.')
    return comment_like2(request, pk, comment_pk)

@login_required
def comment_like2(request, pk, comment_pk):

    commentlike = CommentLike.objects.filter(comment=comment_pk, user=request.user.id)
    
    if commentlike:
        commentlike.delete()
        
        res = {'isLiked': False}

        return HttpResponse(json.dumps(res), content_type="application/json")
    
    else:
        commentlike = CommentLike(comment_id=comment_pk, user_id=request.user.id)
        commentlike.save()

        res = {'isLiked': True}

        return HttpResponse(json.dumps(res), content_type="application/json")
