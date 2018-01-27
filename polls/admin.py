from django.contrib import admin
from polls.models import Question, Choice

'''
class QuestionAdmin(admin.MOdelAdmin):
	fields = ['pub_date', 'question_text'] #필드 순서 변경
'''

admin.site.register(Question)
admin.site.register(Choice)


# Register your models here.

