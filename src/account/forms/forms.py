from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from account.models import Account, MyAccountManager


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Обязательно.', label='Имя')
    last_name = forms.CharField(max_length=30, required=True, help_text='Обязательно.', label='Фамилия')
    patronymic = forms.CharField(max_length=30, required=True, help_text='Обязательно.', label='Отчество')
    email = forms.EmailField(max_length=254, help_text='Обязательно. Введите валидную почту.')

    class Meta:
        model = Account
        fields = (
            'username',
            'first_name',
            'last_name',
            'patronymic',
            'email',
            'password1',
            'password2',
        )
