# Generated by Django 4.1.7 on 2023-03-19 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0006_alter_phonemodel_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='markmodel',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='Ссылка'),
        ),
    ]
