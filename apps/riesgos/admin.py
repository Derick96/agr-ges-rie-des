from django.contrib import admin
from .models import (Riesgos,Propietario,Categorias,FuenteRiesgos,MagnitudImpacto,
EstadosRiesgos,Estrategia,KRI,Tipos_KRI,Servicios,TiposServicios,Comentarios)

# Register your models here.
admin.site.register(Riesgos)
admin.site.register(Propietario)
admin.site.register(Categorias)
admin.site.register(FuenteRiesgos)
admin.site.register(MagnitudImpacto)
admin.site.register(EstadosRiesgos)
admin.site.register(Estrategia)
admin.site.register(KRI)
admin.site.register(Tipos_KRI)
admin.site.register(Servicios)
admin.site.register(TiposServicios)
admin.site.register(Comentarios)
