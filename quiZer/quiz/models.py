from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.urls import reverse

class User_quiz(models.Model):
    def __str__(self):
        return self.title
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='user_quiz')
    title = models.CharField(max_length=250, null=False,unique=True)
    slug = models.SlugField(null=True, blank=True)
    reattempt = models.BooleanField(default=True, verbose_name='allow reattempts')
    privacy = models.BooleanField(default=False, verbose_name='private')
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(User_quiz, self).save(*args, **kwargs)

class Question(models.Model):
    quiz = models.ForeignKey(User_quiz, on_delete=models.CASCADE,related_name='quiz_question')
    slug = models.SlugField(null=True, blank=True,max_length=60)
    question = models.TextField(default='')
    option_type = models.CharField(max_length=1024, default='')
    points=models.PositiveIntegerField(default=1,verbose_name='points')
    def __str__(self):
        return f'{self.question}'
    def save(self, *args, **kwargs):
        self.slug = slugify(self.question[:50])
        super(Question, self).save(*args, **kwargs)

class Score(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    quiz=models.ForeignKey(User_quiz, on_delete=models.CASCADE,related_name='score_quiz') 
    score=models.IntegerField(default=0)
    def __str__(self):
        return f"{self.user}'s score{self.score} in {self.quiz.title}"
    
class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE,related_name='question_option')
    option = models.CharField(max_length=1024, default='')
    answer = models.BooleanField(default=False, verbose_name='answer')
    def __str__(self):
        return f'{self.option}'