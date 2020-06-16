from django.db import models
from userProfile.models import Profile
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Response_json(models.Model):
    response_json  = models.TextField()

class Matches(models.Model):
    user_id = models.CharField(max_length=1000)
    match_id = models.CharField(max_length=1000)

    def __str__(self):
        return self.user_id

   