from django.shortcuts import render
from django.utils import timezone
from .models import Publicacion
def lista_public(request):

    publicaciones = Publicacion.objects.filter(fecha_creacion__lte=timezone.now()).order_by('fecha_creacion')

    return render(request, 'blog/lista_public.html', {'publicaciones':publicaciones})
def publicacion_nueva(request):
    # Aquí irá el código para manejar el formulario más adelante
    return render(request, 'blog/publicacion_editar.html', {})