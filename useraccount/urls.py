from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('login/', views.custom_login, name='custom_login'),
    path('signup/', views.signup_view, name='signup'),
]
