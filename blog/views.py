from .models import Post
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.db.models.functions import Lower
from .forms import CommentForm
from django.contrib import messages
from .forms import PostForm


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


def PostDetail(request, slug):
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
