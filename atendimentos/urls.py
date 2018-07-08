
from django.urls import path

# Produtos
from .views import novo_atendimento, nova_compra


urlpatterns = (
    path('novo/atendimento', novo_atendimento, name="novo_atendimento"),
    path('nova/compra', nova_compra, name="nova_compra"),
)
