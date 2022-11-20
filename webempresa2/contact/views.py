from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.
def contact(request):
    contact_form = ContactForm()

    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            subject = request.POST.get('subject', '')
            content = request.POST.get('content', '')
            #enviamos el correo y redireccionamos
            email = EmailMessage(
                "Meteoagro SAS: Nuevo mensaje de contacto",
                "De {} <{}>\n\nAsunto: {}\nEscribió:\n{}".format(name, email, subject, content),
                "no-contestar@inbox.mailtrap.io",
                ["contacto@meteoagro.co"],
                reply_to=[email]
            )

            try: 
                email.send()
                 # Todo ha ido bien, redireccionamos a ok
                return redirect(reverse('contact')+"?ok")
            except:
                # Algo no ha ido bien, redireccionamos a FAIL
                return redirect(reverse('contact')+"?fail")


    return render(request, "contact/contact.html", {'form':contact_form})


