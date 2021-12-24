# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 20:42:48 2021

@author: linal
"""

from django.conf.urls import url
from respuesta_exitosa.views import succeful

urlpatterns=[
     url(r'^exitosa/',succeful,name="respuesta_exitosa"),
]
