from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from allauth.socialaccount.models import SocialApp
from .models import post


from django.shortcuts import render

def index(request):
    posts = post.objects.all()
    return render(request, 'home.html', {
        "posts": posts
    })


def index1(request):
    return render(request, 'learn.html')

def index2(request):
    return render(request, 'pst.html')

@login_required
def profile(request):
    # your code here
    return render(request, 'home.html')

def custom_login(request):
    form = AuthenticationForm(request)
    google_app = SocialApp.objects.filter(provider='google').first()
    google_client_id = google_app.client_id if google_app else None

    return render(request, 'custom_login.html', {
        'form': form,
        'google_client_id': google_client_id,
    })
