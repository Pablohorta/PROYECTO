
from django.urls import path
from . import views

urlpatterns = [
    path("",  views.index, name="index"),
    path("crear-cita/",  views.crear_cita, name="crear-cita"),
    path("crear-autor/",  views.crear_autor, name="crear-autor"),
    path("crear-cliente/",  views.crear_cliente, name="crear-cliente"),
]
