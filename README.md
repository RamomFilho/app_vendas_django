# API Django

Utilizando Django como API com as seguintes ferramentas:

- Banco de dados PostgreSQL 10.+


## Instalação
Preparação de ambiente da aplicação.
Para aplicação é indicado rodar em um ambiente isolado, uma [virtualenv](https://docs.python.org/pt-br/dev/library/venv.html).
Requisitos:

* Python 3.6+


Com o ambiente virtual ativado instale as dependências com o seguinte comando no terminal:
```shell
$ pip install -r requirements.txt
```

## Criação do banco de dados
É necessário que você possua o banco de dados PostgreSQL instaladado em sua máquina. [Downlaod](https://www.postgresql.org/download/)
Com o PostgreSQL instalado é necessário criar um banco com o nome 'app_vendas'.
Com usuário e senha postgres, ou alterar no arquivo settings.py na variavel 'DATABASES', os seus parametros de acordo com suas credenciais.



## Como executar o projeto

Vamos executar os comandos abaixo partindo que esteja no diretório raiz onde fez o clone do projeto.
Crie um superadmin para acessar o django admin.
```sh
python manage.py migrate
python manage.py createsuperuser
python mange.py runserver
```


### Inserindo Dados Endpoints REST

Para criar uma entrada no banco iremos utilizar o path abaixo em algum aplicativo como Postman ou Insomnia
#####Inserindo Cliente
```sh
http://localhost:8000/custumer/
```

Via metódo POST, passaremos o corpo do objeto JSON a ser inserido
## Requisição
```json
{
    "name": "Ramom"
}
```
## Resposta
```json
{
  "id": 1,
  "name": "Ramom"
}
```
#####Inserindo Vendedor
```sh
http://localhost:8000/seller/
```

Via metódo POST, passaremos o corpo do objeto JSON a ser inserido
## Requisição
```json
{
    "name": "Amanda"
}
```
## Resposta
```json
{
  "id": 1,
  "name": "Amanda"
}
```

#####Inserindo um produto
```sh
http://localhost:8000/product/
```

Via metódo POST, passaremos o corpo do objeto JSON a ser inserido
## Requisição
```json
    {
        "name": "Shampoo",
        "price": 5.0,
        "commission": 0.05
    }
```
## Resposta
```json
[
    {
        "id": 1,
        "name": "Shampoo",
        "price": 5.0,
        "commission": 0.05
    }
]
```

#####Inserindo uma venda
```sh
http://localhost:8000/sale/
```

Via metódo POST, passaremos o corpo do objeto JSON a ser inserido
## Requisição
```json
    {
        "seller": 1,
        "custumer": 1,
        "status": false,
        "itens": [
            {
               "quantity": 1,
                "sale": 1,
                "product": 1
            }
        ]
    }
```
## Resposta
```json
{
    "id": 1,
    "seller": 1,
    "custumer": 1,
    "status": false,
    "date": "2021-05-17T19:22:30.830721-03:00",
    "itens": [
        {
            "id": 1,
            "quantity": 1,
            "sale": 2,
            "product": 1
        }
    ]
}
```

#####Inserindo uma Item de linha(Repesenta a lista de Itens selecionados para venda)
Relacionamento da venda com os produtos
```sh
http://localhost:8000/lineitem/
```

Via metódo POST, passaremos o corpo do objeto JSON a ser inserido
## Requisição
```json
    {
        "quantity": 1,
        "sale": 1,
        "product": 1
    }
```
## Resposta
```json
{
    "id": 1,
    "quantity": 5,
    "sale": 1,
    "product": 1
}
```