from django.shortcuts import render, get_object_or_404, redirect
from .models import Empresa, Fornecedor
from .forms import EmpresaForm, FornecedorForm

# ---- VIEWS PARA EMPRESA ----
def index(request):
    return render(request, 'index.html')


# Listar todas as empresas
def empresa_list(request):
    empresas = Empresa.objects.all()
    return render(request, 'empresa/empresa_list.html', {'empresas': empresas})

# Criar uma nova empresa
def empresa_create(request):
    if request.method == 'POST':
        form = EmpresaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('empresa_list')
    else:
        form = EmpresaForm()
    return render(request, 'empresa/empresa_form.html', {'form': form})

# Editar uma empresa
def empresa_update(request, pk):
    empresa = get_object_or_404(Empresa, pk=pk)
    if request.method == 'POST':
        form = EmpresaForm(request.POST, instance=empresa)
        if form.is_valid():
            form.save()
            return redirect('empresa_list')
    else:
        form = EmpresaForm(instance=empresa)
    return render(request, 'empresa/empresa_form.html', {'form': form})

# Excluir uma empresa
def empresa_delete(request, pk):
    empresa = get_object_or_404(Empresa, pk=pk)
    if request.method == 'POST':
        empresa.delete()
        return redirect('empresa_list')
    return render(request, 'empresa/empresa_confirm_delete.html', {'empresa': empresa})

# ---- VIEWS PARA FORNECEDOR ----

# Listar todos os fornecedores
def fornecedor_list(request):
    fornecedores = Fornecedor.objects.all()
    return render(request, 'fornecedor/fornecedor_list.html', {'fornecedores': fornecedores})

# Criar um novo fornecedor
def fornecedor_create(request):
    if request.method == 'POST':
        form = FornecedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fornecedor_list')
    else:
        form = FornecedorForm()
    return render(request, 'fornecedor/fornecedor_form.html', {'form': form})

# Editar um fornecedor
def fornecedor_update(request, pk):
    fornecedor = get_object_or_404(Fornecedor, pk=pk)
    if request.method == 'POST':
        form = FornecedorForm(request.POST, instance=fornecedor)
        if form.is_valid():
            form.save()
            return redirect('fornecedor_list')
    else:
        form = FornecedorForm(instance=fornecedor)
    return render(request, 'fornecedor/fornecedor_form.html', {'form': form})

# Excluir um fornecedor
def fornecedor_delete(request, pk):
    fornecedor = get_object_or_404(Fornecedor, pk=pk)
    if request.method == 'POST':
        fornecedor.delete()
        return redirect('fornecedor_list')
    return render(request, 'fornecedor/fornecedor_confirm_delete.html', {'fornecedor': fornecedor})