# Generated by Django 3.0.6 on 2020-05-06 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0011_auto_20200503_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='avatar',
            field=models.ImageField(default='contacts/images/default.png', upload_to='images/'),
        ),
    ]
