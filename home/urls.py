from django.urls import path
from . import views

# this is the root url
urlpatterns = [
    path('', views.index, name='home'),
    path('about_us/', views.about_us, name='about_us')
]
