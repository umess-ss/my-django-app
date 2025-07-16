from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),         # root URL now shows home page
    path('learn/', views.index1, name='index1'),
    path('pst/', views.index2, name='index2'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.custom_login, name='custom_login'), 
]
