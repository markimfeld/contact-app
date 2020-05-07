# Generated by Django 3.0.5 on 2020-05-07 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0017_auto_20200506_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='category',
            field=models.CharField(choices=[('FR', 'Friend'), ('FY', 'Family'), ('CO', 'Coworker'), ('OR', 'Other')], default='Choose..', max_length=2),
        ),
    ]
