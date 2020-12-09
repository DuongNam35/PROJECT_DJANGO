from django.shortcuts import render,get_object_or_404
from .models import *
# Create your views here.

def index(request):
    tickerList = Movie.objects.all()
    return render(request,'index.html',{'tickerList':tickerList})
def viewMovie(request,id):
    movie = get_object_or_404(Movie,pk=id)
    return render(request,'view_movie.html',{'movie':movie})
def bookMovie(request,id):
    moviebooking = Movie.objects.get(id=id)

