from django.shortcuts import render
from django.views import generic
from .models import Livro, AutorLivro, Autor
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class ListarLivros(generic.ListView):
    model = Livro
    template_name = 'gerenciador/list_todos.html'

@login_required
def paginaInicial(request):
    lido = Livro.objects.filter(user=request.user, estado=0).order_by("-id")[0:5]
    lendo = Livro.objects.filter(user=request.user, estado=1).order_by("-id")[0:5]
    parado = Livro.objects.filter(user=request.user, estado=2).order_by("-id")[0:5]
    quero_ler = Livro.objects.filter(user=request.user, estado=3).order_by("-id")[0:5]
    context = {'lido': lido,
               'quero_ler': quero_ler,
               'lendo': lendo,
               'parado': parado
               }
    return render(request, 'gerenciador/inicio.html', context)

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

def deslogar(request):
    logout(request)
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

def adicionarLivro(request):
    livro = Livro()
    autor = Autor()
    autor_livro = AutorLivro()
    livro.user = request.user
    livro.nome = request.POST['nome']
    livro.isbn_13 = request.POST['isbn_13']
    livro.capa = request.POST['capa']
    livro.sinopse = request.POST['sinopse']
    livro.estado = request.POST['estado']
    autor.nome = request.POST['autor']
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

def excluirLivro(request, livro_id):
    livro = Livro.objects.get(pk=livro_id)
    livro.delete()
    return HttpResponseRedirect(reverse('gerenciador:listarTodos'))
    

