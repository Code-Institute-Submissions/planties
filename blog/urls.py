from . import views
from django.urls import path

urlpatterns = [
    path('', views.posts, name='posts'),
    path('posts/<slug:slug>/', views.PostDetail, name='post_detail'),
]
