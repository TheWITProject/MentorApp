from django.contrib import admin
from .models import *

# Register your models here.

#class AnswerTabularInline(admin.TabularInline):
#	model = LocationAnswer


#class QuestionAdmin(admin.ModelAdmin):
#	inlines = [AnswerTabularInline]
#	class Meta:
#		model = LocationQuestion


admin.site.register(Profile)
#admin.site.register(LocationQuestion, QuestionAdmin)
#admin.site.register(LocationAnswer)