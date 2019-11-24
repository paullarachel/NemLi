from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Livro(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    nome = models.CharField(max_length=200)
    editora = models.CharField(max_length=50)
    isbn_13 = models.CharField(max_length=13)
    sinopse = models.CharField(max_length=2000)
    capa = models.CharField(max_length=100)
    estado_choices = [
        (0, 'Lido'),
        (1, 'Estou lendo'),
        (2, 'Parei de ler'),
        (3, 'Quero ler')
    ]
    estado = models.IntegerField(choices=estado_choices, default=0)

class Autor(models.Model):
    nome = models.CharField(max_length=200)

class AutorLivro(models.Model):
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)