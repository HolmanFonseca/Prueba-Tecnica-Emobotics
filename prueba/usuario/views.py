from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy,reverse
from usuario.forms import RegistroForm

class RegistrarUsuario(CreateView):
    ## Crear modelo 
    model=User
    
    ## Llamar plantilla registrar
    template_name="registrar.html"

    ## Crear formulario con los campos que se requieren
    form_class=RegistroForm
    ## Redirigir a la página
    success_url=reverse_lazy('respuesta_exitosa')

class ConsultarUsuario(CreateView):
    ## Crear modelo 
    def register_user(self,request):
        r_username= request.GET['username']
        
        if User.objects.filter(username=r_username).exists():
            
            return reverse_lazy('respuesta_exitosa')
 

