from django.urls import path
from . import views

urlpatterns = [
    path('', views.services, name="services"),
    path('detalle/<int:id>/',views.detalle,name='detalle'),  
]