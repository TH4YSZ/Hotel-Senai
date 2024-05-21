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

    dados_hotel = Hotel.objects.all() 
    context["dados_hotel"] = dados_hotel
    
    context["dados_quarto"] = dados_quarto
    
    return render(request, 'quartos.html', context)

def reserva(request):
    context = {}
    dados_hotel = Hotel.objects.all()
    context["dados_hotel"] = dados_hotel

    if not request.user.is_authenticated:
        return render(request, 'login.html', context)

    if request.method == "POST":
        form = FormReserva(request.POST)
        if form.is_valid():
            var_nome = form.cleaned_data['nome']
            var_sobrenome = form.cleaned_data['sobrenome']
            var_email = form.cleaned_data['email']
            var_idade = form.cleaned_data['idade']
            var_end = form.cleaned_data['end']
            var_quarto = form.cleaned_data['quarto']
            var_data = form.cleaned_data['data']

            user = Reserva(nome=var_nome, sobrenome=var_sobrenome, email=var_email, idade=var_idade, end=var_end, quarto=var_quarto, data=var_data)
            user.save()
            return redirect("quartos")
        else:
            return redirect("reserva")
    else:
        form = FormReserva()

    context.update({"form": form})
    return render(request, "reserva.html", context)



def cadastro(request):
    context = {}
    dados_hotel = Hotel.objects.all()
    context["dados_hotel"] = dados_hotel

    if request.method == "POST":
        form = FormCadastro(request.POST)
        if form.is_valid():
            var_first_name = form.cleaned_data['first_name']
            var_last_name = form.cleaned_data['last_name']
            var_user = form.cleaned_data['user']
            var_email = form.cleaned_data['email']
            var_password = form.cleaned_data['password']

            user = User.objects.create_user(username=var_user, email=var_email, password=var_password)
            user.first_name = var_first_name
            user.last_name = var_last_name
            user.save()
            return redirect("login")
        else:
            return redirect("cadastro")
    else:
        form = FormCadastro()

    context.update({"form": form})
    return render(request, "cadastro.html", context)



def login(request):
    context = {}
    dados_hotel = Hotel.objects.all()
    context["dados_hotel"] = dados_hotel

    if request.method == "POST":
        form = FormLogin(request.POST)
        if form.is_valid():
            var_user = form.cleaned_data['user']
            var_password = form.cleaned_data['password']

            user = authenticate(username=var_user, password=var_password)

            if user is not None:
                login(request, user)  # Log the user in
                return redirect("quartos")
            else:
                return redirect("login")
    else:
        form = FormLogin()

    context.update({"form": form})
    return render(request, "login.html", context)

