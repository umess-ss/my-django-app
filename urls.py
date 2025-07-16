from django.contrib import admin
from django.urls import path, include  # include is used for app-level urls
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('post.urls')),  # Root path is now handled in post/urls.py
    path('category/',include('category.urls')),
    path('about/',include('about.urls')),
    path('contact/',include('contact.urls')),
    path('accounts/', include('allauth.urls')),
]
