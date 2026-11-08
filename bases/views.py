from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import Aprendiz_Form
from .models import aprendiz  # Importación del modelo en minúscula como lo definiste

def listar(request):
    """Vista principal para mostrar la tabla con todos los registros."""
    # Trae todos los aprendices desde la base de datos
    registros_aprendices = aprendiz.objects.all()
    
    # Pasa los registros a la plantilla index.html
    return render(request, 'bases/index.html', {'aprendices': registros_aprendices})


def crear_aprendiz(request):
    """Vista para agregar un nuevo aprendiz."""
    if request.method == 'POST':
        form = Aprendiz_Form(request.POST)
        if form.is_valid():
            form.save() 
            messages.success(request, '¡Aprendiz creado con éxito!')  
            return redirect('crear_aprendiz')  
    else:
        form = Aprendiz_Form()  
        
    return render(request, 'bases/aprendiz.html', {'form': form})


def editar_aprendiz(request, documento):
    aprendiz_objeto = get_object_or_404(aprendiz, documento=documento)
    form = Aprendiz_Form(request.POST or None, instance=aprendiz_objeto)
    if 'documento' in form.fields:
        form.fields['documento'].disabled = True
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, '¡Aprendiz actualizado con éxito!')
        return redirect('bases')  
        
    return render(request, 'bases/aprendiz.html', {'form': form})

from . import models 


def eliminar_aprendiz(request, documento):
    # Usamos models.aprendiz para que Django busque dinámicamente la clase
    aprendiz_objeto = get_object_or_404(models.aprendiz, documento=documento)
    aprendiz_objeto.delete()
    messages.success(request, '¡Aprendiz eliminado con éxito!')
    return redirect('bases')

def mapa(request):
    return render(request, 'bases/mapa.html')

def buscar_aprendiz(request):
    documento = request.GET.get('documento', '').strip()
    resultado = None
    buscado = False

    if documento:
        buscado = True
        try:
            resultado = aprendiz.objects.filter(documento=documento).first()
        except ValueError:
            
            resultado = None

    return render(request, 'bases/buscar.html', {
        'documento': documento,
        'resultado': resultado,
        'buscado': buscado,
    })
import folium  
from folium.plugins import Geocoder 
def ver_mapa_aprendices(request):
    coordenadas_inicio = [4.5826, -74.2104]
    
    mapa = folium.Map(
        location=coordenadas_inicio, 
        zoom_start=14,
        control_scale=True,
        tiles='https://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png',
        attr='&copy; <a href="https://openstreetmap.org">OpenStreetMap</a> contributors'
    )
    
    # 2. AÑADE ESTA LÍNEA justo antes de convertir el mapa a HTML
    Geocoder(
        placeholder="Buscar dirección o lugar...",
        collapsed=False,  # Muestra la barra de texto abierta por defecto
        position='topright'  # Ubica la barra en la esquina superior derecha
    ).add_to(mapa)
    
    # ... Aquí mantienes tu lógica actual para pintar los marcadores ...
    
    mapa_html = mapa._repr_html_()
    return render(request, 'bases/mapa.html', {'mapa_html': mapa_html})
