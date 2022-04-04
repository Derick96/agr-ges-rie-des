from apps.usuario.models import Usuario
from apps.usuario.serializer import UsuarioSerializer
from .models import KRI, Categorias, Comentarios, EstadosRiesgos, Estrategia, FuenteRiesgos, MagnitudImpacto, Propietario, Riesgos, Servicios, Tipos_KRI, TiposServicios
from rest_framework import serializers


class tipoServiciosSerializer(serializers.ModelSerializer):
    class Meta:
        model = TiposServicios
        fields = '__all__'

#Serializador para anidados
class tiposServiciosSerializer(serializers.ModelSerializer):
    nombre = serializers.CharField(required = False)
    class Meta:
        model = TiposServicios
        fields = '__all__'

class ServiciosSerializer(serializers.ModelSerializer):
    tipos_servicios = tipoServiciosSerializer()

    class Meta:
        model = Servicios
        fields = '__all__'

#Serializador para anidados
class ServiciosSerializers(serializers.ModelSerializer):
    nombre = serializers.CharField(required = False)
    tipos_servicios = tiposServiciosSerializer(required = False)

    class Meta:
        model = Servicios
        fields = '__all__'

class PropietarioSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Propietario
        fields = '__all__'

# serializador para anidados
class PropietariosSerializer(serializers.ModelSerializer):
    nombre = serializers.CharField(required = False)
    class Meta:
        model = Propietario
        fields = '__all__'


class CategoriasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorias
        fields = '__all__'

# serializador para anidados
class CategoriasSerializers(serializers.ModelSerializer):
    nombre = serializers.CharField(required = False)
    class Meta:
        model = Categorias
        fields = '__all__'


class FuenteRiesgosSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuenteRiesgos
        fields = '__all__'

# serializador para anidados
class FuentesRiesgosSerializer(serializers.ModelSerializer):
    nombre = serializers.CharField(required = False)
    class Meta:
        model = FuenteRiesgos
        fields = '__all__'


class MagnitudImpactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MagnitudImpacto
        fields = '__all__'

# serializador para anidados
class MagnitudImpactosSerializer(serializers.ModelSerializer):
    descripcion = serializers.CharField(required = False)
    class Meta:
        model = MagnitudImpacto
        fields = '__all__'

class EstadosRiesgosSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadosRiesgos
        fields = '__all__'

# serializador para anidados
class EstadosRiesgosSerializers(serializers.ModelSerializer):
    estado = serializers.CharField(required = False)
    class Meta:
        model = EstadosRiesgos
        fields = '__all__'

class EstrategiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estrategia
        fields = '__all__'

# serializador para anidados
class EstrategiasSerializer(serializers.ModelSerializer):
    nombre_estrategia = serializers.CharField(required = False)
    class Meta:
        model = Estrategia
        fields = '__all__'

class TipoKriSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipos_KRI
        fields = '__all__'

# serializador para anidados
class TiposKriSerializer(serializers.ModelSerializer):
    nombre_tipo = serializers.CharField(required = False)
    class Meta:
        model = Tipos_KRI
        fields = '__all__'

class KriSerializer(serializers.ModelSerializer):
    tipos_kri = TipoKriSerializer()

    class Meta:
        model = KRI
        fields = '__all__'

# serializador para anidados
class KriSerializers(serializers.ModelSerializer):
    descripcion_kri = serializers.CharField(required = False)
    tipos_kri = TiposKriSerializer(required = False)

    class Meta:
        model = KRI
        fields = '__all__'

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class ComentarioSerializer(serializers.ModelSerializer):
    usuario = UsuariosSerializer()
    class Meta:
        model = Comentarios
        fields = '__all__'


