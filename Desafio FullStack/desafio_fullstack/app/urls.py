from django.urls import path
from . import views

urlpatterns = [
    # INDEX
    path('', views.index, name='index'),

    # EMPRESA
    path('empresas/', views.empresa_list, name='empresa_list'),
    path('empresa/criar/', views.empresa_create, name='empresa_create'),
    path('empresa/<int:pk>/editar/', views.empresa_update, name='empresa_update'),
    path('empresa/<int:pk>/excluir/', views.empresa_delete, name='empresa_delete'),
    
    # FORNECEDOR
    path('fornecedores/', views.fornecedor_list, name='fornecedor_list'),
    path('fornecedor/criar/', views.fornecedor_create, name='fornecedor_create'),
    path('fornecedor/<int:pk>/editar/', views.fornecedor_update, name='fornecedor_update'),
    path('fornecedor/<int:pk>/excluir/', views.fornecedor_delete, name='fornecedor_delete'),
]
