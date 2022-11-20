from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import NewsletterForm
from django.core.mail import EmailMessage
from newsletter.models import SubscribedUsers
from django.urls import reverse

# Create your views here.
def home(request):
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")

def newsletter(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data.get('subject')
            receivers = form.cleaned_data.get('receivers').split(',')
            email_message = form.cleaned_data.get('message')

            mail = EmailMessage(subject, email_message, f"Meteoagro <{'contacto@meteoagro.co'}>", bcc=receivers)
            mail.content_subtype = 'html'

            if mail.send():
                messages.success(request, "Mensaje enviado correctamente")
            else:
                messages.error(request, "Se presentó un error con el envío del email")

        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

        return redirect('/')

    form = NewsletterForm()
    form.fields['receivers'].initial = ','.join([active.email for active in SubscribedUsers.objects.all()])
    return render(request=request, template_name='core/newsletter.html', context={'form': form})