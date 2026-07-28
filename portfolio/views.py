import logging
from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from django.http import HttpResponse

logger = logging.getLogger(__name__)

# Create your views here.
def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        try:
            send_mail(
                subject=f"Message from portfolio from {name}",
                message=f"Email is {email}\n Message:\n{message}",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.DEFAULT_EMAIL_RECIPIENT],
                fail_silently=False,
            )
            send_mail(
                subject="Thank you for contacting me",
                message=f"Hi {name},\n\nThank you for your message, I will get back to you soon.",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[email],
                fail_silently=False,
            )
            messages.success(request, "Your message has been sent successfully!")
        except Exception as e:
            # Ye asal error ab Render Logs mein clean dikhega, page crash nahi hoga
            logger.error(f"Email sending failed: {e}")
            messages.error(request, "Sorry, something went wrong while sending your message. Please try again later.")

    return render(request, 'index.html')