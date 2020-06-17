from django.db import models

# Create your models here.
class Response_json(models.Model):
    response_json  = models.TextField()

class Matches(models.Model):
    user_id = models.CharField(max_length=1000)
    match_id = models.CharField(max_length=1000)
