# Generated by Django 4.1.7 on 2023-03-19 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0004_phonemodel_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phonemodel',
            name='slug',
            field=models.SlugField(default='', unique=True, verbose_name='Ссылка'),
        ),
    ]
