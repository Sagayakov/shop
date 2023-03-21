from django import forms
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
