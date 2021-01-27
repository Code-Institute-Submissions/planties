from . import views
from django.urls import path

urlpatterns = [
    path('', views.posts, name='posts'),
    path('<str:slug>', views.post_detail, name='post_detail'),
]
