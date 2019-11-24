from django.contrib import admin
from django.urls import path
from . import views

app_name = 'gerenciador'
urlpatterns = [
    path('login', views.paginaLogin, name='paginaLogin'),
    path('inicio', views.paginaInicial, name='paginaInicial'),
    path('cadastro', views.paginaCadastro, name='paginaCadastro'),
    path('cadastrar', views.cadastrar, name='cadastrar'),
    path('logar', views.logar, name='logar')
]