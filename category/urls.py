from django.urls import path
from . import views

urlpatterns = [
    path('', views.category_list, name='category_list'),
    path('<int:id>/', views.category_detail, name='category_detail'),

]
