from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('addsnitch/', views.addsnitch),
    path('topics/', views.topics),
    path('topicc/<str:pk>/', views.topicc),
    path(
        'snitchh/<str:sk>/',
        views.snitchh,
    ),
    path('upvote/<str:sk>/<str:link>/', views.upvote),
    path('downvote/<str:sk>/<str:link>/', views.downvote),
    path('login/', views.loginn, name="loginn"),
    path('logout/', views.logoutt),
]
