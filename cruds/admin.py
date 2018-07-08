from django.contrib import admin
from .models import Produtos, Fornecedores, Medidas,Clientes


#ADICIONANDO COISAS NO ADMIN
admin.site.register(Produtos)
admin.site.register(Fornecedores)
admin.site.register(Medidas)
admin.site.register(Clientes)

# Register your models here.
