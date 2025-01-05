# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_movie/', views.add_movie, name='add_movie'),
    path('get_movies/', views.get_movies, name='get_movies'),
    path('movie_links/', views.url, name='movie_links'), 
    path('knowus/',views.knowus,name='knowus'),
]
