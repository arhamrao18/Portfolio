from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
# Create your views here.
def index(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        send_mail(
            subject=f"Message from portfolio from {name}",
            message=f"Email is {email}\n Message:\n{message}",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.DEFAULT_EMAIL_RECIPIENT]
        )
        send_mail(
            subject=f"Thank you for contacting me",
            message=f"Hi{name},\n\n Thank you for your message i will back to you soon",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email]
        )
    return render(request,'index.html')
