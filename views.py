from . import forms
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render


def login_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(settings.NODE_URL)

    elif request.POST:
        form = forms.UserLoginForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data

            user = authenticate(username=cleaned_data.get('username'), password=cleaned_data.get('password'))
            if (user is not None) and user.is_active:
                login(request, user)

                response = HttpResponseRedirect(settings.NODE_URL)
                response.set_cookie('username', user.username)
                return response
            else:
                messages.error(request, 'Invalid auth data :(')
        else:
            messages.error(request, 'Sorry, but you can\'t use this credentials :(')

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    response = HttpResponseRedirect(settings.LOGOUT_REDIRECT_URL)
    response.delete_cookie('username')
    return response


def register_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(settings.NODE_URL)
    elif request.POST:
        form = forms.UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()

            login(request, user)
            return HttpResponseRedirect(settings.NODE_URL)
        else:
            messages.error(request, form.errors)

    return render(request, 'register.html')
