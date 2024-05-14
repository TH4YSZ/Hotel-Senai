from django.shortcuts import render, HttpResponse
from .models import *

# Create your views here.
def homepage(request):
    context = {}
    dados_hotel = Hotel.objects.all() #consulta no banco de dados trazendo todas as informações do hotel por meio de um objeto
    context["dados_hotel"] = dados_hotel
    return render(request, 'homepage.html', context)

def quartos(request):
    context = {}
    context2 = {}
    dados_quarto = Quarto.objects.all() 
    dados_hotel = Hotel.objects.all()
    
    context["dados_quarto"] = dados_quarto
    
    return render(request, 'quartos.html', context)