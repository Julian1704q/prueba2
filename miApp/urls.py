from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),  
    path('categoria/', views.categoria, name="categoria"),
    path('producto/', views.detalle, name='detalle'),
]