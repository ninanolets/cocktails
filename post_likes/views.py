from django.contrib import messages
from .models import PostLike
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import json



def post_like(request, pk):
    if request.user.is_anonymous:
        messages.error(request, 'You must be logged in to like posts.')
    return post_like2(request, pk)

@login_required
def post_like2(request, pk):
    
    postlike = PostLike.objects.filter(post=pk, user=request.user.id)
    
    if postlike:
        postlike.delete()
        
        res = {'isLiked': False}
        return HttpResponse(json.dumps(res), content_type="application/json")
    
    else:
        postlike = PostLike(post_id=pk, user_id=request.user.id)
        postlike.save()
        
        res = {'isLiked': True}

        return HttpResponse(json.dumps(res), content_type="application/json")

        
