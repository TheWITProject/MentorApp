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
 
# class ResponseInline(admin.TabularInline):
#    model = Response
#    def formfield_for_foreignkey(self,db_field , request, **kwargs):
#       list_display = (self.model.question,)
#       if db_field.name == "answer":
#          kwargs["queryset"] = Answer.objects.filter(question_id = list_display[0].id)
#       return super().formfield_for_foreignkey(db_field, request, **kwargs)
  
class ResponseInline(admin.TabularInline):
   model = Response
   # question = model.question
   # print (question.answers.all())
   # def formfield_for_foreignkey(self, db_field , request, **kwargs):
   #    if db_field.name == "answer":
   #       kwargs["queryset"] = Answer.objects.filter(question_id = self.value)
   #    return super().formfield_for_foreignkey(db_field, request, **kwargs)
 
class ResponseAdmin(nested_admin.NestedModelAdmin):
   list_display = ("question", "user", "question_form")

class UserResponderAdmin(admin.ModelAdmin):
   inlines = [ResponseInline,]
 
 
admin.site.register(AdditionalQuestions, AdditionalQuestionsAdmin) 
admin.site.register(Response, ResponseAdmin)
admin.site.register(Profile, UserResponderAdmin)
