from django.db import models
from django.core.validators import MinLengthValidator, MaxValueValidator


# from django.core.exceptions import ValidationError


class FeedbackModel(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDERS = [
        (MALE, "Мужской"),
        (FEMALE, "Женский")
    ]

    name = models.CharField(max_length=25, validators=[MinLengthValidator(2)], verbose_name='Имя')
    surname = models.CharField(max_length=35, null=True, blank=True, verbose_name='Фамилия')
    sex = models.CharField(max_length=1, choices=GENDERS, null=True, blank=True, verbose_name='Пол')
    rating = models.PositiveIntegerField(validators=[MaxValueValidator(10)], verbose_name='Рэйтинг')
    feedback = models.TextField(verbose_name='Отзыв', null=True, blank=True)
    photo = models.ImageField(upload_to='photos/feedback', verbose_name='Фото', null=True, blank=True)
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} {self.rating}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['-rating', 'name']

    # def clean_feedback(self):
    #     feedback = self.cleaned_data['feedback']
    #     if len(feedback) > 1000:
    #         raise ValidationError('Длина не может превышать 1000')
    #
    #     return feedback
