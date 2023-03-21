# Generated by Django 4.1.7 on 2023-03-19 10:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0002_alter_markmodel_options_alter_phonemodel_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='markmodel',
            name='slug',
            field=models.SlugField(default='', verbose_name='Ссылка'),
        ),
        migrations.AlterField(
            model_name='markmodel',
            name='country',
            field=models.CharField(max_length=15, verbose_name='Страна производитель'),
        ),
        migrations.AlterField(
            model_name='markmodel',
            name='mark',
            field=models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(2)], verbose_name='Марка'),
        ),
    ]
