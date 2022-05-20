from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib import auth

from .models import *
from django.views.generic import TemplateView
from .models import *
from .forms import *


def index(request):
    return render(request, 'main/index.html', )
    # путь к шаблону - как будто я уже в папке templates


def about(request):
    abouts = About.objects.order_by('-id').all()
    return render(request, 'main/about.html', {'title': 'Страница о нас', 'abouts': abouts})


def actions(request):
    action = Actions.objects.all()
    return render(request, 'main/actions.html', {'title': 'акции и предложения', 'action': action})


def pizza(request):
    pizzas = Food.objects.order_by('-id').filter(cat_id=1)
    return render(request, 'main/pizza.html', {'title': 'Страница с пиццой', 'pizzas': pizzas})


def rolls(request):
    rolls1 = Food.objects.order_by('-id').filter(cat_id=2)
    return render(request, 'main/rolls.html', {'title': 'Страница с роллами', 'rolls1': rolls1})


def sushi(request):
    sushies = Food.objects.order_by('-id').filter(cat_id=3)
    return render(request, 'main/sushi.html', {'title': 'Страница с суши', 'sushies': sushies})


def drinks(request):
    drink = Food.objects.order_by('-id').filter(cat_id=4)
    return render(request, 'main/drinks.html', {'title': 'Страница с напитками', 'drink': drink})


def politika(request):
    return render(request, 'main/politika.html')


def work(request):
    error = ''
    if request.method == 'POST':
        form = WorkForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('work')
        else:
            error = 'Форма была неверной'

    form = WorkForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/work.html', context)


def workspisok(request):
    works = Work.objects.order_by('-id')[:10]
    return render(request, 'main/workspisok.html', {'title': 'Список резюме', 'works': works})


def booktable(request):
    error = ''
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('menu')
        else:
            error = 'Форма была неверной'

    form = BookingForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/booktable.html', context)


def spisokbroni(request):
    bookings = Booking.objects.order_by('-id')[:10]
    return render(request, 'main/spisokbroni.html', {'title': 'Список брони', 'bookings': bookings})


def forum(request):
    forums = Forum.objects.order_by('-id')[:10]
    return render(request, 'main/forum.html', {'title': 'Страница с отзывами', 'forums': forums, 'username': auth.get_user(request).username})


def createforum(request):
    error = ''
    if request.method == 'POST':
        form = ForumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('forum')
        else:
            error = 'error'
    form = ForumForm()
    context = {
        'form': form,
        'error': error,
        'username': auth.get_user(request).username
    }
    return render(request, 'main/createforum.html', context)


def profil(request):
    info = Profile.objects.all()[:1]
    news = New.objects.order_by('-id')
    return render(request, 'main/profil.html', {'title': 'Профиль пользователя', 'news':news, 'info':info})


def new(request):
    error = ''
    if request.method == 'POST':
        form = NewForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('new')
        else:
            error = 'Форма была неверной'

    form = NewForm
    news = Food.objects.all()
    context = {
        'form': form,
        'error': error,
        'news': news
    }
    return render(request, 'main/new.html', context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')




