from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from allauth.socialaccount.models import SocialApp

@login_required
def profile(request):
    return render(request, 'home.html')

def custom_login(request):
    form = AuthenticationForm(request)
    google_app = SocialApp.objects.filter(provider='google').first()
    google_client_id = google_app.client_id if google_app else None

    return render(request, 'custom_login.html', {
        'form': form,
        'google_client_id': google_client_id,
    })


# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email    = request.POST['email']
        password = request.POST['password']
        confirm  = request.POST['confirm']

        if password != confirm:
            messages.error(request, "Passwords do not match.")
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('signup')

        user = User.objects.create_user(username=username, email=email, password=password)
        login(request, user)
        messages.success(request, "Account created successfully.")
        return redirect('home')  # or your blog home page
    return render(request, 'signup.html')
