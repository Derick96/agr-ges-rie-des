from django.db import models
from apps.usuario.models import Usuario
from datetime import datetime

# Create your models here.
class Propietario(models.Model):
    nombre = models.CharField('Propietario',max_length=200)
    codigo = models.CharField('Codigo de la Vertical', max_length=10)

    class Meta:
        verbose_name = 'Propietario'
        verbose_name_plural = 'Propietarios'

    def __str__(self):
        return self.nombre

class Categorias(models.Model):
    nombre = models.CharField('Categorias',max_length=100)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nombre

class FuenteRiesgos(models.Model):
    nombre = models.CharField('Fuente de Riesgos',max_length=200)

    class Meta:
        verbose_name = 'Fuente de Riesgo'
        verbose_name_plural = 'Fuentes de Riesgos'

    def __str__(self):
        return self.nombre

class MagnitudImpacto(models.Model):
    descripcion = models.TextField('Magnitud de Impacto')

    class Meta:
        verbose_name = 'Magnitud de impacto'
        verbose_name_plural = 'Magnitud de impactos'

    def __str__(self):
        return self.descripcion

class Estrategia(models.Model):
    nombre_estrategia = models.CharField('Estrategia Utilizada',max_length=200)

    class Meta:
        verbose_name = 'Estrategia'
        verbose_name_plural = 'Estrategias'

    def __str__(self):
        return self.nombre_estrategia  

class Tipos_KRI(models.Model):
    nombre_tipo = models.TextField('KRI')

    class Meta:
        verbose_name = 'Tipo de KRI'
        verbose_name_plural = 'Tipos de KRI'

    def __str__(self):
        return self.nombre_tipo

class KRI(models.Model):
    descripcion_kri = models.TextField('KRI')
    tipos_kri = models.ForeignKey(Tipos_KRI,on_delete=models.CASCADE,null=True)

    class Meta:
        verbose_name = 'KRI'
        verbose_name_plural = 'KRI'

    def __str__(self):
        return self.descripcion_kri

class TiposServicios(models.Model):
    nombre = models.CharField('Tipo de Servicios',max_length=60)

    class Meta:
        verbose_name = 'Tipo Servicio'
        verbose_name_plural = 'Tipos de Servicios'

    def __str__(self):
        return self.nombre

class Servicios(models.Model):
    nombre = models.CharField('Servicios',max_length=60)
    tipos_servicios = models.ForeignKey(TiposServicios,on_delete=models.CASCADE,null=True)

    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'

    def __str__(self):
        return self.nombre

class EstadosRiesgos(models.Model):
    estado = models.CharField('Estado del Riesgo',max_length=50, blank = False)

    class Meta:
        verbose_name = 'Estado Riesgo'
        verbose_name_plural = 'Estados Riesgos'

    def __str__(self):
        return self.estado

