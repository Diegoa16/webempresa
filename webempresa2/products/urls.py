from django.urls import path
from . import views
from .views import categories_m

urlpatterns = [
    path('', views.products, name="products"),
    path('detail/<int:id>/',views.detail,name='detail'),
    path('categories/', views.categories_m, name='categories'), 
]