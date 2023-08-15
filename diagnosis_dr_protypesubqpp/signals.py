from django.db.models.signals import post_save
from django.contrib.auth.models import User 
from .models import *


def user_create_profile(sender , instance ,created , **kwargs):
    if created:
         user = User.objects.get(name="Doctor",name="Dr_assints")
         instance.user.add(user)

         User.objects.create(
             user = instance,
             name= instance.username
         )
         print('User profile created !')

post_save.connect(user_create_profile , sender=User)