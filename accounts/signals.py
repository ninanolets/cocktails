# this creates a profile with the creation of a user
# following the django documentation to avoid import colisions


from django.db.models.signals import post_save
from  django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    # instance is the user that was just created
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

# now you have to import our signals to apps.py
