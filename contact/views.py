from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .forms import FeedbackForm

class ContactView(FormView):
    template_name = 'contact/contact.html'
    form_class = FeedbackForm
    success_url = reverse_lazy('index')  # Redirect after successful form submission

    def form_valid(self, form):
        form.save()  # Save Feedback instance
        return super().form_valid(form)
