# Generated by Django 4.1 on 2022-09-17 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0005_remove_consulta_cpf_consulta_paciente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulta',
            name='paciente',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='paciente.paciente'),
        ),
    ]
