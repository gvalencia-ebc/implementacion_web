import os
from django.conf import settings
from django.shortcuts import render
from django.contrib.staticfiles.finders import find
from PIL import Image
# Create your views here.

#INDEX
def index(request):
    return render(request,'shashinmx/index.html')

def galeria(request):
    SUBDIR_REL = 'shashinmx/images/'
    
    RUTA_ESTATICA_APP = os.path.join(
        settings.BASE_DIR,
        'shashinmx',
        'static',
        'shashinmx',
        'images',) 
    
    galeria_grid = []
    
    for nombre in os.listdir(RUTA_ESTATICA_APP):
        if nombre.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            
            ruta_absoluta = os.path.join(RUTA_ESTATICA_APP, nombre)
            is_wide = False
            
            try:
                with Image.open(ruta_absoluta) as img:
                    width, height = img.size
                    
                    if width > (height * 1.2):
                        is_wide = True
            except Exception as e:
                print(f"Error al procesar imagen {nombre}: {e}")
                
            galeria_grid.append({
                'path': os.path.join(SUBDIR_REL, nombre), 
                'is_wide': is_wide  
            })

    contexto = {'images': galeria_grid} 
    return render(request, 'shashinmx/galeria.html', contexto)

def blog(request):
    return render(request, 'shashinmx/blog.html',)

def contacto(request):
    return render(request, 'shashinmx/contacto.html',)
