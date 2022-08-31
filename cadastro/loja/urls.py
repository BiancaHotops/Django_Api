from django.urls import path
from . import views


urlpatterns = [
    path('produtos/', views.Produtos_listar),
    path('produtos/<id>/', views.produto_detalhe),
    
]
