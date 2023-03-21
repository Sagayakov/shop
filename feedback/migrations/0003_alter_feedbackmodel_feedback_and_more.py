# Generated by Django 4.1.7 on 2023-03-19 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0002_alter_feedbackmodel_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedbackmodel',
            name='feedback',
            field=models.TextField(blank=True, null=True, verbose_name='Отзыв'),
        ),
        migrations.AlterField(
            model_name='feedbackmodel',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photos/feedback', verbose_name='Фото'),
        ),
    ]
