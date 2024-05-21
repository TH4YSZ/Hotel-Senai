from django import forms

TIPOS_QUARTOS = (
    ("SOLTEIRO", "Solteiro"),
    ("CASAL", "Casal"),
    ("CONFORTO", "Conforto"),
    ("LUXO", "Luxo")
)

class FormReserva(forms.Form):
    nome = forms.CharField(label="Nome", max_length=20)
    sobrenome = forms.CharField(label="Sobrenome", max_length=20)
    email = forms.CharField(label="Email", max_length=50)
    idade = forms.CharField(label="Idade", max_length=3)
    end = forms.CharField(label="Endereço", max_length=100)
    quarto = forms.ChoiceField(label="Tipo de Quarto", choices=TIPOS_QUARTOS)
    data = forms.CharField(label="Data", max_length=8)

class FormCadastro(forms.Form):
    first_name = forms.CharField(label="Nome", max_length=20)
    last_name = forms.CharField(label="Sobrenome", max_length=20)
    user = forms.CharField(label="Usuário", max_length=20)
    email = forms.EmailField(label="Email", max_length=100)
    password = forms.CharField(label="Senha", widget=forms.PasswordInput)

class FormLogin(forms.Form):
    user = forms.CharField(label="Usuário", max_length=20)
    password = forms.CharField(label="Senha", widget=forms.PasswordInput)