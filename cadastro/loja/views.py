from dataclasses import fields
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Categoria, Clientes, Produto, Avaliacoes
from .serializer import CategoriaSerializer, ProdutoSerializer, ClienteSerializer, AvaliacaoSerializer
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import viewsets
from django_filters import rest_framework as filters
from django_filters.rest_framework import FilterSet

# Create your views here.
        
class ProdutoList(ListCreateAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    
    #Não permitir cadastrar produto com preço negativo
    def post(self):
        if float (request.data['preco']) < 0:
            return Response({'ERROR': 'Preço não pode ser negativo'})

    
    
class ProdutoDetalhe(RetrieveUpdateDestroyAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    # lookup_field = 'id'

    def get_queryset(self):
        return Avaliacoes.objects.filter(produto_id=self.kwargs['produtos_pk'])

    #Não permitir deletar produto, se qtd_estoque for maior que 0
    def delete(self, request, pk):
        produto = get_object_or_404(Produto, pk=pk)
                  
        if produto.qtd_estoque > 0:
            return Response({'ERROR':'Ainda tem estoque, não pode ser deletado'})
        produto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, *args, **kwargs):
        if float(request.data['preco']) < 0 or float(request.data['preco']) > 100 :
            return Response({'ERROR': 'valor não permitido!'})
        
        return super().put(request, *args, **kwargs)
        
    
class Categorias(ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class ProdutoFiltro(FilterSet):
    class Meta:
        model = Produto
        fields = {
            'categoria_id':['exact'],
            'qtd_estoque':['gt', 'lt']
        }
        
        
            
class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    # filterset_fields = ('categoria','qtd_estoque')
    filterset_class = ProdutoFiltro
    
    # def get_queryset(self):
    #     queryset = Produto.objects.all()
    #     categoria_id = self.request.query_params.get('categoria_id')
    #     if categoria_id is not None:
    #         queryset = queryset.filter(categoria_id=categoria_id)
        
    #     return queryset
    
class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Clientes.objects.all()
    serializer_class = ClienteSerializer
    
class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacoes.objects.all()
    serializer_class = AvaliacaoSerializer
    
    
    
    
@api_view(['GET', 'POST'])
def Produtos_listar(request):
    if request.method == 'GET':
        queryset = Produto.objects.all()
        serializer = ProdutoSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProdutoSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.validated_data)
            serializer.save()
            return Response('ok')
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'DELETE'])
def produto_detalhe(request, id):
        produto =  get_object_or_404(Produto, pk=id)
        if request.method == 'GET':
            serializer = ProdutoSerializer(produto)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = ProdutoSerializer(produto, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        elif request.method == 'DELETE':
            produto.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

    

