from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .enums import *


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)
    first_name = models.CharField(max_length=30, default='')
    last_name = models.CharField(max_length=30, default='')
    location = models.CharField(max_length = 50, default='YUBA')
    phone = models.CharField(max_length = 15, blank=True, help_text='(000) 000-000')
    user_type = models.CharField(max_length = 20, choices=UserChoice.choices(), default = 'mentee')
    title = models.CharField(max_length=30, default='')
    company = models.CharField(max_length=30, default='')
    county = models.CharField(max_length = 20, choices=CountyChoice.choices(), default = '')
    gender  = models.CharField(max_length = 20, choices=GenderChoice.choices(), default = '')
    education = models.CharField(max_length = 20, choices=EducationChoice.choices(), default = '')
    industry = models.CharField(max_length = 20, choices=IndustryChoice.choices(), default = '')
    

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        instance.profile.save()