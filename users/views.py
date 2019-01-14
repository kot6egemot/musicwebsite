from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import RegForm

from django.contrib.auth import logout
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

def login_view(request):
    if request.method != 'POST':
        form = RegForm(initial={'login':'admin', 'password':'admin'})
    else:
        form = RegForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['login']
            password = form.cleaned_data['password']
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
        return HttpResponseRedirect(reverse('music:index'))
    context = {'form' : form}
    return render(request, 'users/login.html', context)


def register_view(request):
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            authenticated_user = authenticate(username = new_user.username,
                                               password = request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('music:index'))
    return render(request, 'users\egister.html', {'form' : form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('music:index'))
