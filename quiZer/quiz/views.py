from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from  .forms import QuizForm, QuestionFormset

'''
@login_required
def add_quiz(request):
    quiz_form=QuizForm(request.POST or None,request.FILES or None)
    question_formset=QuestionFormset(request.POST or None)
    if question_formset.is_valid() and quiz_form.is_valid():
        quiz_instance=quiz_form.save(commit=False)
        quiz_instance.user=request.user
        quiz_instance.save()
        instance = question_formset.save(commit=False)
        for i in instance:  
            i.quiz_question=quiz_instance        
        for i in instance:
            i.save()
        return redirect('quiz/add/')
    return render(request, 'quiz/create_quiz.html', {'question_form': question_fromset,'quiz_form':quiz_form})


@login_required
def edit_quiz(request):

    return

@login_required
def view_quiz(request):

    return
'''