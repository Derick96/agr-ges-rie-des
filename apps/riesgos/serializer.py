from .models import KRI, Categorias, Comentarios, EstadosRiesgos, Estrategia, FuenteRiesgos, MagnitudImpacto, Propietario, Riesgos, Servicios, Tipos_KRI
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

class EstadosRiesgosSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadosRiesgos
        fields = ['estado']

class EstrategiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estrategia
        fields = ['nombre_estrategia']

class TipoKriSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipos_KRI
        fields = ['nombre_tipo']

class KriSerializer(serializers.ModelSerializer):
    tipos_kri = TipoKriSerializer()

    class Meta:
        model = KRI
        fields = ('descripcion_kri', 'tipos_kri')

class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentarios
        fields = '__all__'


class RiesgoSerializer(serializers.ModelSerializer):
    impacto_display = serializers.CharField(source = "get_impacto_display")
    probabilidad_display = serializers.CharField(source = "get_probabilidad_ocurrencia_display")
    propietario = PropietarioSerializer()
    categorias = CategoriasSerializer()
    fuente_riesgo = FuenteRiesgosSerializer()
    # riesgos_servicios = ServiciosSerializer()
    magnitud_impacto = MagnitudImpactoSerializer()
    estados_riesgos = EstadosRiesgosSerializer()
    estrategia = EstrategiaSerializer()
    # comentario = ComentarioSerializer()
    kri = KriSerializer()

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
