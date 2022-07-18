from django.shortcuts import render
from django.contrib.auth import authenticate,login as auth_login
from auth import forms
from django.http import HttpResponseRedirect
from django.contrib.auth.views import LoginView,LogoutView

# Create your views here.
class Login(LoginView):
    template_name='auth/login.html'
    redirect_authenticated_user =True
    success_url='/'

class Logout(LogoutView):
    template_name='auth/logout.html'

def login(request):
    loginform=forms.LoginForm()
    error=None
    if request.method=='POST':
        loginform=forms.LoginForm(request.POST)
        if loginform.is_valid():
            username=loginform.cleaned_data['username']
            password=loginform.cleaned_data['password']
            user=authenticate(username=username, password=password)
            if user:
                auth_login(request,user)
                return HttpResponseRedirect('/')
            else:
                error='Invalid password or username'
    context ={
        'form':loginform,
        'error':error 
        }
    return render(request,'auth/login.html',context)


