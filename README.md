# Bookstore API

API REST para gerenciamento de livraria desenvolvida com Django e Django REST Framework.

## Requisitos

- Docker
- Docker Compose

## Instalação

1. Clone o repositório:

   ```bash
   git clone <url-do-repositorio>
   cd bookstore
   ```

2. Inicie os containers:

   ```bash
   docker-compose up -d
   ```

3. Acesse a aplicação:
   - Backend: http://localhost:8000
   - Admin Django: http://localhost:8000/admin

## Comandos Úteis

- Parar os containers: `docker-compose down`
- Ver logs: `docker-compose logs -f`
- Recriar containers: `docker-compose up --build -d`
- Acessar shell do container: `docker-compose exec backend bash`

## Estrutura do Projeto

- `bookstore/`: Configurações do Django
  - `settings.py`: Configurações do Django
  - `urls.py`: URLs principais
  - `wsgi.py`/`asgi.py`: Configurações de servidor
- `order/`: Módulo de pedidos
  - `models/`: Modelos de dados de pedidos
  - `serializers/`: Serializadores para API REST
  - `viewsets/`: Views da API REST
- `product/`: Módulo de produtos
  - `models/`: Modelos de dados de produtos
  - `serializers/`: Serializadores para API REST
  - `viewsets/`: Views da API REST

## Configuração de Ambiente

O projeto utiliza variáveis de ambiente para configuração:

- `DEBUG=1`: Modo desenvolvimento ativado
- `DJANGO_ALLOWED_HOSTS`: Hosts permitidos (localhost, 127.0.0.1, 0.0.0.0)
- `SQL_ENGINE`: Banco de dados SQLite para desenvolvimento
- `SECRET_KEY`: Chave de desenvolvimento

## Solução de Problemas

### Erro "you must have settings.ALLOWED_HOSTS if DEBUG is false"

Esse erro ocorre quando o Django está em modo produção (DEBUG=False) sem hosts permitidos configurados. A solução está no docker-compose.yml com as variáveis de ambiente corretas.

### Banco de dados

Para desenvolvimento, o projeto usa SQLite. Para produção, configure as variáveis de ambiente do PostgreSQL no docker-compose.yml.

## Tecnologias Utilizadas

- Python 3.12+
- Django 5.0+
- Django REST Framework 3.16+
- PostgreSQL (para produção)
- Docker & Docker Compose
- Poetry (gerenciador de dependências)
