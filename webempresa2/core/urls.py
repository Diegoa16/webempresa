from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    # Paths del core
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path("newsletter/", views.newsletter, name="newsletter"),

]