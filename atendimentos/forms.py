from django.forms import ModelForm
from .models import Atendimentos, Compras



class AtendimentoForm(ModelForm):
    class Meta:
        model = Atendimentos
        fields = ['cod_cliente',
                  'cod_vendedor',
                  'cod_compra',
                  'observacao',
                  'data_entrega',
                  'valor_total',
                  'tipo_pgto',
                  'valor_entrada',
                  'parcelas',
                  'data_vencimento']


class CompraForm(ModelForm):
    class Meta:
        model = Compras
        fields = ['cod_produto',
                  'quantidade',
                  'valor',
                  'valor_over',]

