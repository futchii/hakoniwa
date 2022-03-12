# Generated by Django 4.0.2 on 2022-02-26 08:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('heiwa', '0005_alter_islands_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='islands',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True),
        ),
    ]
