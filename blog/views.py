from .models import Post, Comment
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.db.models.functions import Lower
from .forms import CommentForm
from django.contrib import messages
from .forms import PostForm
from django.contrib.auth.models import User


def posts(request):
    """ A view to show all posts, including sorting """

    posts = Post.objects.all()
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'title':
                sortkey = 'lower_title'
                posts = posts.annotate(lower_title=Lower('title'))
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            posts = posts.order_by(sortkey)

    current_sorting = f'{sort}_{direction}'

    context = {
        'posts': posts,
        'current_sorting': current_sorting,
    }

    return render(request, 'blog/posts.html', context)


def post_detail(request, slug):
    """ A view to show individual post details """

    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None

    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    context = {
        'post': post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
    }

    return render(request, 'blog/post_detail.html', context)


def add_post(request):
    """ add a post in the blog """
    if not request.user.is_superuser:
        messages.error(request, 'Forbidden! Only the Admin can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username=request.user.username)
            form.instance.author = user
            post = form.save()
            messages.success(request, 'Successfully added post!')
            return redirect(reverse('post_detail', args=[post.slug]))
        else:
            messages.error(
                request,
                'Failed to add post. Please ensure the form is valid.'
                )
    else:
        form = PostForm()

    context = {
        'form': form,
    }

    return render(request, 'blog/add_post.html', context)


def edit_post(request, slug):
    """ Edit a post in the blog """
    if not request.user.is_superuser:
        messages.error(request, 'Forbidden! Only the Admin can do that.')
        return redirect(reverse('home'))

    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated post!')
            return redirect(reverse('post_detail', args=[slug]))
        else:
            messages.error(
                request,
                'Failed to update post. Please ensure the form is valid.'
                )
    else:
        form = PostForm(instance=post)
        messages.info(request, f'You are editing {post.title}')

    context = {
        'form': form,
        'post': post,
    }

    return render(request, 'blog/edit_post.html', context)


def delete_post(request, slug):
    """ delete a post in the blog """
    if not request.user.is_superuser:
        messages.error(request, 'Forbidden! Only the Admin can do that.')
        return redirect(reverse('home'))

    post = get_object_or_404(Post, slug=slug)
    post.delete()
    messages.success(request, 'Successfully deleted post!')
    return redirect(reverse('posts'))


def delete_comment(request, slug, comment_id):
    """ delete comments if super.user """
    if not request.user.is_superuser:
        messages.error(request, 'Forbidden! Only the Admin can do that.')
        return redirect(reverse('home'))

    post = get_object_or_404(Post, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    messages.success(request, 'Comment successfully deleted!')
    return redirect(reverse('post_detail', args=[slug]))
