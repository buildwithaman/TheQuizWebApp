from django.shortcuts import render , HttpResponseRedirect , redirect
from django.http import HttpResponseRedirect
from .forms import SignUpForm , LoginForm , ProfileForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate , login ,logout 
from .models import SignUpModel
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        print(request.user)
        profile = SignUpModel.objects.get(username=request.user)
        return render(request , 'home.html' , {"profile":profile})
    return render(request , 'home.html')
    

def register(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = SignUpForm(request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request , "Account Creation Successful")
                return HttpResponseRedirect('/signin/')
                
        else:
            fm = SignUpForm()
        return render(request , 'register.html' ,{"form":fm})
    else:
        return HttpResponseRedirect("/profile/")

def signin(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = LoginForm(request=request , data=request.POST)
            if fm.is_valid():
                username = fm.cleaned_data.get('username')
                password = fm.cleaned_data.get('password')
                account = authenticate(username=username , password=password)
                if account is not None:
                    login(request , account)
                    messages.success(request , "Logged in Successsfully")
                    return redirect('profile', username)
                else:
                    messages.error(request , 'Credentails Does Not Matched')
        else:
            fm = LoginForm()
        return render(request , 'signin.html' , {"form":fm})
    else:
        return redirect('profile' , request.user)

def signout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request , "Logged Out Successfully")
        return HttpResponseRedirect('/')
    else:
        HttpResponseRedirect('/signin/')


def profile(request , username):
    if request.user.is_authenticated:
        profile = SignUpModel.objects.get(username=username)
        return render(request , 'profile.html' , {"profile":profile})
    else:
        return HttpResponseRedirect('/signin/')
    


def leaderboard(request):
    return render(request , 'leaderboard.html')


