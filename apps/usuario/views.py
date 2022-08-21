from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from apps.usuario.forms import RegistroForm


# Create your views here.

class RegistroUsuario(CreateView):
    model = User
    template_name = "usuario/registrar.html"
    print('llego')
    
    #form_class = UserCreationForm
    form_class = RegistroForm
    print('pasa')
    success_url = reverse_lazy('mascota:mascota_listar')
    print('sigue')
