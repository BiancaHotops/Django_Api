from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Produto
from .serializer import ProdutoSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404


# Create your views here.


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

