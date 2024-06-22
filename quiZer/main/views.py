from django.shortcuts import render

def home(request):
    return render(request, 'main/home.html')

def login(request):
    return render(request, 'main/registration/login.html')

def sign_up(request):
    return render(request, 'main/registration/sign_up.html')
# Create your views here.
