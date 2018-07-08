from django.db import models

from django.db.models.deletion import CASCADE


class Medidas(models.Model):

    id = models.AutoField(primary_key=True)
    desc_medida = models.CharField(max_length=50)

    def __str__(self):
        return self.desc_medida


class Fornecedores(models.Model):

    id = models.AutoField(primary_key=True)
    empresa = models.CharField(max_length=40)
    nome_prop = models.CharField(max_length=50)
    telefone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    tipo_fornecedor = models.CharField(max_length=50)

    def __str__(self):
        return self.empresa


class Produtos(models.Model):

    id = models.AutoField(primary_key=True)
    fornecedor = models.ForeignKey(Fornecedores, on_delete=models.CASCADE) #fk FORNECEDOR
    nome_produto = models.CharField(max_length=100)
    desc_produto = models.CharField(max_length=100)
    medida = models.ForeignKey(Medidas, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=6, decimal_places=2)


    def __str__(self):
        return self.nome_produto


class Clientes(models.Model):

    id = models.AutoField(primary_key=True)
    razao_social = models.CharField(max_length=100)
    nome_fantasia = models.CharField(max_length=100)
    nome_cliente = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    insc_estadual = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    contato_cel = models.CharField(max_length=100)
    contato_tel = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    site = models.CharField(max_length=100)


    def __str__(self):
        return self.nome_cliente


class Vendedores(models.Model):

    id = models.AutoField(primary_key=True)
    nome_vendedor = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contato = models.CharField(max_length=100)


    def __str__(self):
        return self.nome_vendedor







