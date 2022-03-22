from .models import Riesgos
from rest_framework import serializers

class RiesgoSerializer(serializers.ModelSerializer):
    impacto_display = serializers.CharField(source = "get_impacto_display")
    probabilidad_display = serializers.CharField(source = "get_probabilidad_ocurrencia_display")

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
