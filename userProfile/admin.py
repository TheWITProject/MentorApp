from django.contrib import admin
from .models import *
import nested_admin

<<<<<<< HEAD
 
=======
>>>>>>> 014f67e89cc597187ccf48b88c40ed3bab8cd76c
class AnswerInline(nested_admin.NestedTabularInline):
   model = Answer
   extra = 4
   # max_num = 4
 
class QuestionInline(nested_admin.NestedTabularInline):
   model = Question
   inlines = [AnswerInline,]
   extra = 0
 
class QuizAdmin(nested_admin.NestedModelAdmin):
   inlines = [QuestionInline,]
 
class ResponseInline(admin.TabularInline):
   model = Response
 
class QuizTakersAdmin(admin.ModelAdmin):
   inlines = [ResponseInline,]
 
 
admin.site.register(Quiz, QuizAdmin) 
admin.site.register(Response)
admin.site.register(Profile, QuizTakersAdmin)
