from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput

from .models import *


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class FieldForm(ModelForm):
    class Meta:
        model = FieldName
        fields = ['name']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите номер столбца сущности'
            })
        }


class ColumnsForm(ModelForm):
    class Meta:
        model = ColumnsCount
        fields = ['count']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите количество столбцов'
            })
        }