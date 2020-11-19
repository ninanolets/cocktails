from django.db import models
from django.contrib.auth.models import User
from comments.models import Comment

class CommentLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)   
    comment = models.ForeignKey(Comment, related_name="commentlikes", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)