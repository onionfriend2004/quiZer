from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import User
from .forms import RegisterForm, UserUpdate, ProfileUpdate
from .models import Profile

@login_required(login_url="/login")
def home(request):
    return render(request, 'main/home.html')

def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            login(request, user)
            return redirect('/home')
    else:
        form = RegisterForm()
    return render(request, 'registration/sign_up.html', {"form": form})

@login_required(login_url="/login")
def profile(request, view_user=None):
    if view_user is not None:
        user=User.objects.get(username=view_user)
        return render(request, 'main/profile.html', {'author':False,'user':user})
    if request.method == 'POST':
        p_form = ProfileUpdate(request.POST,instance=request.user.profile)
        u_form = UserUpdate(request.POST, instance=request.user)

        if u_form.is_valid() and p_form.is_valid():

            u_form.save()
            p_form.save()

            messages.success(request, 'Your Profile has been updated!')
            return redirect('profile')
    else:
        p_form = ProfileUpdate(instance=request.user.profile)
        u_form = UserUpdate(instance=request.user)   
    return render(request, 'main/profile.html', {"p_form": p_form, "u_form": u_form, 'author':True})