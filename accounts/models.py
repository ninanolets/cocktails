from django.db import models
from django.contrib.auth.models import User

import os
from django.db.models.signals import post_save
from django.dispatch import receiver
# from utilities.utils import get_filename, rotate_image

# from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default_avatar.png', upload_to='profile_pic')

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


from PIL import Image, ExifTags

def rotate_image(filepath):
    try:
        image = Image.open(filepath)

        if image.height > 300 or image.width > 300:
            output_size = (300, 300)
            image.thumbnail(output_size)
            image.save(filepath)

        for orientation in ExifTags.TAGS.keys():
            if ExifTags.TAGS[orientation] == 'Orientation':
                    break
            exif = dict(image._getexif().items())

            if exif[orientation] == 3:
                image = image.rotate(180, expand=True)
            elif exif[orientation] == 6:
                image = image.rotate(270, expand=True)
            elif exif[orientation] == 8:
                image = image.rotate(90, expand=True)
            image.save(filepath)
            image.close()
    except (AttributeError, KeyError, IndexError):
        # cases: image don't have getexif
        pass


@receiver(post_save, sender=Profile, dispatch_uid="update_image_profile")
def update_image(sender, instance, **kwargs):
  if instance.image:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    fullpath = BASE_DIR + instance.image.url
    rotate_image(fullpath)