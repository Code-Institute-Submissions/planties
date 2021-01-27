from .models import Post
from django.shortcuts import render


def posts(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }

    return render(request, 'blog/posts.html', context)
