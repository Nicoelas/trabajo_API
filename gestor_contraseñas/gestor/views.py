# gestor/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Usuario
from json import loads

@csrf_exempt
def crear_usuario(request):
    if request.method == 'POST':
        data = loads(request.body)
        nombre_usuario = data.get('nombre_usuario')
        contraseña = data.get('contraseña')
        if nombre_usuario and contraseña:
            Usuario.objects.create(nombre_usuario=nombre_usuario, contraseña=contraseña)
            return JsonResponse({'mensaje': 'Usuario creado exitosamente'}, status=201)
        else:
            return JsonResponse({'error': 'Faltan datos'}, status=400)
    return JsonResponse({'error': 'Método no permitido'}, status=405)

@csrf_exempt
def actualizar_usuario(request):
    if request.method == 'POST':
        data = loads(request.body)
        nombre_usuario = data.get('nombre_usuario')
        nueva_contraseña = data.get('nueva_contraseña')
        try:
            usuario = Usuario.objects.get(nombre_usuario=nombre_usuario)
            usuario.contraseña = nueva_contraseña
            usuario.save()
            return JsonResponse({'mensaje': 'Contraseña actualizada exitosamente'}, status=200)
        except Usuario.DoesNotExist:
            return JsonResponse({'error': 'Usuario no encontrado'}, status=404)
    return JsonResponse({'error': 'Método no permitido'}, status=405)

@csrf_exempt
def borrar_usuario(request):
    if request.method == 'DELETE':
        data = loads(request.body)
        nombre_usuario = data.get('nombre_usuario')
        try:
            usuario = Usuario.objects.get(nombre_usuario=nombre_usuario)
            usuario.delete()
            return JsonResponse({'mensaje': 'Usuario borrado exitosamente'}, status=200)
        except Usuario.DoesNotExist:
            return JsonResponse({'error': 'Usuario no encontrado'}, status=404)
    return JsonResponse({'error': 'Método no permitido'}, status=405)
