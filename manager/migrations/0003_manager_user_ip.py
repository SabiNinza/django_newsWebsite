# Generated by Django 3.0.5 on 2020-04-27 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_auto_20200425_1416'),
    ]

    operations = [
        migrations.AddField(
            model_name='manager',
            name='user_ip',
            field=models.CharField(default=' ', max_length=15),
        ),
    ]
