from django.db import models
from django.contrib.auth.models import User
from posts.models import Post

from django.utils import timezone
# from datetime import datetime

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    
    body = models.TextField(blank=False)
    pub_date = models.DateTimeField(default=timezone.now, blank=True)
    update_date = models.DateTimeField(default=timezone.now, blank=True)

    class Meta:
        ordering = ['-pub_date']

    def approve(self):
        self.approved_comment = True
        self.save()
        
    def __str__(self):
        return self.body or ''
    