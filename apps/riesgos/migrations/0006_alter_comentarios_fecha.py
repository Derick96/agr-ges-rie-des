# Generated by Django 4.0.3 on 2022-03-16 20:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('riesgos', '0005_alter_comentarios_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentarios',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 16, 14, 49, 37, 442526), verbose_name='Fecha'),
        ),
    ]
