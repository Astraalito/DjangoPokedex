# Generated by Django 2.2.9 on 2020-02-08 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokeApp', '0003_auto_20200131_1040'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pokemon',
            old_name='type',
            new_name='pokeType',
        ),
    ]
