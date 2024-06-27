from django.contrib import admin
from .models import User_quiz, Score, Question, Option

admin.site.register(User_quiz)
admin.site.register(Question)
admin.site.register(Score)
admin.site.register(Option)
