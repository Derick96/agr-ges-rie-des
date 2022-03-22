from django.urls import path
from rest_framework.routers import DefaultRouter
from . import viewsets 
from . import views

router = DefaultRouter()
router.register(r'riesgo',viewsets.RiesgosViewSet, basename="riesgo")

urlpatterns = router.urls
