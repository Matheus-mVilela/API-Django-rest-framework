# Generated by Django 3.1.7 on 2021-03-18 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20210317_2048'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='pontos_turisticos'),
        ),
    ]
