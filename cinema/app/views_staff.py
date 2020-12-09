from django.shortcuts import render
from .models import *
def listCategory(request):
    categoryList = Category.objects.all()
    return render(request,'staff/category/list.html',{'categoryList':categoryList})
def listLanguage(request):
    languageList = Language.objects.all()
    return render(request,'staff/language/list.html',{'languageList':languageList})
def listMovie(request):
    movieList = Movie.objects.all()
    return render(request,'staff/movie/list.html',{'movieList':movieList})
def listMovieShow(request):
    movieshowList = MovieShow.objects.all()
    return render(request,'staff/movie_show/list.html',{'movieshowList':movieshowList})
    