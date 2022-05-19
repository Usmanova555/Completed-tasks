from django.shortcuts import render, redirect
from .models import Recipes
from .forms import RecipeForm
from django.contrib import auth
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from .forms import AuthUserForm, RegisterUserForm
from django.views.generic import CreateView


# main page with all recipes
def main(request):
    recipe = Recipes.objects.order_by('-id')
    return render(request, 'main.html', {'recipes': recipe})


# page add recipe
def add(request):
    error = ''
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'неверно введены данные'

    return render(request, 'add.html', {'error': error})


# page show recipe
def recipe(request):
    # method for get need recipe
    form = RecipeForm()
    return redirect(request, 'main/recipe.html', {'recipe': form})


class RegisterUser(CreateView):
    model = User
    template_name = 'register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('login')
    success_msg = 'Пользователь успешно создан.'

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class LoginUser(LoginView):
    template_name = 'login.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('home')
    def get_success_url(self):
        return self.success_url


def search(request):
    return render(request, 'main/templates/search.html')


def profile(request):
    return render(request, 'main/templates/profile.html')
