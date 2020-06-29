from django.db import models
from userProfile.models import Profile
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Response_json(models.Model):
    response_json  = models.TextField()

class Matches(models.Model):
    match_profile = models.OneToOneField(Profile, on_delete=models.CASCADE, null =True, related_name = "match_profile")
    user_profile = models.OneToOneField(Profile, on_delete=models.CASCADE, null =True,  related_name = "user_profile")
    profile_search = models.ForeignKey(Profile, on_delete=models.CASCADE, null =True)
    # temp_id = AutoSlugField(populate_from=['match_profile__user_id'])
    # match_user = models.ForeignKey(MatchProfile, on_delete=models.CASCADE, null =True)
    user_id = models.CharField(max_length=1000, blank=True)
    match_id = models.CharField(max_length=1000, blank=True)
    manual_match = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.manual_match:
            self.user_id = str(self.user_profile.user_id)
            self.match_id = str(self.match_profile.user_id)
            self.manual_match = True
            print(self.user_id)
        super(Matches, self).save(*args, **kwargs)

    def __str__(self):
        return self.user_id

    class Meta:
        verbose_name_plural ="Matches"
