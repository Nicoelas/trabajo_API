# gestor_contraseñas/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gestor/', include('gestor.urls')),  # Incluye las URLs de la app gestor
]
