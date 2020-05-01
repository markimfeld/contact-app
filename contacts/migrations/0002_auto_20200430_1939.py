# Generated by Django 3.0.5 on 2020-04-30 19:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='address',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='contact',
            name='avatar',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='contact',
            name='city',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='contact',
            name='company_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='contact',
            name='country',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='contact',
            name='created',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='job',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='contact',
            name='website',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]