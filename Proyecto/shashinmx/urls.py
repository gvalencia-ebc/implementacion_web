from django.urls import path
from . import views

urlpatterns =[
    #index
    path('',views.index, name='index'),
    #galeria
    path('',views.galeria, name='galeria')
]