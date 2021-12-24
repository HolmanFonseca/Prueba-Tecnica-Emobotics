from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy,reverse
from usuario.forms import RegistroForm

   


def succeful(request):
    documento="""<html>
    <body>
    <h1>
    El usuario se ha creado con éxito!
    </h1>
    <form action="/usuario/registrar">
        <button id="stat-btn" class="btn"> Crear otro usuario </button>
    </form>
    </body>
    </html>
    """
    return HttpResponse(documento)