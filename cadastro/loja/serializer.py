from decimal import Decimal
from rest_framework import serializers

from .models import Produto



class ProdutoSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    titulo = serializers.CharField(max_length=255)
    preco = serializers.DecimalField(max_digits=6, decimal_places=2)
    preco_taxa = serializers.SerializerMethodField(method_name='calcular_taxa')
    

    def calcular_taxa(self, produto: Produto):
        return produto.preco * Decimal(1.1 )
    