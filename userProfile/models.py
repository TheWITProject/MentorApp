from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .enums import *



#class LocationQuestion(models.Model):
#    text = models.TextField()
#    active = models.BooleanField(default=True)
#    draft = models.BooleanField(default=False)
#    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    #issue is that profile_id can't be null
    #last working migration is 0010
    #profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
#    def __unicode__(self):
#        return self.text[:10]
#    def __str__(self):
#        return self.text

#class LocationAnswer(models.Model):
#    question = models.ForeignKey(LocationQuestion, on_delete=models.CASCADE)
#    text = models.CharField(max_length=120)
#    active = models.BooleanField(default=True)
#    draft = models.BooleanField(default=False)
#    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
#    def __unicode__(self):
#        return self.text[:10]
#    def __str__(self):
#        return self.text


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(default='profileimage.png', null = True, blank=True)
    #location_q = models.ForeignKey(LocationAnswer, on_delete=models.CASCADE, null = True)
    email_confirmed = models.BooleanField(default=False)
    first_name = models.CharField(max_length=30, default='')
    last_name = models.CharField(max_length=30, default='')
    phone = models.CharField(max_length = 15, blank=True, help_text='(000) 000-000')
    user_type = models.CharField(max_length = 20, choices=UserChoice.choices(), default = 'mentee')
    title = models.CharField(max_length=30, default='')
    company = models.CharField(max_length=30, default='')
    county = models.CharField(max_length = 20, choices=CountyChoice.choices(), default = '')
    gender  = models.CharField(max_length = 20, choices=GenderChoice.choices(), default = '')
    ethnicity  = models.CharField(max_length = 20, choices=EthnicityChoice.choices(), default = '')
    education = models.CharField(max_length = 20, choices=EducationChoice.choices(), default = '')
    industry = models.CharField(max_length = 20, choices=IndustryChoice.choices(), default = '')
    learningtrack = models.CharField(max_length = 20, choices=TrackChoice.choices(), default = '')
    linkedin = models.URLField(max_length = 60, default = '')
    funfact = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        instance.profile.save()


