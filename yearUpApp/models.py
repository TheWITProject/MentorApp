from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from enum import Enum, EnumMeta
from django.utils.translation import gettext as _
from django.forms import Form, ChoiceField
# class User_type(models.TextChoices):
#     MENTOR = 'MTR', _('Mentor')
#     MENTEE = 'MNT', _('Mentee')
#     ADMIN = 'ADM', _('Admin')



CHOICE_LIST = [
    ('', '----'), # replace the value '----' with whatever you want, it won't matter
    (1, 'Mentee'),
    (2, 'Mentor'),
    (3, 'Admin')
]

class Profile(models.Model):
    first_name = models.CharField(max_length=250, blank=False)
    last_name = models.CharField(max_length=250, blank=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)
    location = models.CharField(max_length=30, default='default_city', blank=False)
    user_choice = ChoiceField(choices=CHOICE_LIST, blank=False)
    phone_number = models.IntegerField(default=False, blank=False)
    #usertype = models.TextChoices(max_length=10, choices=User_type)
    #password = models.CharField(widget=models.PasswordInput)
    id = models.AutoField(primary_key=True)
def default_city():
    return "Bay Area"



@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
<<<<<<< HEAD
    instance.profile.save()

=======
        instance.profile.save()
>>>>>>> 82e9a713d15e40f52aaf18c5e31f209ab89e90b7
