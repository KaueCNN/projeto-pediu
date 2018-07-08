from django.contrib import admin

from .models import Compras, Atendimentos

# Register your models here.

admin.site.register(Compras)
admin.site.register(Atendimentos)