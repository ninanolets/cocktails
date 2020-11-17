from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.urls import reverse

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    title = models.CharField(max_length=23)
    sub_title = models.CharField(max_length=150, default=None)
    image = models.ImageField(default='thumbnail.jpeg', upload_to="photos/%Y/%m/%d/")
    body = models.TextField(default='')
    pub_date = models.DateField(default=datetime.now, blank=True)
    update_date = models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):
        return self.title or ''

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})
    
    def costume_sub_title(self):
        return self.sub_title[:35] + "..." if len(self.sub_title) > 30 else self.sub_title
    
    def costume_pub_date(self):
        return self.pub_date.strftime('%b %e %Y')
    
    # def compare_pub_date(self):
    #     return self.pub_date.strftime('%b %e %Y %H %M %S')
    
    # def compare_update_date(self):
    #     return self.update_date.strftime('%b %e %Y %H %M %S')


    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk": self.pk})
    