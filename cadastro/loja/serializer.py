from dataclasses import field
from decimal import Decimal
from rest_framework import serializers
from .models import Avaliacoes, Categoria, Clientes, Produto

from .models import Produto



class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['id', 'titulo', 'preco','categoria', 'qtd_estoque']
        
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Clientes
        fields = ['id', 'nome', 'idade', 'email', 'celular']
        
class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Avaliacoes
        fields = ['id', 'cliente','produto', 'nota']
     
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nome']
        
        
        
    #     id = serializers.IntegerField()
    #     titulo = serializers.CharField(max_length=255)
    #     preco = serializers.DecimalField(max_digits=6, decimal_places=2)
    #     preco_taxa = serializers.SerializerMethodField(method_name='calcular_taxa')
    

    # def calcular_taxa(self, produto: Produto):
    #     return produto.preco * Decimal(1.1 )
    