# Generated by Django 3.0.5 on 2020-04-21 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_main_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='main',
            name='fb',
            field=models.TextField(default='#'),
        ),
        migrations.AddField(
            model_name='main',
            name='lk',
            field=models.TextField(default='#'),
        ),
        migrations.AddField(
            model_name='main',
            name='tw',
            field=models.TextField(default='#'),
        ),
        migrations.AddField(
            model_name='main',
            name='vm',
            field=models.TextField(default='#'),
        ),
        migrations.AddField(
            model_name='main',
            name='yt',
            field=models.TextField(default='#'),
        ),
    ]
