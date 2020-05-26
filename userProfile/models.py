from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .enums import *



class AdditionalQuestions(models.Model):
    name = models.CharField(max_length=1000,default='')
    # questions_count = models.IntegerField(default=0)
    #description = models.CharField(max_length=70)
    created = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    # slug = models.SlugField()
    #roll_out = models.BooleanField(default=False)
    class Meta:
        ordering = ['created',]
        verbose_name_plural ="Additional Questions"
    def __str__(self):
        return self.name

class Question(models.Model):
    question_form = models.ForeignKey(AdditionalQuestions, on_delete=models.CASCADE)
    label = models.CharField(max_length=1000)
    order = models.IntegerField(default=0)
    def __str__(self):
        return self.label

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)
    # is_correct = models.BooleanField(default=False)
    def __str__(self):
        return self.text


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(default='profileimage.png', null = True, blank=True)
    question_form = models.ForeignKey(AdditionalQuestions, on_delete=models.CASCADE, null = True)
    email_confirmed = models.BooleanField(default=False)
    first_name = models.CharField(max_length=30, default='')
    last_name = models.CharField(max_length=30, default='')
    phone = models.CharField(max_length = 15, blank=True, help_text='(000) 000-000')
    user_type = models.CharField(max_length = 20, choices=UserChoice.choices(), default = 'mentee')
    job_title = models.CharField(max_length=30, default='')
    company = models.CharField(max_length=30, default='')
    county = models.CharField(max_length = 20, choices=CountyChoice.choices(), default = '')
    gender_pronouns  = models.CharField(max_length = 20, choices=GenderChoice.choices(), default = '')
    ethnicity  = models.CharField(max_length = 20, choices=EthnicityChoice.choices(), default = '')
    education = models.CharField(max_length = 20, choices=EducationChoice.choices(), default = '')
    industry = models.CharField(max_length = 20, choices=IndustryChoice.choices(), default = '')
    learningtrack = models.CharField(max_length = 20, choices=TrackChoice.choices(), default = '')
    linkedin = models.URLField(max_length = 60, default = '')
    funfact = models.CharField(max_length=100, default='')
    cohort = models.CharField(max_length = 20, choices=CohortChoice.choices(), default = '')
    site_location = models.CharField(max_length = 20, choices=SiteChoice.choices(), default = '')
    # x = models.FloatField()
    # y = models.FloatField()
    # width = models.FloatField()
    # height = models.FloatField()

    def __str__(self):
        return self.user.username


class Response(models.Model):
    question_form = models.ForeignKey(AdditionalQuestions, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, null = True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    answer = models.ForeignKey(Answer,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.question.label


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        instance.profile.save()

class FrequentlyAsked(models.Model):
    question = models.CharField(max_length=1000, default='')
    answer = models.TextField(max_length=5000, default='')
    class Meta:
        verbose_name_plural ="Frequently Asked Questions Mentee"
    def __str__(self):
        return self.question

class FrequentlyAskedMentor(models.Model):
    mentor_questions = models.CharField(max_length=1000, default='')
    mentor_answers = models.TextField(max_length=5000, default='')
    class Meta:
        verbose_name_plural="Frequently Asked Questions Mentor"
    def __str__(self):
        return self.mentor_questions
