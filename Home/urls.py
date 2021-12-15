from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
    path('',views.homePage, name='Home Page'),
    path('mythology',views.myth, name='myth'),
    path('create',views.create, name='create'),
    path('cricket', views.cricket, name='cricket'),
]