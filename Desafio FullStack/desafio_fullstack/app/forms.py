from django import forms
from .models import Empresa, Fornecedor

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['nome', 'cnpj', 'endereco']

class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = ['empresa', 'nome', 'cnpj', 'endereco', 'email']