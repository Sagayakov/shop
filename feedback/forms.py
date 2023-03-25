from django import forms
from captcha.fields import CaptchaField

from .models import FeedbackModel


class FeedbackForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['sex'].empty_label = 'пол'
    captcha = CaptchaField()

    class Meta:
        model = FeedbackModel
        # fields = '__all__'
        fields = ['name', 'surname', 'sex', 'rating', 'feedback', 'photo']
        labels = {
            'name': 'Имя*',
            'surname': 'Фамилия',
            'sex': 'Пол',
            'rating': 'Оценка (1-10)*',
            'feedback': 'Отзыв',
            'photo': 'Фото'
        }

        widgets = {
            'feedback': forms.Textarea(attrs={'cols': 60, 'rows': 10})
        }

        error_messages = {
            'rating': {
                'required': 'Поле не может быть пустым',
                'max_value': 'Введите число от 0 до 10'
            }
        }
