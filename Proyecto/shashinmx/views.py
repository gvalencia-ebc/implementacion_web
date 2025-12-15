import os
from django.conf import settings
from django.shortcuts import render
from django.contrib.staticfiles.finders import find


# Create your views here.

#INDEX
def index(request):
    return render(request,'shashinmx/index.html')

def galeria(request):
    SUBDIR_REL = 'shashinmx/images/'
    ruta_absoluta = find(SUBDIR_REL)
    galeria_grid =[]

    if ruta_absoluta and os.path.isdir(ruta_absoluta):
        nombres = os.listdir(ruta_absoluta)

        for nombre in nombres:

            
            if nombre.lower().endswith(('.png','.jpg','.gif','.webp')):
                ruta_estatica= os.path.join(SUBDIR_REL, nombre)
                galeria_grid.append(ruta_estatica)

    contexto = {'images':galeria_grid}
    
    return render(request, 'shashinmx/galeria.html', contexto)

def blog(request):
    return render(request, 'shashinmx/blog.html',)

def contacto(request):
    return render(request, 'shashinmx/contacto.html',)
