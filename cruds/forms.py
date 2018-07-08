from django.forms import ModelForm
from .models import Produtos
from .models import Fornecedores
from .models import Clientes
from .models import Vendedores


class ProdutoForm(ModelForm):
    class Meta:
        model = Produtos
        fields = ['fornecedor',
                  'nome_produto',
                  'desc_produto',
                  'medida',
                  'valor']


class FornecedorForm(ModelForm):
    class Meta:
        model = Fornecedores
        fields = ['empresa',
                  'nome_prop',
                  'telefone',
                  'email',
                  'tipo_fornecedor']

class ClienteForm(ModelForm):
    class Meta:
        model = Clientes
        fields = ['razao_social',
                  'nome_fantasia',
                  'nome_cliente',
                  'tipo',
                  'insc_estadual',
                  'cnpj',
                  'endereco',
                  'contato_cel',
                  'contato_tel',
                  'email',
                  'site']

class VendedorForm(ModelForm):
    class Meta:
        model = Vendedores
        fields = ['nome_vendedor',
                  'email',
                  'contato'
                  ]