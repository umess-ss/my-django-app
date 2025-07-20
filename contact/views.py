from django.shortcuts import render,redirect
from .models import Feedback


# Create your views here.
def contact(request):
    if (request.method == 'POST'):
        name = request.POST.get('name')
        email = request.POST['email']
        message = request.POST['message']
        feedback = Feedback(
            name = name,
            email = email,
            message = message
        )
        feedback.save()
        return redirect("index")
    return render(request,'contact/contact.html')