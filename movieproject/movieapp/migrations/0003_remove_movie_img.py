# Generated by Django 4.2.3 on 2023-07-18 11:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0002_movie_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='img',
        ),
    ]
