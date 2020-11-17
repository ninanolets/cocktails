from django.db import models
from django.contrib.auth.models import User
from posts.models import Post

class CommentLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)   
    comment = models.ForeignKey(Post, related_name="commentlikes", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)