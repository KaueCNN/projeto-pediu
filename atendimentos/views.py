from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import AtendimentoForm, CompraForm


# Create your views here.


@login_required
def novo_atendimento(request):
    form = AtendimentoForm(request.POST or None, request.FILES or None, initial={"status": "C"})

    if form.is_valid():
        form.save()
        return redirect('novo_atendimento')

    return render(request, 'novo_atendimento.html', {'form': form})


@login_required
def nova_compra(request):
    form = CompraForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('novo_atendimento')

    return render(request, 'nova_compra.html', {'form': form})