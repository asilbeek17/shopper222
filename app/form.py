from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from app.models import *


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


# class ProductModelForm(ModelForm):
#
#     class Meta:
#         model = Product
#         fields = '__all__'
#         exclude = ()
#
#
# class ContactForm(ModelForm):
#
#     class Meta:
#         model = Contact
#         fields = '__all__'
#         exclude = ()

