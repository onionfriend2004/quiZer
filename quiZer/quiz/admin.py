from django.contrib import admin
from .models import User_quiz, Score, Question, Option
from nested_admin import NestedTabularInline, NestedModelAdmin

class OptionAdmin(NestedTabularInline):
    model = Option

class QuestionAdmin(NestedTabularInline):
    model = Question
    inlines = [OptionAdmin]

class User_quizAdmin(NestedModelAdmin):
    inlines = [QuestionAdmin]

admin.site.register(User_quiz, User_quizAdmin)
admin.site.register(Question)
admin.site.register(Score)
admin.site.register(Option)
