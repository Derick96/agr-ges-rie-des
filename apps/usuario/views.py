# from rest_framework import status

from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from .models import Usuario
from django.contrib.auth.hashers import check_password
# from rest_framework.authtoken.views import ObtainAuthToken

# from apps.usuario.serializer import UsuarioTokenSerializer

@api_view(['POST'])
def login(request):

    email = request.POST.get('email')
    password = request.POST.get('password')
    # roles = RolesSerializer(read_only=True)

    try:
        usuario = Usuario.objects.get(email=email)
    except Usuario.DoesNotExist:
        return Response("Usuario Incorrecto")
    
    pwd_valid = check_password(password,usuario.password)
    if not pwd_valid:
        return Response("Passoword Incorrecto")
        
    token,_ = Token.objects.get_or_create(user = usuario)
    return Response({
            'token': token.key,
            'email': usuario.email,
            'password': usuario.password,
            'rol': usuario.rol,
            
        })
    # print(token.key)



# class Login(ObtainAuthToken):

#     def post(self,request,*args,**kwargs):
#         login_serializer = self.serializer_class(data = request.data, context = {'request':request})
#         if login_serializer.is_valid():
#             usuario =  login_serializer.validated_data['user']
#             if usuario:
#                 token,created = Token.objects.get_or_create(user = usuario)
#                 usuario_serializer = UsuarioTokenSerializer(usuario)
#                 if created:
#                     return Response({
#                         'token': token.key,
#                         'user': usuario_serializer.data,
#                         'message': 'Inicio de sesion exitoso'
#                     }, status = status.HTTP_201_CREATED)
#                 else:
#                     token.delete()
#                     token = Token.objects.create(user = usuario)
#                     return Response({
#                         'token': token.key,
#                         'user': usuario_serializer.data,
#                         'message': 'Inicio de sesion exitoso'
#                     }, status = status.HTTP_201_CREATED)
#             else:
#                 return Response({'error':'Este usuario no puede iniciar sesion'},
#                                     status = status.HTTP_401_UNAUTHORIZED)
#         else:
#             return Response({'error': 'Email o password incorrecto'},
#                                     status = status.HTTP_400_BAD_REQUEST)
#         return Response({'mensaje':'hola desde response'},status = status.HTTP_200_OK)