# Generated by Django 3.1.7 on 2021-03-17 23:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('atracoes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='atracao',
            old_name='idade_minina',
            new_name='idade_minima',
        ),
    ]