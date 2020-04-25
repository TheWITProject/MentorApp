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
   inlines = [QuestionInline,]
 
class ResponseInline(admin.TabularInline):
   model = Response
 
class UserResponderAdmin(admin.ModelAdmin):
   inlines = [ResponseInline,]
 
 
admin.site.register(AdditionalQuestions, AdditionalQuestionsAdmin) 
admin.site.register(Response)
admin.site.register(Profile, UserResponderAdmin)

