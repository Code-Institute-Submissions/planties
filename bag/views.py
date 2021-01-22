from django.shortcuts import render

# Create your views here.


def view_bag(request):
    """ shows the page with the bags content  """

    return render(request, 'bag/bag.html')
