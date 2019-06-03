# Generated by Django 2.1.4 on 2019-01-14 15:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0004_auto_20190114_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='phone',
            field=models.CharField(max_length=11, validators=[django.core.validators.RegexValidator(code='nomatch', message='Please use a valid phone number', regex='^.{11}$')]),
        ),
    ]
