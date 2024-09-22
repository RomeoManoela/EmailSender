from django.core.mail import send_mail
from .settings import EMAIL_HOST_USER
from django.shortcuts import render

def send_mail_page(request):
    context = {}
    if request.method == 'POST':
        email_address = request.POST.get('address')
        email_subject = request.POST.get('subject')
        email_message = request.POST.get('message')

        if email_address and email_subject and email_message:
            try:
                send_mail(email_subject, email_message, EMAIL_HOST_USER, [email_address])
                context['result'] = 'success, check your email'
            except Exception as e:
                context['result'] = f'error {e}'
    return render(request, 'email_sender.html', context)
