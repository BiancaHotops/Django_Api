from decimal import Decimal
import email
from turtle import mode
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Categoria(models.Model):
    nome= models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.nome
    
class Produto(models.Model):
    titulo =  models.CharField(max_length=255)
    descritivo =  models.TextField()
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    qtd_estoque = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0, message='O estoque minimo é 0'), MaxValueValidator(100, message='O estoque máximo é 100')]
    )
    
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
      
    
    def __str__(self) -> str:
        return self.titulo
    
    
class Clientes(models.Model):
    nome = models.CharField(max_length=200)
    idade = models.PositiveSmallIntegerField()
    email = models.EmailField()
    cpf  = models.CharField(max_length=11)
    celular = models.CharField(max_length=15)

    def __str__(self) -> str:
        return self.nome

class Avaliacoes(models.Model):
    cliente = models.ForeignKey(Clientes, on_delete=models.PROTECT)
    produto =  models.ForeignKey(Produto, on_delete=models.CASCADE)
    #categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    nota = models.DecimalField(max_digits=3, decimal_places=2)
    
    def __str__(self) -> str:
        return self.nota
    
    

