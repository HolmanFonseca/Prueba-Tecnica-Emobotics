# -*- coding: utf-8 -*-

from django import forms
 
# creating a form
class InputForm(forms.Form):
 
    username= forms.CharField(max_length = 200)
    
   