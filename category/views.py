from django.urls import reverse_lazy
from django.views.generic import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404
from .models import Category
from post.models import Post
from django_components.component_registry import registry
print("Registered components:", registry._registry.keys())

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category/category_list.html', {'categories': categories})


def category_detail(request, id):
    category = get_object_or_404(Category, id=id)
    posts = Post.objects.filter(category=category)
    return render(request, 'category/category_detail.html', {
        'category': category,
        'posts': posts
    })


