# Generated by Django 3.0.5 on 2020-05-01 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0005_auto_20200501_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='avatar',
            field=models.ImageField(default='images/default.png', upload_to='images/'),
        ),
    ]
