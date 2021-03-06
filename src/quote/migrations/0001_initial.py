# Generated by Django 2.1.4 on 2018-12-28 07:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=11, validators=[django.core.validators.RegexValidator(code='nomatch', message='Please check the phone number', regex='^.{11}$')])),
                ('email', models.EmailField(max_length=254)),
                ('passengers', models.IntegerField()),
                ('pickup', models.CharField(max_length=50)),
                ('dropoff', models.CharField(max_length=50)),
                ('quote_date', models.DateField()),
                ('quote_time', models.TimeField()),
                ('notes', models.TextField()),
            ],
        ),
    ]
