from django.shortcuts import redirect, render, get_object_or_404, HttpResponse
from .forms import ContactForm
from .models import AboutMe, Achievement, Contact, Experience, Info, Work
from django.contrib import messages
# Create your views here.
from django.core.mail import EmailMessage
from django.template.loader import render_to_string


def information(request):
    info = Info.objects.all()
    return info


def aboutme(request):
    me = AboutMe.objects.all()
    return me


def achievement(request):
    achieve = Achievement.objects.all()
    return achieve


def experience(request):
    experience = Experience.objects.all().order_by('-created_at')
    return experience


def works(request):
    projects = Work.objects.all()
    return projects


def index(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            is_exist = Contact.objects.filter(email=email).exists()
            if is_exist:
                messages.error(
                    request, f" {name} your email already exists...")
                return redirect('index')
            else:
                user = Contact.objects.create(
                    name=name, email=email, subject=subject, message=message)
                user.save()
                messages.success(
                    request, f"Hey!! {name} thanks for reaching out.We will be in touch soon...")
                # send order received email to the customer
                mail_subject = 'Thank you for reaching out!!!.'
                message = render_to_string('home/order_recieved_email.html', {
                    'name': name,
                    'subject': subject,
                    'message': message,
                })
                to_email = email
                send_email = EmailMessage(
                    mail_subject, message, to=[to_email])
                send_email.send()
                return redirect('index')
    else:
        form = ContactForm()

    context = {
        'form': form,
        'projects': works(request),
        'experiences': experience(request),
        'achievement': achievement(request),
        'me': aboutme(request),
        'info': information(request),

    }

    return render(request, 'home/index.html', context)
