from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'home.html', {'name':'Victor Manuel Botero The Best'})
    #return HttpResponse('<h1>Welcome To Home Page</h1>')