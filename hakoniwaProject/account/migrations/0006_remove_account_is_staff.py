# Generated by Django 4.0.1 on 2022-02-03 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_account_is_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='is_staff',
        ),
    ]
