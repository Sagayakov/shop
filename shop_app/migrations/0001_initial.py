# Generated by Django 4.1.7 on 2023-03-18 13:13

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MarkModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(2)])),
                ('country', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='PhoneModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_p', models.CharField(max_length=25, validators=[django.core.validators.MinLengthValidator(1)])),
                ('price_p', models.PositiveIntegerField()),
                ('discount_p', models.PositiveIntegerField(blank=True, null=True)),
                ('slug', models.SlugField(default='')),
                ('photo', models.ImageField(upload_to='photos/phones')),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('mark_p', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shop_app.markmodel')),
            ],
        ),
    ]
