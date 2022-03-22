from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
# Create your models here.
  
class UserManager(BaseUserManager):
        def _create_user(self, email,  password, is_staff, is_superuser, **extra_fields):
            user = self.model(
                email = email,
                is_staff = is_staff,
                is_superuser = is_superuser,
                **extra_fields
            )
            user.set_password(password)
            user.save(using=self.db)
            return user

        def create_user(self,  email,  password=None, **extra_fields):
            return self._create_user( email,  password, False, False, **extra_fields)

        def create_superuser(self,  email,  password=None, **extra_fields):
            return self._create_user( email, password, True, True, **extra_fields)

# class Roles(models.Model):
#     rol = models.CharField('Roles',max_length=60,blank=False)
#     descripcion = models.TextField('Descripcion del rol')

#     class Meta:
#             verbose_name = 'Rol'
#             verbose_name_plural = 'Roles'

#     def __str__(self):
#         return self.rol

class Usuario(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('Correo Electrónico',max_length = 255, unique = True,)
    rol = models.CharField('Rol de Usuario',max_length = 50,blank=True)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email