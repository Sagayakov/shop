# Generated by Django 4.1.7 on 2023-03-19 07:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feedbackmodel',
            options={'ordering': ['-rating', 'name'], 'verbose_name': 'Отзыв', 'verbose_name_plural': 'Отзывы'},
        ),
        migrations.AlterField(
            model_name='feedbackmodel',
            name='feedback',
            field=models.TextField(verbose_name='Отзыв'),
        ),
        migrations.AlterField(
            model_name='feedbackmodel',
            name='name',
            field=models.CharField(max_length=25, validators=[django.core.validators.MinLengthValidator(2)], verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='feedbackmodel',
            name='photo',
            field=models.ImageField(upload_to='photos/feedback', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='feedbackmodel',
            name='rating',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(10)], verbose_name='Рэйтинг'),
        ),
        migrations.AlterField(
            model_name='feedbackmodel',
            name='sex',
            field=models.CharField(blank=True, choices=[('M', 'Мужской'), ('F', 'Женский')], max_length=1, null=True, verbose_name='Пол'),
        ),
        migrations.AlterField(
            model_name='feedbackmodel',
            name='surname',
            field=models.CharField(blank=True, max_length=35, null=True, verbose_name='Фамилия'),
        ),
    ]
