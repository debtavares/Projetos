from django.db import models

# Create your models here.
def index(request):
    return render(request, 'index.html')

class Empresa(models.Model):
    nome = models.CharField(max_length=200)
    cnpj = models.CharField(max_length=18, unique=True)
    endereco = models.TextField()

    def __str__(self):
        return self.nome

class Fornecedor(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='fornecedores')
    nome = models.CharField(max_length=200)
    cnpj = models.CharField(max_length=18, unique=True)
    endereco = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.nome