from django.shortcuts import render
from django.http import HttpResponse

#from .models import Movie

def home(request):
    #return render(request,'home.html', {'name':'Victor Manuel Botero The Best'})
    #return HttpResponse('<h1>Welcome To Home Page</h1>')
    searchterm = request.GET.get('searchMovie')
    #if searchterm:
    #    movies = Movie.objects.filter(title__icontains=searchterm)
    #else:
    #    movies = Movie.objects.all()
    #return render(request,'home.html', {'searchterm': searchterm, 'movies': movies})
    return render(request,'home.html', {'searchterm': searchterm})
    
def about(request):
    return render(request,'about.html')