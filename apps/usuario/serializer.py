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

    class Meta:
        model = Usuario
        fields = ('id','email','password','rol')
    
    def create(self,validated_data):
        usuario = Usuario(**validated_data)
        usuario.set_password(validated_data['password'])
        usuario.save()
        return usuario

    def update(self, instance, validated_data):
        update_usuario = super().update(instance,validated_data)
        update_usuario.set_password(validated_data['password'])
        update_usuario.save()
        return update_usuario
    
