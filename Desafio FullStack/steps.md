CRIAR PROJETO DJANGO

Instalar Django:
pip install django

Criar um projeto Django:
python -m django startproject desafio_fullstack
cd desafio_fullstack

Criar app Django:
python manage.py startapp app

Criar uma pasta 'templates' dentro de app com 'index.html'

Exibir Templates:
-em views.py
from django.shortcuts import render
def home(request):
    return render(request, 'app/index.html')

-em urls.py
--do app
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
]

--do projeto
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('nome_do_app.urls')),
]

Conteúdo HTML

Rodar servidor
python manage.py runserver

- As entidades são criadas em _models_. Criamos Empresa e Fornecedor. 
- Os paths em _urls_.
- _View_ é um Controller. É responsável por controlar o que acontece quando um usuário acessa uma URL.Ela recebe uma requisição (request), processa os dados e retorna uma resposta (response).
- Os _forms_ são usados para criar e validar formulários no Django.


Depois que criar modelos, criar e aplicar as migrações
python manage.py makemigrations
python manage.py migrate


Se você seguiu as boas práticas do Django e configurou corretamente as views e URLs, pode acessar o CRUD diretamente pelo navegador pelos paths configurados em urls.


PASSO A PASSO
Quando o usuário digita http://127.0.0.1:8000/empresas/, ele está fazendo uma requisição HTTP GET para o Django. 
O Django procura no urls.py uma rota que corresponda a /empresas/. No path, passamos a url e a view.

O Django encontra a view relacionado ao path /empresas/. Essa view busca os dados no banco e renderiza um template HTML para exibir os dados.

Quando o usuário clica em cadastrar uma nova, leva para a URL /empresas/cadastrar/ em urls.py, que aponta para a view criar_empresa, e redenriza o template empresa_form.html.

o Django salva a empresa no banco de dados, usando o model Empresa.