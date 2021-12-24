# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 05:13:16 2021

@author: linal
"""


from django.conf.urls import url
from usuario.views import RegistrarUsuario

urlpatterns=[
     url(r'^registrar/', RegistrarUsuario.as_view(),name="registrar$"),
]