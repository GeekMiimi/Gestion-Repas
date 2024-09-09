from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
# Create your views here.

def index(request):
   return render(request, 'pages/index.html')

def about(request):
   return render(request, 'pages/about.html')



def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')

        subject = 'Contact Form Submission'
        body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
        from_email = settings.DEFAULT_FROM_EMAIL
        to_email = [settings.EMAIL_HOST_USER]

        try:
            send_mail(subject, body, from_email, to_email)
            success_message = 'Your message has been sent. Thank you for using our services!.Team FoodExpress'
        except Exception as e:
            error_message = 'An error occurred while sending the message.'

    return render(request, 'pages/contact.html')

def subscribe_newsletter(request):
    if request.method == 'POST':
        email = request.POST.get('newsletter-email')

        user_subject = 'Newsletter Subscription Confirmation'
        user_message = 'Thank you for subscribing to our newsletter!.Team FoodExpress'
        user_from_email = settings.EMAIL_HOST_USER
        user_recipient_list = [email]

        send_mail(user_subject, user_message, user_from_email, user_recipient_list)

        app_subject = 'New Newsletter Subscription'
        app_message = f'A new user has subscribed to the newsletter. Email: {email}'
        app_from_email = settings.EMAIL_HOST_USER
        app_recipient_list = [settings.EMAIL_HOST_USER]

        send_mail(app_subject, app_message, app_from_email, app_recipient_list)

    return redirect(request.META['HTTP_REFERER'])




