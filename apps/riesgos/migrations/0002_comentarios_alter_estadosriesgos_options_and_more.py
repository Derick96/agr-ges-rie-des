# Generated by Django 4.0.3 on 2022-03-15 15:32

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('usuario', '0003_roles_remove_usuario_isadmin_usuario_usuarios_roles'),
        ('riesgos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.TextField(verbose_name='Comentarios')),
                ('fecha', models.DateTimeField(default=datetime.datetime(2022, 3, 15, 9, 32, 35, 545992), verbose_name='Fecha')),
            ],
        ),
        migrations.AlterModelOptions(
            name='estadosriesgos',
            options={'verbose_name': 'Estado Riesgo', 'verbose_name_plural': 'Estados Riesgos'},
        ),
        migrations.AddField(
            model_name='riesgos',
            name='estado',
            field=models.CharField(max_length=20, null=True, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='estadosriesgos',
            name='estado',
            field=models.CharField(max_length=50, verbose_name='Estado del Riesgo'),
        ),
        migrations.RemoveField(
            model_name='riesgos',
            name='comentario',
        ),
        migrations.AddField(
            model_name='riesgos',
            name='comentario',
            field=models.ManyToManyField(blank=True, through='riesgos.Comentarios', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comentarios',
            name='riesgos',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='riesgos.riesgos'),
        ),
        migrations.AddField(
            model_name='comentarios',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
