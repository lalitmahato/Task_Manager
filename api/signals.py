from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import UserProfile
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=User)
def build_profile(sender,instance,created,**kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
    token = Token.objects.create(user=instance)
    token.save()