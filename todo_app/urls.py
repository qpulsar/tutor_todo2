from django.contrib import admin
from django.urls import path, include

from todo_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('create/', views.create, name='create'),
]
