# Generated by Django 3.0.5 on 2020-05-01 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_auto_20200430_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='avatar',
            field=models.ImageField(default='default.png', upload_to='images/'),
        ),
    ]