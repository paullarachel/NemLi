from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Livro, AutorLivro, Autor

# Create your views here.

def paginaBiblioteca(request):
    livros = Livro.objects.all()
    context = {'livros': livros}
    return render(request, '', context)

def adicionarLivro(request):
    livro = Livro()
    livro.nome = request.POST['nome']
    livro.isbn_13 = request.POST['isbn_13']
    livro.ano = request.POST['ano']
    livro.sinopse = request.POST['sinopse']
    livro.save()