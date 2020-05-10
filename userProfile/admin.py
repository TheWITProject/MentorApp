from django.contrib import admin
from .models import *
import nested_admin


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
 
 
admin.site.register(AdditionalQuestions, AdditionalQuestionsAdmin) 
admin.site.register(Response, ResponseAdmin)
admin.site.register(Profile, UserResponderAdmin)
admin.site.register(FrequentlyAsked)

