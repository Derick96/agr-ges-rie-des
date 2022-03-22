from rest_framework import viewsets
from .models import Riesgos
from .serializer import RiesgoSerializer

class RiesgosViewSet(viewsets.ModelViewSet):
    queryset = Riesgos.objects.all()
    serializer_class = RiesgoSerializer