class Riesgos(models.Model):

    IMPACTOS = (
        ('1', 'Insignificante'),
        ('2', 'Menor'),
        ('3', 'Significante'),
        ('4', 'Mayor'),
        ('5', 'Severo')
    )
    PROBABILIDAD_OCURRENCIA = (
        ('1', 'Improbable'),
        ('2', 'Raro'),
        ('3', 'Moderado'),
        ('4', 'Probable'),
        ('5', 'Casi Cierto')
    )
    auto_increment_id = models.AutoField(primary_key=True)
    riesgo = models.CharField('Riesgo',max_length=200, blank = False)
    fecha_identificacion_riesgo = models.DateField('Fecha de Identificación del Riesgo',null = True, blank = False)
    escenario_riesgo = models.CharField('Escenario Riesgo',max_length=350, blank = False)
    riesgos_servicios = models.ManyToManyField(Servicios,blank=True,null=True)
    activos_afectados = models.CharField('Activos Afectados',max_length=100, blank = True)
    propietario = models.ForeignKey(Propietario,on_delete=models.CASCADE, null=True)
    categorias = models.ForeignKey(Categorias,on_delete=models.CASCADE, null=True)
    form_ident_riesgo = models.CharField('Forma de Identificación del Riesgo',max_length=15,blank = False)
    fuente_riesgo = models.ForeignKey(FuenteRiesgos,on_delete=models.CASCADE,null=True)
    impacto = models.CharField('Impacto',max_length=50, blank = False,choices=IMPACTOS)
    probabilidad_ocurrencia = models.CharField('Probabilidad Ocurrencia',max_length=50, blank = False,choices=PROBABILIDAD_OCURRENCIA)
    magnitud_impacto = models.ForeignKey(MagnitudImpacto,on_delete=models.CASCADE,null=True)
    estados_riesgos = models.ForeignKey(EstadosRiesgos,on_delete=models.CASCADE,null=True)
    fecha_estado_riesgo = models.DateField('Fecha del estado del Riesgo',blank = False, null=True)
    control = models.TextField('Control', blank = True)
    estrategia = models.ForeignKey(Estrategia,on_delete=models.CASCADE,null=True)
    comentario_local= models.TextField('Comentario', blank = True)
    kri = models.ForeignKey(KRI,on_delete=models.CASCADE,null=True)
    importancia = models.TextField('Importancia', blank = True)
    comentario = models.ManyToManyField(Usuario,blank=True,through='Comentarios')


    @property
    def nivel_riesgo(self):
        
        if self.impacto == "1" and self.probabilidad_ocurrencia == "4"\
             or self.impacto == "1" and self.probabilidad_ocurrencia == "3"\
             or self.impacto == "1" and self.probabilidad_ocurrencia == "2"\
             or self.impacto == "2" and self.probabilidad_ocurrencia == "2"\
             or self.impacto == "2" and self.probabilidad_ocurrencia == "1"\
             or self.impacto == "3" and self.probabilidad_ocurrencia == "1"\
             or self.impacto == "4" and self.probabilidad_ocurrencia == "1":
            return "Aceptable"
        elif self.impacto == "1" and self.probabilidad_ocurrencia == "1":
                return "Oportunidad"
        elif self.impacto == "3" and self.probabilidad_ocurrencia == "5"\
            or self.impacto == "3" and self.probabilidad_ocurrencia == "4"\
            or self.impacto == "4" and self.probabilidad_ocurrencia == "5"\
            or self.impacto == "4" and self.probabilidad_ocurrencia == "4"\
            or self.impacto == "4" and self.probabilidad_ocurrencia == "3"\
            or self.impacto == "5" and self.probabilidad_ocurrencia == "5"\
            or self.impacto == "5" and self.probabilidad_ocurrencia == "4"\
            or self.impacto == "5" and self.probabilidad_ocurrencia == "3":
                return "Inaceptable (Acción inmediata)"
        else:
            return "Inaceptable"
    
    @property
    def codigo(self):
        return self.propietario.codigo + str(self.auto_increment_id)

    class Meta:
        verbose_name = 'Riesgo'
        verbose_name_plural = 'Riesgos'
        unique_together = (('propietario', 'auto_increment_id'),)

    def __str__(self):
        return self.riesgo
    

class Comentarios(models.Model):
    comentario = models.TextField('Comentarios')
    fecha = models.DateTimeField('Fecha',default=datetime.now())
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE, null=True)
    riesgos = models.ForeignKey(Riesgos,on_delete=models.CASCADE,null=True)

    class Meta:
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'

    def __str__(self):
        return self.comentario

# class Incidentes(models.Model):
#     fecha_registro_incidente = models.DateField('Fecha de Registro del Incidente',null = True, blank = False)
#     riesgos = models.ForeignKey(Riesgos,on_delete=models.CASCADE,null=True)

#     class Meta:
#         verbose_name = 'Incidente'
#         verbose_name_plural = 'Incidentes'

#     def __str__(self):
#         return self.fecha_registro_incidente