# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 05:13:16 2021

@author: linal
"""


from django.conf.urls import url

from consulta.views import consultar_usuario

urlpatterns=[
    
     url(r'^usuario/',consultar_usuario,name="consultar"),
]