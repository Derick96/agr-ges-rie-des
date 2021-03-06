# Generated by Django 4.0.3 on 2022-04-07 18:24

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('usuario', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Categorias')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Comentarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.TextField(verbose_name='Comentarios')),
                ('fecha', models.DateTimeField(default=datetime.datetime(2022, 4, 7, 12, 24, 3, 205982), verbose_name='Fecha')),
            ],
            options={
                'verbose_name': 'Comentario',
                'verbose_name_plural': 'Comentarios',
            },
        ),
        migrations.CreateModel(
            name='EstadosRiesgos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=50, verbose_name='Estado del Riesgo')),
            ],
            options={
                'verbose_name': 'Estado Riesgo',
                'verbose_name_plural': 'Estados Riesgos',
            },
        ),
        migrations.CreateModel(
            name='Estrategia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_estrategia', models.CharField(max_length=200, verbose_name='Estrategia Utilizada')),
            ],
            options={
                'verbose_name': 'Estrategia',
                'verbose_name_plural': 'Estrategias',
            },
        ),
        migrations.CreateModel(
            name='FuenteRiesgos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, verbose_name='Fuente de Riesgos')),
            ],
            options={
                'verbose_name': 'Fuente de Riesgo',
                'verbose_name_plural': 'Fuentes de Riesgos',
            },
        ),
        migrations.CreateModel(
            name='KRI',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion_kri', models.TextField(verbose_name='KRI')),
            ],
            options={
                'verbose_name': 'KRI',
                'verbose_name_plural': 'KRI',
            },
        ),
        migrations.CreateModel(
            name='MagnitudImpacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(verbose_name='Magnitud de Impacto')),
            ],
            options={
                'verbose_name': 'Magnitud de impacto',
                'verbose_name_plural': 'Magnitud de impactos',
            },
        ),
        migrations.CreateModel(
            name='Propietario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, verbose_name='Propietario')),
                ('codigo', models.CharField(max_length=10, verbose_name='Codigo de la Vertical')),
            ],
            options={
                'verbose_name': 'Propietario',
                'verbose_name_plural': 'Propietarios',
            },
        ),
        migrations.CreateModel(
            name='Tipos_KRI',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_tipo', models.TextField(verbose_name='KRI')),
            ],
            options={
                'verbose_name': 'Tipo de KRI',
                'verbose_name_plural': 'Tipos de KRI',
            },
        ),
        migrations.CreateModel(
            name='TiposServicios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60, verbose_name='Tipo de Servicios')),
            ],
            options={
                'verbose_name': 'Tipo Servicio',
                'verbose_name_plural': 'Tipos de Servicios',
            },
        ),
        migrations.CreateModel(
            name='Servicios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60, verbose_name='Servicios')),
                ('tipos_servicios', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='riesgos.tiposservicios')),
            ],
            options={
                'verbose_name': 'Servicio',
                'verbose_name_plural': 'Servicios',
            },
        ),
        migrations.CreateModel(
            name='Riesgos',
            fields=[
                ('auto_increment_id', models.AutoField(primary_key=True, serialize=False)),
                ('riesgo', models.CharField(max_length=200, verbose_name='Riesgo')),
                ('fecha_identificacion_riesgo', models.DateField(null=True, verbose_name='Fecha de Identificaci??n del Riesgo')),
                ('escenario_riesgo', models.CharField(max_length=350, verbose_name='Escenario Riesgo')),
                ('activos_afectados', models.CharField(blank=True, max_length=100, verbose_name='Activos Afectados')),
                ('form_ident_riesgo', models.CharField(max_length=15, verbose_name='Forma de Identificaci??n del Riesgo')),
                ('impacto', models.CharField(choices=[('1', 'Insignificante'), ('2', 'Menor'), ('3', 'Significante'), ('4', 'Mayor'), ('5', 'Severo')], max_length=50, verbose_name='Impacto')),
                ('probabilidad_ocurrencia', models.CharField(choices=[('1', 'Improbable'), ('2', 'Raro'), ('3', 'Moderado'), ('4', 'Probable'), ('5', 'Casi Cierto')], max_length=50, verbose_name='Probabilidad Ocurrencia')),
                ('fecha_estado_riesgo', models.DateField(null=True, verbose_name='Fecha del estado del Riesgo')),
                ('control', models.TextField(blank=True, verbose_name='Control')),
                ('comentario_local', models.TextField(blank=True, verbose_name='Comentario')),
                ('importancia', models.TextField(blank=True, verbose_name='Importancia')),
                ('categorias', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='riesgos.categorias')),
                ('comentario', models.ManyToManyField(blank=True, through='riesgos.Comentarios', to=settings.AUTH_USER_MODEL)),
                ('estados_riesgos', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='riesgos.estadosriesgos')),
                ('estrategia', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='riesgos.estrategia')),
                ('fuente_riesgo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='riesgos.fuenteriesgos')),
                ('kri', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='riesgos.kri')),
                ('magnitud_impacto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='riesgos.magnitudimpacto')),
                ('propietario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='riesgos.propietario')),
                ('riesgos_servicios', models.ManyToManyField(blank=True, null=True, to='riesgos.servicios')),
            ],
            options={
                'verbose_name': 'Riesgo',
                'verbose_name_plural': 'Riesgos',
                'unique_together': {('propietario', 'auto_increment_id')},
            },
        ),
        migrations.AddField(
            model_name='kri',
            name='tipos_kri',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='riesgos.tipos_kri'),
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
