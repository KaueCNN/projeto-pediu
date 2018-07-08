
from django.urls import path

# Produtos
from .views import listar_produtos
from .views import novo_produto
from .views import produto_update
from .views import produto_delete
# Fornecedores
from .views import listar_fornecedores
from .views import novo_fornecedor
from .views import fornecedor_update
from .views import fornecedor_delete
# Clientes
from .views import listar_clientes
from .views import novo_cliente
from .views import cliente_update
from .views import cliente_delete
# Vendedor
from .views import listar_vendedores
from .views import novo_vendedor
from .views import vendedor_update
from .views import vendedor_delete



urlpatterns = [
    ## Function-based views URLs ##

    #Produtos
    path('lista/produto', listar_produtos, name="listar_produtos"),
    path('novo/produto', novo_produto, name="novo_produto"),
    path('update/produto/<int:id>', produto_update, name="produtos_update"),
    path('delete/produto/<int:id>', produto_delete, name="produtos_delete"),
    #Fornecedores
    path('lista/fornecedor', listar_fornecedores, name="listar_fornecedores"),
    path('novo/fornecedor', novo_fornecedor, name="novo_fornecedor"),
    path('update/fornecedor/<int:id>', fornecedor_update, name="fornecedor_update"),
    path('delete/fornecedor/<int:id>', fornecedor_delete, name="fornecedor_delete"),
    # Clientes
    path('lista/cliente', listar_clientes, name="listar_clientes"),
    path('novo/cliente', novo_cliente, name="novo_cliente"),
    path('update/cliente/<int:id>', cliente_update, name="cliente_update"),
    path('delete/cliente/<int:id>', cliente_delete, name="cliente_delete"),
    # Vendedores
    path('lista/vendedor', listar_vendedores, name="listar_vendedores"),
    path('novo/vendedor', novo_vendedor, name="novo_vendedor"),
    path('update/vendedor/<int:id>', vendedor_update, name="vendedor_update"),
    path('delete/vendedor/<int:id>', vendedor_delete, name="vendedor_delete"),

]
