from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts, name='posts'),
    path('posts/<slug:slug>/', views.PostDetail, name='post_detail'),
    # path('add_post/', views.add_post, name='add_post'),
    path('edit/<slug:slug>/', views.edit_post, name='edit_post'),
]
