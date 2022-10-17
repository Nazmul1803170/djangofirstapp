from xml.etree.ElementInclude import include
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import forms
from django import forms

class SignupForm(UserCreationForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}))
    contact = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'input'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input'}))

    

      
