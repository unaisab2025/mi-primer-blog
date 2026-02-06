from django.urls import path
from . import views
urlpatterns = [
path('', views.lista_public, name=' lista_public'),
path('publicacion/nueva/', views.publicacion_nueva, name='publicacion_nueva'),
]

