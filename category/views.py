from django.http import HttpResponse
from django.shortcuts import render

# Sample view to display a list of categories
def category_list(request):
    categories = ['Technology', 'Health', 'Education', 'Sports']  # sample data
    return render(request, 'category/category_list.html', {'categories': categories})

# Sample view to display details of a single category
def category_detail(request, category_name):
    return HttpResponse(f"Details for category: {category_name}")


