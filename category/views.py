from django.http import HttpResponse
from django.shortcuts import render
from .models import Category

# Sample view to display a list of categories
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category/category_list.html', {'categories': categories})

# Sample view to display details of a single category
def category_detail(request, category_name):
    return HttpResponse(f"Details for category: {category_name}")


