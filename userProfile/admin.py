from django.contrib import admin
from .models import *
import nested_admin
from django.core.mail import EmailMessage
# from import_export import resources
from import_export.admin import ImportExportModelAdmin


# class ProfileExport(resources.ModelResource):
#     class Meta:
#         model = Profile

# @admin.register(Profile)
class ProfileAdmin(ImportExportModelAdmin):
    pass

class AnswerInline(nested_admin.NestedTabularInline):
   model = Answer
   extra = 4
   # max_num = 4
 
class QuestionInline(nested_admin.NestedTabularInline):
   model = Question
   inlines = [AnswerInline,]
   extra = 0
 
class AdditionalQuestionsAdmin(nested_admin.NestedModelAdmin):
   list_display = ("name","created")
   inlines = [QuestionInline,]
 
class ResponseInline(admin.TabularInline):
   model = Response
 
class ResponseAdmin(nested_admin.NestedModelAdmin):
   list_display = ("question", "user", "question_form")

class UserResponderAdmin(admin.ModelAdmin):
   inlines = [ResponseInline,]

class EmailAdmin(admin.ModelAdmin):
   list_display = ("from_email", "to_email", "email_mentors", "email_mentees", "cc_to_email", "cc_email_mentors", "cc_email_mentees","bcc_to_email", "bcc_email_mentors", "bcc_email_mentees", "subject", "message_email")
   def save_model(self, request, obj, form, change): 
      data = request.POST

      to_recipients = []
      cc_recipients = []
      bcc_recipients = []

      from_email = data.get("from_email")
      to_email = data.get("to_email")
      
      email_mentors = data.get("email_mentors")
      email_mentees = data.get("email_mentees")

      cc_to_email = data.get("cc_to_email")
      cc_email_mentors = data.get("cc_email_mentors")
      cc_email_mentees = data.get("cc_email_mentees")

      bcc_to_email = data.get("bcc_to_email")
      bcc_email_mentors = data.get("bcc_email_mentors")
      bcc_email_mentees = data.get("bcc_email_mentees")

      subject = data.get("subject")
      message_email = data.get("message_email")

      if email_mentees:
         mentees = list(Profile.objects.filter(user_type = "IS_MENTEE"))
         for each in mentees:
            to_recipients.append(User.objects.get(pk=each.user.pk).email)
      if email_mentors:
         mentors = list(Profile.objects.filter(user_type = "IS_MENTOR"))
         for each in mentors:
            to_recipients.append(User.objects.get(pk=each.user.pk).email) 
      to_recipients.append(to_email)
      to_recipients = list(set(to_recipients))
      
      if cc_email_mentees:
         cc_mentees = list(Profile.objects.filter(user_type = "IS_MENTEE"))
         for each in cc_mentees:
            cc_recipients.append(User.objects.get(pk=each.user.pk).email)
      if cc_email_mentors:
         cc_mentors = list(Profile.objects.filter(user_type = "IS_MENTOR"))
         for each in cc_mentors:
            cc_recipients.append(User.objects.get(pk=each.user.pk).email) 
      cc_recipients.append(cc_to_email)
      cc_recipients = list(set(cc_recipients))

      if bcc_email_mentees:
         bcc_mentees = list(Profile.objects.filter(user_type = "IS_MENTEE"))
         for each in bcc_mentees:
            bcc_recipients.append(User.objects.get(pk=each.user.pk).email)
      if bcc_email_mentors:
         bcc_mentors = list(Profile.objects.filter(user_type = "IS_MENTOR"))
         for each in bcc_mentors:
            bcc_recipients.append(User.objects.get(pk=each.user.pk).email) 
      bcc_recipients.append(bcc_to_email)
      bcc_recipients = list(set(bcc_recipients))

      email = EmailMessage(subject, message_email, from_email, to_recipients, bcc_recipients, cc=cc_recipients)
      email.send()
      obj.save()

admin.site.register(AdditionalQuestions, AdditionalQuestionsAdmin) 
admin.site.register(Response, ResponseAdmin)
admin.site.register(Profile, UserResponderAdmin)
admin.site.register(FrequentlyAsked)
admin.site.register(FrequentlyAskedMentor)
admin.site.register(Email, EmailAdmin)


