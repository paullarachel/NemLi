from django.contrib import admin
from django.urls import path
from . import views

app_name = 'gerenciador'
urlpatterns = [
    path('', views.PaginaLogin.as_view(), name='paginaLogin'),
    path('inicio/', views.paginaInicial, name='paginaInicial'),
    path('cadastro', views.PaginaCadastro.as_view(), name='paginaCadastro'),
    path('cadastrar', views.cadastrar, name='cadastrar'),
    path('logar', views.logar, name='logar'),
    path('deslogar', views.deslogar, name='deslogar'),
    path('novo_livro', views.adicionarLivro, name='adicionarLivro'),
    path('excluir_livro/<int:livro_id>', views.excluirLivro, name='excluirLivro'),
    path('detalhes/<int:livro_id>', views.visualizarLivro, name='visualizarLivro'),
    path('editar_estado/<int:livro_id>', views.editarEstado, name='editarEstado'),
    path('inicio/todos', views.ListarLivros.as_view(), name='listarTodos'),
    path('inicio/lidos', views.listarLidos, name='listarLidos'),
    path('inicio/lendo', views.listarLendo, name='listarLendo'),
    path('inicio/parados', views.listarParados, name='listarParados'),
    path('inicio/lista_esejos', views.listarDesejos, name='listarDesejos')   
]