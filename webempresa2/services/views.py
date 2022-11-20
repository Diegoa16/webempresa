from django.shortcuts import render, get_object_or_404
from .models import Service

# Create your views here.
def services(request):
    services = Service.objects.all()
    return render(request, 'services/services.html', {'services':services})

def detalle(request, id):
    service= get_object_or_404(Service, id=id)
    context= {'service':service}
    return render(request,"services/detalle.html",context)