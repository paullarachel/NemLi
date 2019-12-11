from django.contrib import admin
from django.urls import path
from . import views

app_name = 'gerenciador'
urlpatterns = [
    path('', views.PaginaLogin.as_view(), name='paginaLogin'),
    path('inicio', views.paginaInicial, name='paginaInicial'),
    path('cadastro', views.PaginaCadastro.as_view(), name='paginaCadastro'),
    path('cadastrar', views.cadastrar, name='cadastrar'),
    path('logar', views.logar, name='logar'),
    path('deslogar', views.deslogar, name='deslogar'),
    path('novo_livro', views.adicionarLivro, name='adicionarLivro'),
    path('excluir_livro/<int:livro_id>', views.excluirLivro, name='excluirLivro'),
    path('inicio/todos', views.ListarLivros.as_view(), name='listarTodos'),
    path('detalhes/<int:pk>', views.VisualizarLivro.as_view(), name='visualizarLivro')
]