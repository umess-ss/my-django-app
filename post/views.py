from django.shortcuts import render,get_object_or_404
from .models import Post


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

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'post_detail.html', {'post': post})