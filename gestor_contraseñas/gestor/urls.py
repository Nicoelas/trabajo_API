from django.urls import path
from . import views

urlpatterns = [
    path('crear/', views.crear_usuario, name='crear_usuario'),
    path('actualizar/', views.actualizar_usuario, name='actualizar_usuario'),
    path('borrar/', views.borrar_usuario, name='borrar_usuario'),
]
