# Generated by Django 2.2.9 on 2020-01-18 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokeApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='type',
            field=models.CharField(max_length=20),
        ),
    ]
