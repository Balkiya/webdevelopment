from django import forms

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=100, label='Логин немесе номер')
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')