class RiesgoSerializer(serializers.ModelSerializer):
    impacto_display = serializers.CharField(source = "get_impacto_display", required = False)
    probabilidad_display = serializers.CharField(source = "get_probabilidad_ocurrencia_display",required = False)
    idpropietario = serializers.IntegerField(required = False)
    propietario = PropietariosSerializer(required = False)
    idcategoria = serializers.IntegerField(required = False)
    categorias = CategoriasSerializers(required = False)
    idfuente_riesgo = serializers.IntegerField(required = False)
    fuente_riesgo = FuentesRiesgosSerializer(required = False)
    riesgos_servicios = ServiciosSerializers(many=True,required = False)
    idriesgos_servicios = serializers.ListField(required = False)
    magnitud_impacto = MagnitudImpactosSerializer(required = False)
    idmagnitud_impacto = serializers.IntegerField(required = False)
    idestados_riesgos = serializers.IntegerField(required = False)
    estados_riesgos = EstadosRiesgosSerializers(required = False)
    idestrategia = serializers.IntegerField(required = False)
    estrategia = EstrategiasSerializer(required = False)
    # comentario = ComentarioSerializer(many=True)
    idkri = serializers.IntegerField(required = False)
    kri = KriSerializers(required = False)

    class Meta:
        model = Riesgos
        fields = ('id','riesgo',
        'fecha_identificacion_riesgo','escenario_riesgo',
        'riesgos_servicios','idriesgos_servicios','activos_afectados','propietario',
        'idpropietario','idcategoria',
        'categorias','form_ident_riesgo',
        'fuente_riesgo','idfuente_riesgo','impacto','impacto_display',
        'probabilidad_ocurrencia','probabilidad_display',
        'nivel_riesgo','magnitud_impacto','idmagnitud_impacto',
        'estados_riesgos','idestados_riesgos','fecha_estado_riesgo',
        'control','estrategia','idestrategia',
        'comentario_local','kri','idkri',
        'importancia','comentario')
    
    def create(self,validated_data):
        riesgo = validated_data['riesgo']
        fecha_identificacion_riesgo = validated_data['fecha_identificacion_riesgo']
        escenario_riesgo = validated_data['escenario_riesgo']
        activos_afectados = validated_data['activos_afectados']
        propietario = Propietario.objects.get(pk=validated_data['idpropietario'])
        categorias = Categorias.objects.get(pk=validated_data['idcategoria'])
        form_ident_riesgo = validated_data['form_ident_riesgo']
        fuente_riesgo = FuenteRiesgos.objects.get(pk=validated_data['idfuente_riesgo'])
        impacto = validated_data['impacto']
        probabilidad_ocurrencia = validated_data['probabilidad_ocurrencia']
        magnitud_impacto = MagnitudImpacto.objects.get(pk=validated_data['idmagnitud_impacto'])
        estados_riesgos = EstadosRiesgos.objects.get(pk=validated_data['idestados_riesgos'])
        fecha_estado_riesgo = validated_data['fecha_estado_riesgo']
        control = validated_data['control']
        estrategia = Estrategia.objects.get(pk=validated_data['idestrategia'])
        comentario_local = validated_data['comentario_local']
        kri = KRI.objects.get(pk=validated_data['idkri'])
        importancia = validated_data['importancia']
        # comentario = validated_data['comentario']

        data = {'riesgo':riesgo,'fecha_identificacion_riesgo':fecha_identificacion_riesgo,
        'escenario_riesgo':escenario_riesgo,'activos_afectados':activos_afectados,
        'propietario':propietario,'categorias':categorias,'form_ident_riesgo':form_ident_riesgo,
        'fuente_riesgo':fuente_riesgo,'impacto':impacto,'probabilidad_ocurrencia':probabilidad_ocurrencia,
        'magnitud_impacto':magnitud_impacto,'estados_riesgos':estados_riesgos,'fecha_estado_riesgo': fecha_estado_riesgo,
        'control':control,'estrategia':estrategia,'comentario_local':comentario_local,'kri':kri,'importancia':importancia
        }

        instancia = Riesgos.objects.create(**data)

        ries = validated_data['idriesgos_servicios']
        print(ries)
        lista = []
        for x in ries:
            servicios = Servicios.objects.get(pk=x) 
            lista.append(servicios)
        instancia.riesgos_servicios.set(lista)
        
        return instancia

        
    def update(self, instance, validated_data):
        instance.riesgo = validated_data.get('riesgo',instance.riesgo)       
        instance.fecha_identificacion_riesgo = validated_data.get('fecha_identificacion_riesgo',instance.fecha_identificacion_riesgo)
        instance.escenario_riesgo = validated_data.get('escenario_riesgo',instance.escenario_riesgo)

        # instance.riesgos_servicios = validated_data.get('riesgos_servicios',instance.riesgos_servicios)

        instance.activos_afectados = validated_data.get('activos_afectados',instance.activos_afectados)
        instance.propietario = Propietario.objects.get(pk=validated_data['idpropietario'])
  
        instance.categorias = Categorias.objects.get(pk=validated_data['idcategoria']) 
        instance.form_ident_riesgo = validated_data.get('form_ident_riesgo',instance.form_ident_riesgo)

        instance.fuente_riesgo = FuenteRiesgos.objects.get(pk=validated_data['idfuente_riesgo'])

        instance.impacto = validated_data.get('impacto',instance.impacto)
        instance.probabilidad_ocurrencia = validated_data.get('probabilidad_ocurrencia',instance.probabilidad_ocurrencia)

        instance.magnitud_impacto = MagnitudImpacto.objects.get(pk=validated_data['idmagnitud_impacto'])
        instance.estados_riesgos = EstadosRiesgos.objects.get(pk=validated_data['idestados_riesgos'])

        instance.fecha_estado_riesgo = validated_data.get('fecha_estado_riesgo',instance.fecha_estado_riesgo)
        instance.control = validated_data.get('control',instance.control)

        instance.estrategia = Estrategia.objects.get(pk=validated_data['idestrategia'])

        instance.comentario_local = validated_data.get('comentario_local',instance.comentario_local)

        instance.kri = KRI.objects.get(pk=validated_data['idkri'])
        
        instance.importancia = validated_data.get('importancia',instance.importancia)
        # instance.comentario = validated_data.get('comentario',instance.comentario)
        instance.save()
        return instance
        
