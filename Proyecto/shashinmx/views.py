from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#INDEX
def index(request):
    return render(request,'shashinmx/index.html')

def galeria(request):
    return render(request, 'shashinmx/galeria.html')