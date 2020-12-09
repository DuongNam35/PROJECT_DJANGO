from django.urls import path,include
from .import views, views_staff

urlpatterns =[
    path('',views.index),
    path('movie_detail/<int:id>',views.viewMovie,name='view-movie'),



    path('staff',views_staff.listCategory,name='category-list'),
    path('staff/language_list',views_staff.listLanguage,name='language-list'),
    path('staff/movie_list',views_staff.listMovie,name='movie-list'),
    path('staff/movieshow_list',views_staff.listMovieShow,name='movieshow-list')
]