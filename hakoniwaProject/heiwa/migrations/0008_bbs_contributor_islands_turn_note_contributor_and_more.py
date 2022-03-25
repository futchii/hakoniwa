# Generated by Django 4.0.3 on 2022-03-25 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('heiwa', '0007_rename_population_islands_factory_worker_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bbs',
            name='contributor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='heiwa.islands'),
        ),
        migrations.AddField(
            model_name='islands',
            name='turn',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='note',
            name='contributor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='heiwa.islands'),
        ),
        migrations.CreateModel(
            name='Note_content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('contributor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='heiwa.note')),
            ],
        ),
        migrations.CreateModel(
            name='Bbs_content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('contributor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='heiwa.bbs')),
            ],
        ),
    ]