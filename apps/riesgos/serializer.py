from .models import Categorias, FuenteRiesgos, MagnitudImpacto, Propietario, Riesgos, Servicios
from rest_framework import serializers

# class ServiciosSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Servicios
#         fields = ('nombre','tipos_servicios')

class PropietarioSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Propietario
        fields = ['nombre']

class CategoriasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorias
        fields = ['nombre']

class FuenteRiesgosSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuenteRiesgos
        fields = ['nombre']

class MagnitudImpactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MagnitudImpacto
        fields = ['descripcion']

class RiesgoSerializer(serializers.ModelSerializer):
    impacto_display = serializers.CharField(source = "get_impacto_display")
    probabilidad_display = serializers.CharField(source = "get_probabilidad_ocurrencia_display")
    propietario = PropietarioSerializer()
    categorias = CategoriasSerializer()
    fuente_riesgo = FuenteRiesgosSerializer()
    # riesgos_servicios = ServiciosSerializer()
    magnitud_impacto = MagnitudImpactoSerializer()

    class Meta:
        model = Riesgos
        fields = ('id','riesgo','codigo',
        'fecha_identificacion_riesgo','escenario_riesgo',
        'riesgos_servicios','activos_afectados',
        'propietario',
        'categorias','form_ident_riesgo',
        'fuente_riesgo','impacto_display',
        'probabilidad_display',
        'nivel_riesgo','magnitud_impacto',
        'estados_riesgos','fecha_estado_riesgo',
        'control','estrategia',
        'comentario_local','kri',
        'importancia','comentario')
