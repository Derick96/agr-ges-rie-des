# Generated by Django 4.0.3 on 2022-03-21 17:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('riesgos', '0007_alter_comentarios_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentarios',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 21, 11, 2, 9, 347967), verbose_name='Fecha'),
        ),
    ]