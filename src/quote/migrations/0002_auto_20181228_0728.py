# Generated by Django 2.1.4 on 2018-12-28 07:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='notes',
            field=models.TextField(max_length=250),
        ),
        migrations.AlterField(
            model_name='quote',
            name='passengers',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(8)]),
        ),
    ]
