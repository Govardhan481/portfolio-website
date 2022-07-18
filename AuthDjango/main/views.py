from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
def index(request):
    context={
    }
    return render(request ,'main/index.html',context)

@login_required(login_url='auth/login')
def some(request):
    return HttpResponse('This is a authinticated view')
