# Generated by Django 4.1 on 2022-08-11 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='ativo',
            field=models.CharField(choices=[('ativo', 'Ativo'), ('inativo', 'Inativo')], max_length=7),
        ),
    ]