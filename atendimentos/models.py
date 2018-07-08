from django.db import models

from cruds.models import Clientes, Vendedores, Produtos

# Create your models here.


class Compras(models.Model):

    id = models.AutoField(primary_key=True)
    cod_produto = models.ForeignKey(Produtos, on_delete=models.CASCADE)
    quantidade = models.FloatField(max_length=50)
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    valor_over = models.DecimalField(max_digits=5, decimal_places=2)

    def __int__(self):
        return self.cod_produto

class Atendimentos(models.Model):

    TP_PAGAMENTO = (
        ('AV', 'A Vista'),
        ('CH', 'Cheque'),
        ('PR', 'Parcelas'),
    )

    id = models.AutoField(primary_key=True)
    cod_cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    cod_vendedor = models.ForeignKey(Vendedores, on_delete=models.CASCADE)
    cod_compra = models.ManyToManyField(Compras)
    observacao = models.CharField(max_length=100)
    data_entrega = models.DateField(max_length=100)
    valor_total = models.DecimalField(max_digits=5, decimal_places=2)
    tipo_pgto = models.CharField(max_length=100, choices=TP_PAGAMENTO)
    valor_entrada = models.CharField(max_length=100)
    parcelas = models.IntegerField()
    data_vencimento = models.DateField() #fazer um many to many
    status = models.CharField(max_length=100)


    def __int__(self):
        return self.cod_cliente



# class Compra_Atend(models.Model):
#
#     id = models.AutoField(primary_key=True)
#     cod_compra = models.ForeignKey(Compras, on_delete=models.CASCADE)
#     cod_atend = models.ForeignKey(Atendimentos, on_delete=models.CASCADE)
#     valor = models.DecimalField(max_digits=5, decimal_places=2)
#     valor_over = models.DecimalField(max_digits=5, decimal_places=2)
#
#     def __str__(self):
#         return self.cod_produto
