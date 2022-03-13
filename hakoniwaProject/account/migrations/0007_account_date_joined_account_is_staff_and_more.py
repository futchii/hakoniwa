# Generated by Django 4.0.2 on 2022-02-27 08:19

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_remove_account_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='account',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='account',
            name='name',
            field=models.CharField(max_length=30, unique=True, validators=[django.core.validators.MinLengthValidator(5), django.core.validators.RegexValidator('^[a-zA-Z0-9]*$')]),
        ),
    ]