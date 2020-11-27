from django.db import models
from django.contrib.auth.models import User

# import os
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from PIL import Image
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, Transpose, SmartResize


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default_avatar.png', upload_to='profile_pic', max_length=255)

    def __str__(self):
        if self.user.first_name:
            name = self.user.first_name.capitalize()
        else:
            name = self.user.username.capitalize()
            
        return f'{name} Profile'


    
            
    # this method is so you can compress the pictures posted on the webpage
    # we need to use the pillow package to rewrite the save method of the model
    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

    #     img = Image.open(self.image.path)
        
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)


 