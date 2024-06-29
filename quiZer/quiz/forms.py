from django import forms
from .models import User_quiz, Question, Option

class QuestionForm(forms.Form):
    class Meta: 
        model=Question
        fields=['question','points']

class OptionForm(forms.ModelForm):
    class Meta:
        model = Option
        fields = ['option', 'is_correct']

QuestionFormset = forms.inlineformset_factory(User_quiz, Question, form=QuestionForm, extra=1)

class QuizForm(forms.ModelForm):
    class Meta:
        model=User_quiz
        fields=['title','reattempt','privacy'] 