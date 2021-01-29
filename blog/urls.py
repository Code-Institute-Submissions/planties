from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts, name='posts'),
    path('posts/<slug:slug>/', views.post_detail, name='post_detail'),
    path('edit_post/<slug:slug>/', views.edit_post, name='edit_post'),
    path('add_post/', views.add_post, name='add_post'),
    path('delete_post/<slug:slug>/', views.delete_post, name='delete_post'),
    path(
        'delete_comment/<slug:slug>/<comment_id>',
        views.delete_comment,
        name='delete_comment'
        ),
]
