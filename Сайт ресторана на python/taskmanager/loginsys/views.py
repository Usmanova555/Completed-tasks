from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.template.context_processors import csrf


def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('menu')
        else:
            args['login_error'] = "User is not found"
    return render(request, 'login.html', args)


def logout(request):
    auth.logout(request)
    return redirect("login")


def register(request):
    args = {}
    args.update(csrf(request))
    args['form'] = UserCreationForm()
    if request.POST:
        newuser_form = UserCreationForm(request.POST)
        if newuser_form.is_valid():
            newuser_form.save()
            newuser = auth.authenticate(username=newuser_form.cleaned_data['username'], password=newuser_form.cleaned_data['password2'])
            auth.login(request, newuser)
            return redirect('menu')
        else:
            args['form'] = newuser_form
    return render(request, 'register.html', {"form": args['form']})
