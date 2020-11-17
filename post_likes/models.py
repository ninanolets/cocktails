from django.db import models
from django.contrib.auth.models import User
from posts.models import Post

class PostLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)   
    post = models.ForeignKey(Post, related_name="postlikes", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)