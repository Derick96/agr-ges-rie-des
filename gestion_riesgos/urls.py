from django.contrib import admin
from django.urls import path,include
# from apps.usuario.views import Login


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.usuario.urls')),
    path('api/', include('apps.riesgos.router')),
    # path('',Login.as_view(),name='login'),
]
