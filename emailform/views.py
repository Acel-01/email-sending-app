from django.shortcuts import render
from django.core.mail import send_mail

def index(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        data = {
            'email': email,
            'subject': subject,
            'message': message
        }
        message = '''
        New message: {}

        From: {}        
        '''.format(data['message'], data['email'])
        send_mail(data['subject'], message, '', ['emekaaladimma@gmail.com',data['email']])
    return render(request, 'emailform/index.html', {})