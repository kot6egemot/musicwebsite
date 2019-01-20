from django import forms
from django.contrib.auth.models import User




class RegForm(forms.Form):
    login = forms.CharField(label='Login')
    password = forms.CharField(label='Password',widget=forms.PasswordInput)


"""
    def clean_login(self):
        data = self.cleaned_data['login']
        return data


"""


