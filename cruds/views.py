from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Produtos
from .models import Fornecedores
from .models import Clientes
from .models import Vendedores

from .forms import ProdutoForm
from .forms import FornecedorForm
from .forms import ClienteForm
from .forms import VendedorForm




######### FORNECEDOR #########


@login_required
def listar_fornecedores(request):
    fornecedores = Fornecedores.objects.all()
    return render(request, 'fornecedores/lista_fornecedor.html', {'fornecedores': fornecedores})



@login_required
def novo_fornecedor(request):
    form = FornecedorForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('listar_fornecedores')

    return render(request, 'fornecedores/novo_fornecedor.html', {'form': form})

@login_required
def fornecedor_update(request, id):
    fornecedores = get_object_or_404(Fornecedores, pk=id)
    form = FornecedorForm(request.POST or None, request.FILES or None, instance=fornecedores)

    if form.is_valid():
        form.save()
        return redirect('listar_fornecedores')

    return render(request, 'fornecedores/novo_fornecedor.html', {'form': form})


@login_required
def fornecedor_delete(request, id):
    fornecedores = get_object_or_404(Fornecedores, pk=id)

    if request.method == 'POST':
        fornecedores.delete()
        return redirect('listar_fornecedores')

    return render(request, 'fornecedores/del_confirm_fornecedor.html', {'fornecedores': fornecedores})


############ PRODUTOS ###############

@login_required
def listar_produtos(request):
    produtos =  Produtos.objects.all()
    return render(request, 'produtos/lista_produto.html', {'produtos': produtos})



@login_required
def novo_produto(request):
    form = ProdutoForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('listar_produtos')

    return render(request, 'produtos/novo_produto.html', {'form': form})



@login_required
def produto_update(request, id):
    produtos = get_object_or_404(Produtos, pk=id)
    form = ProdutoForm(request.POST or None, request.FILES or None, instance=produtos)

    if form.is_valid():
        form.save()
        return redirect('listar_produtos')

    return render(request, 'produtos/novo_produto.html', {'form': form})



@login_required
def produto_delete(request, id):
    produtos = get_object_or_404(Produtos, pk=id)

    if request.method == 'POST':
        produtos.delete()
        return redirect('listar_produtos')

    return render(request, 'produtos/del_confirm_fornecedor.html', {'cruds': produtos})



############ CLIENTES ###############


@login_required
def listar_clientes(request):
    clientes =  Clientes.objects.all()
    return render(request, 'clientes/lista_cliente.html', {'clientes': clientes})


@login_required
def novo_cliente(request):
    form = ClienteForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('listar_clientes')

    return render(request, 'clientes/novo_cliente.html', {'form': form})



@login_required
def cliente_update(request, id):
    clientes = get_object_or_404(Clientes, pk=id)
    form = ClienteForm(request.POST or None, request.FILES or None, instance=clientes)

    if form.is_valid():
        form.save()
        return redirect('listar_clientes')

    return render(request, 'clientes/novo_cliente.html', {'form': form})



@login_required
def cliente_delete(request, id):
    cliente = get_object_or_404(Clientes, pk=id)

    if request.method == 'POST':
        cliente.delete()
        return redirect('listar_clientes')

    return render(request, 'clientes/del_confirm_cliente.html', {'cliente': cliente})


############ VENDEDOR ###############


@login_required
def listar_vendedores(request):
    vendedores =  Vendedores.objects.all()
    return render(request, 'vendedores/lista_vendedor.html', {'vendedores': vendedores})


@login_required
def novo_vendedor(request):
    form = VendedorForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('listar_vendedores')

    return render(request, 'vendedores/novo_vendedor.html', {'form': form})



@login_required
def vendedor_update(request, id):
    vendedores = get_object_or_404(Vendedores, pk=id)
    form = VendedorForm(request.POST or None, request.FILES or None, instance=vendedores)

    if form.is_valid():
        form.save()
        return redirect('listar_vendedores')

    return render(request, 'vendedores/novo_vendedor.html', {'form': form})



@login_required
def vendedor_delete(request, id):
    vendedores = get_object_or_404(Vendedores, pk=id)

    if request.method == 'POST':
        vendedores.delete()
        return redirect('listar_vendedores')

    return render(request, 'vendedores/del_confirm_vendedor.html', {'vendedores': vendedores})

