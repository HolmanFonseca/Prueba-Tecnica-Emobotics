# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistroForm(UserCreationForm):
    class Meta:
        model=User
        fields=["first_name","last_name","username","email"]
        labels={
            "first_name":"Nombre",
            "last_name":"Apellido",
            "username":"Nombre de usuario",
            "email":"Correo"}
        