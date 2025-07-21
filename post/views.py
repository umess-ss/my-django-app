from django.shortcuts import render,get_object_or_404,redirect
from .models import Post
from django.contrib.auth.decorators import login_required
from .forms import CommentForm

from django.shortcuts import render

def index(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {
        "posts": posts
    })


def index1(request):
    return render(request, 'learn.html')

def index2(request):
    return render(request, 'pst.html')

# def post_detail(request, slug):
#     post = get_object_or_404(Post, slug=slug)
#     return render(request, 'post_detail.html', {'post': post})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.all().order_by('-created_at')

    if request.user.is_authenticated:
        form = CommentForm(request.POST or None)
        if request.method == 'POST' and form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = None

    return render(request, 'post_detail.html', {
        'post': post,
        'comments': comments,
        'form': form,
    })