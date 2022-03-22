# Generated by Django 4.0.3 on 2022-03-15 17:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('riesgos', '0003_remove_riesgos_nivel_riesgo_alter_comentarios_fecha_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comentarios',
            options={'verbose_name': 'Comentario', 'verbose_name_plural': 'Comentarios'},
        ),
        migrations.AddField(
            model_name='riesgos',
            name='comentario_local',
            field=models.TextField(blank=True, verbose_name='Comentario'),
        ),
        migrations.AlterField(
            model_name='comentarios',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 15, 11, 44, 7, 201062), verbose_name='Fecha'),
        ),
    ]