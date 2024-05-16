from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name="home"),
    path('quartos', views.quartos, name="quartos"),
    path('reserva', views.reserva, name="reserva")
]