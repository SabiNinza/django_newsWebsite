# Generated by Django 3.0.5 on 2020-04-21 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200422_0115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main',
            name='fb',
            field=models.CharField(default='#', max_length=300),
        ),
        migrations.AlterField(
            model_name='main',
            name='lk',
            field=models.CharField(default='#', max_length=300),
        ),
        migrations.AlterField(
            model_name='main',
            name='mylink',
            field=models.CharField(default='#', max_length=300),
        ),
        migrations.AlterField(
            model_name='main',
            name='site_name',
            field=models.CharField(default='#', max_length=300),
        ),
        migrations.AlterField(
            model_name='main',
            name='tel',
            field=models.CharField(default='#', max_length=10),
        ),
        migrations.AlterField(
            model_name='main',
            name='tw',
            field=models.CharField(default='#', max_length=300),
        ),
        migrations.AlterField(
            model_name='main',
            name='vm',
            field=models.CharField(default='#', max_length=300),
        ),
        migrations.AlterField(
            model_name='main',
            name='yt',
            field=models.CharField(default='#', max_length=300),
        ),
    ]