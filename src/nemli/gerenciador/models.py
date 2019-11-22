from django.db import models

# Create your models here.

class Livro(models.Model):
    nome = models.CharField(max_length=200)
    isbn_13 = models.CharField(max_length=13)
    sinopse = models.CharField(max_length=2000)
    ano = models.CharField(max_length=4)

class Autor(models.Model):
    nome = models.CharField(max_length=200)

class AutorLivro(models.Model):
    autor = models.ForeignKey(Autor, on_delete=models.PROTECT)
    livro = models.ForeignKey(Livro, on_delete=models.PROTECT)