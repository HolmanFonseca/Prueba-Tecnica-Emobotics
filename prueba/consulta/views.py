from django.shortcuts import render
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy,reverse
from django.http import HttpResponse
from django import forms




from consulta.forms import InputForm
 
# Create your views here.
def consultar_usuario(request):
    context ={}
    context['form']= InputForm()
    if request.GET:
        userstring = request.GET['username']

        user_filter=User.objects.filter(username=userstring).values()
        if user_filter.exists():
            return HttpResponse(user_filter)
        else:
            return HttpResponse("No Existe usuario con ese username") 

    return render(request, "home.html", context)





   


