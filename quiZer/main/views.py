from django.shortcuts import render

def home(request):
    return render(request, 'main/home.html')

def login(request):
    return render(request, 'main/registration/login.html')

def sign_up(request):
    if request.method == 'PoST':
        form = RegisterForm(request.POST)
    else:
        form = RegisterForm()
    return render(request, 'main/registration/sign_up.html', {"form": form})
# Create your views here.
