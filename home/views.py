from django.shortcuts import render

# Create your views here.


def index(request):
    """ returns the index page """

    return render(request, 'home/index.html')


def about_us(request):
    """ returns the about us page """

    return render(request, 'home/about_us.html')
