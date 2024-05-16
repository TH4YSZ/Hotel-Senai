from django.shortcuts import render, HttpResponse
from .models import *
from .forms import FormReserva

# Create your views here.
def homepage(request):
    context = {}
    dados_hotel = Hotel.objects.all() #consulta no banco de dados trazendo todas as informações do hotel por meio de um objeto
    context["dados_hotel"] = dados_hotel
    return render(request, 'homepage.html', context)

def quartos(request):
    context = {}
    dados_quarto = Quarto.objects.all() 
    
    context["dados_quarto"] = dados_quarto
    
    return render(request, 'quartos.html', context)

def reserva(request):
    context = {}
    dados_hotel = Hotel.objects.all()
    context["dados_hotel"] = dados_hotel

    # POST para validação
    if request.method == "POST":
        form = FormReserva(request.POST)
        if form.is_valid():
            # variavel para armazenar o que o formulário passo através do cleaned_data, que manipula o dicionário
            var_nome = form.cleaned_data['nome']
            var_sobrenome = form.cleaned_data['sobrenome']
            var_email = form.cleaned_data['email']
            var_idade = form.cleaned_data['idade']
            var_end = form.cleaned_data['end']
            var_quarto = form.cleaned_data['quarto']
            var_data = form.cleaned_data['data']
            

            user = Reserva(nome=var_nome, sobrenome=var_sobrenome, email=var_email, idade=var_idade, end=var_end, quarto=var_quarto, data=var_data)
            # Armazena a informação no banco
            user.save()

    # GET
    else:
        form = FormReserva()

    return render(request, "reserva.html", {"form": form})