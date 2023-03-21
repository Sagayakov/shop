from django.db import models
from django.core.validators import MinLengthValidator
from django.utils.text import slugify
from django.urls import reverse


# Create your models here.

class MarkModel(models.Model):
    mark = models.CharField(max_length=20, validators=[MinLengthValidator(2)], verbose_name='Марка')
    country = models.CharField(max_length=15, verbose_name='Страна производитель')
    slug = models.SlugField(null=False, db_index=True, unique=True, verbose_name='Ссылка')

    def __str__(self):
        return f'{self.mark}'

    def get_absolute_url(self):
        return reverse('mark_link', kwargs={'mark_slug': self.slug})

    def save(self, *args, **kwargs):
        if self.slug == 'a':
            self.slug = slugify(f"{self.mark}")
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Марка телефона'
        verbose_name_plural = 'Марки телефонов'


class PhoneModel(models.Model):
    mark_p = models.ForeignKey(MarkModel, on_delete=models.PROTECT, verbose_name='Марка')
    model_p = models.CharField(max_length=25, validators=[MinLengthValidator(1)], verbose_name='Модель')
    description = models.TextField(default='', verbose_name='Описание')
    price_p = models.PositiveIntegerField(verbose_name='Стоимость')
    discount_p = models.PositiveIntegerField(null=True, blank=True, verbose_name='Скидка')
    slug = models.SlugField(null=False, db_index=True, unique=True, verbose_name='Ссылка')
    photo = models.ImageField(upload_to='photos/phones', verbose_name='Фото')
    is_public = models.BooleanField(default=True, verbose_name='Публикация')
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.model_p} {self.price_p}'

    def get_absolute_url(self):
        return reverse('phone_link', kwargs={'phone_slug': self.slug})

    def get_disc_price(self):
        return self.price_p - self.discount_p

    def save(self, *args, **kwargs):
        if self.slug == 'a':
            self.slug = slugify(f"{self.mark_p}-{self.model_p}")
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Модель телефона'
        verbose_name_plural = 'Модели телефонов'
        ordering = ['-price_p', 'mark_p', '-model_p']
