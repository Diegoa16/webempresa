from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .models import SubscribedUsers
from django.contrib import messages
from django.shortcuts import redirect

# Create your views here.
def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email', None)

        if not email:
            messages.error(request, "Escriba una dirección de email correcta para suscribirse al Newsletter")
            return redirect("/")

        subscribe_user = SubscribedUsers.objects.filter(email=email).first()
        if subscribe_user:
            messages.error(request, "La dirección de email ya aparece suscrita.")
            return redirect(request.META.get("HTTP_REFERER", "/"))

        try:
            validate_email(email)
        except ValidationError as e:
            messages.error(request, e.messages[0])
            return redirect("/")

        subscribe_model_instance = SubscribedUsers()
        subscribe_model_instance.email = email
        subscribe_model_instance.save()
        messages.success(request, f'{email} Registro exitoso!')
        return redirect(request.META.get("HTTP_REFERER", "/"))
