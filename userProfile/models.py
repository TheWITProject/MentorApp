from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .enums import *
from django.utils.translation import ugettext_lazy as _

#class Quiz
class AdditionalQuestions(models.Model):
    name = models.CharField(max_length=1000,default='')
    questions_count = models.IntegerField(default=0)
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

    def __init__(self, *args, **kwargs):
        try:
            question = Question.objects.get(pk=kwargs["question_id"])
        except KeyError:
            question = kwargs.get("question")
            print("action failed")
        # body = kwargs.get("body")
        # if question and body:
        #     self.check_answer_body(question, body)
        super(Answer, self).__init__(*args, **kwargs)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)     #ONetoOne vs ForeignKey (Document)
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

    def __init__(self, *args, **kwargs):
        try:
            answer = Answer.objects.filter(question_id="1")
        except KeyError:
            #question = kwargs.get("question")
            print("response failed")
        # body = kwargs.get("body")
        # if question and body:
        #     self.check_answer_body(question, body)
        super(Response, self).__init__(*args, **kwargs)

@receiver(post_save, sender=User)  #AdditionalQuestions instead of User
def update_user_profile(sender, instance, created, **kwargs):
    question_form = AdditionalQuestions.objects.filter(id = instance.id)

    if created:
        Profile.objects.create(user=instance.id)  #ADDED ID
        instance.profile.save()

        question_form.update(questions_count=instance.question_set.filter(question_form=instance.pk).count())

# ADDED THIS
@receiver(post_save, sender=Question)
def set_default(sender, instance, created,**kwargs):
    question_form = AdditionalQuestions.objects.filter(id = instance.question_form.id)

    question_form.update(questions_count=instance.question_form.question_set.filter(question_form=instance.question_form.pk).count())


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

class Email(models.Model):
    from_email = models.CharField(max_length=1000, default='')
    to_email = models.CharField(max_length=20000, default='', blank=True)
    email_mentors = models.BooleanField(default=False, verbose_name=_('Email All Mentors'))
    email_mentees = models.BooleanField(default=False, verbose_name=_('Email All Mentees'))
    cc_to_email = models.CharField(max_length=20000, default='', blank=True, verbose_name=_('CC:'))
    cc_email_mentors = models.BooleanField(default=False, verbose_name=_('CC All Mentors'))
    cc_email_mentees = models.BooleanField(default=False, verbose_name=_('CC All Mentees'))
    bcc_to_email = models.CharField(max_length=20000, default='', blank=True, verbose_name=_('BCC:'))
    bcc_email_mentors = models.BooleanField(default=False, verbose_name=_('BCC All Mentors'))
    bcc_email_mentees = models.BooleanField(default=False, verbose_name=_('BCC All Mentees'))
    subject = models.CharField(max_length=5000, default='')
    message_email = models.TextField(max_length=30000, default='')
