from django.contrib import admin
from django.urls import path
from . import views

# this is the root url
urlpatterns = [
    path('', views.index, name='home')
]
