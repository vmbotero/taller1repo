from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'home.html', {'name':'Greg Lim'})
    #return HttpResponse('<h1>Welcome To Home Page</h1>')