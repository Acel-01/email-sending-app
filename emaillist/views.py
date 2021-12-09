from .models import Email
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

class EmailCreateView(CreateView):
    model = Email
    template_name = 'emaillist/add_email.html'
    fields = ('email',)
    success_url = reverse_lazy('add_email')

class EmailDeleteView(DeleteView): 
    model = Email
    template_name = 'emaillist/delete_email.html'
    success_url = reverse_lazy('list_email')

class EmailListView(ListView):
    model = Email
    template_name = 'emaillist/list_email.html'

# Send Bulk Email
from django.shortcuts import render
from django.core.mail import send_mail

def send_email(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        send_mail(subject, message, 'emekaaladimma@gmail.com', list(Email.objects.all().values_list('email',flat=True)))
    return render(request, 'emaillist/send_email.html')
