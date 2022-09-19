from cgitb import lookup
from django.urls import path, include
from . import views
from rest_framework_nested import routers

rota = routers.DefaultRouter()
rota.register('produtos', views.ProdutoViewSet, basename='produtos')
# rota.register('avaliacao', views.AvaliacaoViewSet, basename='avaliacao')
rota.register('clientes', views.ClienteViewSet, basename='clientes')

rota_produto = routers.NestedDefaultRouter(rota, 'produtos', lookup='produtos')
rota_produto.register('avaliacoes', views.AvaliacaoViewSet)

urlpatterns = [
    # path('produtos/', views.ProdutoList.as_view()),
    # path('produtos/', views. ProdutoViewSet.as_view()),
    path('', include(rota.urls)),
    path('', include(rota_produto.urls)),
    # path('clientes/', views.Clientes.as_view()),
    # path('avaliacoes/', views.Avaliacoes.as_view()),
    path('categorias/', views.Categorias.as_view()),
    # path('produtos/<int:pk>', views.ProdutoDetalhe.as_view()),
    # path('produtos/<id>/', views.produto_detalhe),
    
]
