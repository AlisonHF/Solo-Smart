# Generated by Django 5.1.1 on 2024-09-07 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_fazenda', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dados',
            name='ph',
            field=models.FloatField(max_length=255),
        ),
        migrations.AlterField(
            model_name='dados',
            name='umidade',
            field=models.FloatField(max_length=255),
        ),
    ]