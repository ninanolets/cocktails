from django.db import models
from django.contrib.auth.models import User
from posts.models import Post
from datetime import datetime

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    
    body = models.TextField(blank=False)
    pub_date = models.DateTimeField(default=datetime.now, blank=True)
    update_date = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        ordering = ['-pub_date']

    def approve(self):
        self.approved_comment = True
        self.save()
        
    def __str__(self):
        return self.body or ''
    
    def costume_pub_date(self):
        return self.pub_date.strftime('%b %e %Y')
    
    def compare_pub_date(self):
        return self.pub_date.strftime('%b %e %Y %H %M %S')
    
    # def compare_pub_date(self):
    #     return self.update_date.strftime('%b %e %Y %H %M %S')
