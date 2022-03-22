# Generated by Django 4.0.3 on 2022-03-21 22:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('riesgos', '0008_alter_comentarios_fecha'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='riesgos',
            name='estado',
        ),
        migrations.RemoveField(
            model_name='riesgos',
            name='fecha_registro_riesgo',
        ),
        migrations.AddField(
            model_name='riesgos',
            name='fecha_estado_riesgo',
            field=models.DateField(null=True, verbose_name='Fecha del estado del Riesgo'),
        ),
        migrations.AddField(
            model_name='riesgos',
            name='fecha_identificacion_riesgo',
            field=models.DateField(null=True, verbose_name='Fecha de Identificación del Riesgo'),
        ),
        migrations.AlterField(
            model_name='comentarios',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 21, 16, 2, 38, 96619), verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='estrategia',
            name='nombre_estrategia',
            field=models.CharField(max_length=200, verbose_name='Estrategia Utilizada'),
        ),
    ]
