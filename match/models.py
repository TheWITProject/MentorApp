from django.db import models
from userProfile.models import Profile
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


# Create your models here.
class Response_json(models.Model):
    response_json  = models.TextField()

class Matches(models.Model):
    # match_user = models.ManyToManyField(User)
    # match_users= models.ManyToManyField(User)
    puser = models.ForeignKey(Profile, null = True, on_delete=models.CASCADE,related_name='getting_matched')
    match_user = models.ForeignKey(Profile, null = True, on_delete=models.CASCADE, related_name='match_user')
    user_id = models.CharField(max_length=1000)
    match_id = models.CharField(max_length=1000)

    def __str__(self):
        return self.user_id
