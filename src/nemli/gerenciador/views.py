from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Livro, AutorLivro, Autor
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def logar(request):
    user = authenticate(request, username=request.POST['usuario'], password=request.POST['senha'])
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('gerenciador:paginaInicial'))
    else:
        messages.add_message(
            request, messages.ERROR,
            'Usuário ou senha incorretos.'
        )
        return HttpResponseRedirect(reverse('gerenciador:paginaLogin'))

def paginaLogin(request):
    return render(request, 'gerenciador/registration/login.html')

def paginaCadastro(request):
    return render(request, 'gerenciador/cadastro.html')

def cadastrar(request):
    username = request.POST['usuario']
    email = request.POST['email']
    password = request.POST['senha']
    user = User.objects.create_user(username, email=email, password=password)
    messages.add_message(
        request, messages.SUCCESS,
        'Usuário cadastrado com sucesso!'
    )
    user.save()
    return HttpResponseRedirect(reverse('gerenciador:paginaCadastro'))

@login_required
def paginaInicial(request):
    livros = Livro.objects.filter(user=request.user)
    context = {'livros': livros}
    return render(request, 'gerenciador/inicio.html', context)

def adicionarLivro(request):
    livro = Livro()
    autor = Autor()
    autor_livro = AutorLivro()
    user = request.user
    livro.nome = request.POST['nome']
    livro.isbn_13 = request.POST['isbn_13']
    livro.ano = request.POST['ano']
    livro.capa = request.POST['capa']
    livro.sinopse = request.POST['sinopse']
    autor = request.POST['autor']
    livro.save()
    autor.save()
    autor_livro.livro = livro
    autor_livro.autor = autor
    autor_livro.save()
    messages.add_message(
        request, messages.SUCCESS,
        'Livro cadastrado com sucesso!'
    )
    return HttpResponseRedirect(reverse('gerenciador:paginaInicial'))

