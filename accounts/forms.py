from . import models
from django import forms
from django.contrib.auth.forms import UserCreationForm


class UserLoginForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={}))

    class Meta:
        model = models.User
        fields = [
            'username',
            'password',
        ]


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = models.User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]
