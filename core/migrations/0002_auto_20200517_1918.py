# Generated by Django 3.0.6 on 2020-05-17 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forminformation',
            name='planilha',
        ),
        migrations.AddField(
            model_name='forminformation',
            name='plan',
            field=models.FileField(blank=True, upload_to='planilhas', verbose_name='Filecsv'),
        ),
    ]
