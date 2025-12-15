from django.urls import path
from . import views

urlpatterns =[
    #index
    path('',views.index, name='index'),
    #galeria
    path('galeria/',views.galeria, name='galeria'),
    
    path('blog/',views.blog, name='blog'),

    path('contacto/',views.contacto, name='contacto'),

]