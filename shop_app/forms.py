from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import PhoneModel, MarkModel


class PhoneFrom(forms.ModelForm):
    class Meta:
        model = PhoneModel
        fields = '__all__'
        labels = {
            'mark_p': 'Марка',
            'model_p': 'Модель',
            'price_p': 'Цена',
            'discount_p': 'Скидка'
        }


class MarkForm(forms.ModelForm):
    class Meta:
        model = MarkModel
        fields = '__all__'
        labels = {
            'mark': 'Марка',
            'country': 'Страна'
        }


class RegisterForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput())
    email = forms.EmailField(label='Email', widget=forms.EmailInput())
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        field_order = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput())
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput())
