from .models import Usuario
from rest_framework import serializers



# class UsuarioTokenSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Usuario
#         fields = ('email','usuarios_roles')

# class RolesSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Roles
#         fields = '__all__'
    

class UsuarioSerializer(serializers.ModelSerializer):

    # usuarios_roles = RolesSerializer(many=True)
   
    class Meta:
        model = Usuario
        fields = ('id','email','password','rol')

    # def create_or_update_roles(self,roles):
    #     lista = []
    #     for rol in roles:
    #         rol_instance = Roles.objects.update_or_create(pk=rol.get('id'),defaults=rol)
    #         lista.append(rol_instance.pk)
    #     return lista
    
    def create(self,validated_data):
        usuario = Usuario(**validated_data)
        usuario.set_password(validated_data['password'])
        # roles = validated_data.pop('usuario_roles',[])
        # usuario.usuarios_roles.set(self.create_or_update_roles(roles))
        usuario.save()
        return usuario

    def update(self, instance, validated_data):
        update_usuario = super().update(instance,validated_data)
        update_usuario.set_password(validated_data['password'])
        # roles = validated_data.pop('usuario_roles',[])
        # update_usuario.usuarios_roles.set(self.create_or_update_roles(roles))
        update_usuario.save()
        return update_usuario
    
