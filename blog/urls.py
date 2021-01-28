from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts, name='posts'),
    path('posts/<slug:slug>/', views.post_detail, name='post_detail'),
    path('edit_post/<slug:slug>/', views.edit_post, name='edit_post'),
    path('add_post/', views.add_post, name='add_post'),
]
