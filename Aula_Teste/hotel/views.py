from django.shortcuts import render, HttpResponse
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.conf import settings
from django.shortcuts import redirect

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

    # POST para validação
    if not request.user.is_authenticated:
        return render(request, 'login')
    
    else:
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

                return redirect("quartos")
            else:
                return redirect("reserva")
        # GET
        else:
            form = FormReserva()

        return render(request, "reserva.html", {"form": form})


def cadastro(request):

    if request.method == "POST":
        form = FormCadastro(request.POST)
        if form.is_valid():

            var_first_name = form.cleaned_data['first_name']
            var_last_name = form.cleaned_data['last_name']
            var_user = form.cleaned_data['user']
            var_email = form.cleaned_data['email']
            var_password = form.cleaned_data['password']

            user = User.objects.create_user(username= var_user, email=var_email, password=var_password)
            user.first_name = var_first_name
            user.last_name = var_last_name
            user.save()

            return redirect("login")
        else:
            return redirect("cadastro")

    else:
        form = FormCadastro()

    return render(request, "cadastro.html", {"form": form})


def login(request):

    if request.method == "POST":
        form = FormLogin(request.POST)
        if form.is_valid():
            
            var_user = form.cleaned_data['user']
            var_password = form.cleaned_data['password']

            user = authenticate(username=var_user, password=var_password)

            if user is not None:
                return redirect("quartos")
            else:
                return redirect("login")

    # GET
    else:
        form = FormLogin()

    return render(request, "login.html", {"form": form})
