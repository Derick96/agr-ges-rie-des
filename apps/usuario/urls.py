from django.urls import path
from rest_framework.routers import DefaultRouter
from . import viewsets 
from . import views

router = DefaultRouter()
router.register(r'usuario',viewsets.UsuarioViewSet, basename="usuario")

urlpatterns = router.urls
urlpatterns += path('login',views.login),