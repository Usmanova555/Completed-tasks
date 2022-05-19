from .models import Recipes
from django.forms import ModelForm, TextInput, Textarea
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


class RecipeForm(ModelForm):
    username = forms.CharField(widget = forms.TextInput(attrs={
    "class":"input",
    "type":"text",
    }), label = "Логин")

    password = forms.CharField(widget = forms.TextInput(attrs={
    "class":"input",
    "type":"password",
    }), label = "Пароль")

    class Meta:
        model = Recipes
        fields = ["name", "text", "photo", "time", "complexity", "ingredients", "video"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'название'
            }),
            "text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'текст'
            }),

        }

class AuthUserForm(AuthenticationForm, forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')

class RegisterUserForm(forms.ModelForm):
    username = forms.CharField(widget = forms.TextInput(attrs={
    "class":"input",
    "type":"text",
    }), label = "Логин")

    password = forms.CharField(widget = forms.TextInput(attrs={
    "class":"input",
    "type":"password",
    }), label = "Пароль")

    email = forms.CharField(widget = forms.TextInput(attrs={
    "class":"input",
    "type":"email",
    }), label = "Почта")

    class Meta:
        model = User
        fields = ('username', 'password', 'email')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for field in self.fields:
    #         self.fields[field].widget.attrs['class'] = 'form-control'
