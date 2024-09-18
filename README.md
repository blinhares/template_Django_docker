# Criando um Template Para Desenvolvimento de app Django com Docker

## Como

### Instalar Dependências

#### Python

As dependências do projeto serão instaladas via poetry. Logo, é necessário que a ferramenta esteja necessário.

Caso não tenha familiaridade com a ferramenta recomendo verificar este link: [Poetry](https://python-poetry.org/docs/)

Para instalar as dependencias utilizaremos o comando abaixo. O comando utiliza como base o arquivo de extenção `.toml` para instalar tudo que é necessário.

```bash
poetry install
```

*Caso haja algum problema* e o ambiente virtual não seja criado localmente, verifique as configurações do poetry [conforme documentação](https://python-poetry.org/docs/configuration/).

#### Docker

Sera nescessário ter o Docker instalado. Caso não possua, visite a [Documentação Oficial Docker](https://docs.docker.com/get-docker/)

### Criar um Django Project (já criado)

Criar um django app de nome `project` dentro da pasta `djangoapp` na raiz do projeto. O nome pode ser alterado mas deve-se ter atenção para mudar todos os arquivos mostrados a seguir.

Com o ambiente virtual ativado criamos um novo projeto com o seguinte comando:

```bash
mkdir djangoapp ;cd djangoapp/ && django-admin startproject project .

```

### Criar um Django APP

```bash
django-admin startapp djangoapp/<app_name>
```

### Arquivos de Configuração

Os arquivos de configuração ( com extensão `.env` ) vão armazenar todas as nossa variáveis de ambiente.

Veja abaixo o conteudo do arquivo `.env-example` para verificar as variáveis devidamente comentadas.

```bash
#para gerar a chave use o seguinte comando no terminal: 
#python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'

SECRET_KEY="CHANGE-ME"

# 0 False, 1 True
DEBUG="1"

# Comma Separated values
ALLOWED_HOSTS="127.0.0.1, localhost"

DB_ENGINE="django.db.backends.postgresql"
POSTGRES_DB="CHANGE-ME"
POSTGRES_USER="CHANGE-ME"
POSTGRES_PASSWORD="CHANGE-ME"
POSTGRES_HOST="localhost" #container_name do docker compose
POSTGRES_PORT="5432"
```

Duplique o arquivo, faça suas alterações e renomeie o arquivo para `.env`.

### Alterando Arquivos settings.py (já feito)

Os arquivos de configuração serão lidos tanto pelo app Django quanto pelo docker-compose. Nosso docker compose ja aponta para este arquivo, agora há que editar o `settings.py` que encontra-se em: `djangoapp/project/project/settings.py`.

Visite o arquivo para verificar as alterações.

### Criando o arquivo `requirements.txt` (já feito)

A criação do conteiner utilizar o arquivo para instalar as dependências do projeto. Para isso execute o seguinte comando:

```bash
pip freeze > djangoapp/requirements.txt
```

### Arquivos `.dockerignore` e `.gitignore`

Estes arquivos são responsáveis por ignorar os arquivos desnecessários.

### Criar Imagens Dos Conteiners

Para dar start ao projeto, vamos construir nosso contêiner através do arquivo `docker-compose.yml` dentro de `/blog_django`.

```bash
sudo docker compose up --build 
```

Se tudo for bem, agora voce deve ter dois conteiners rodando em sua maquina. E seu terminal deve mostrar isso, pois acabamos de criar conteiners em modo verboso. Para verificar basta executar o comando abaixo:

```bash
docker ps -a
```

A essa altura o projeto ja deve estar rodando no seu endereço local [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

### Pronto

Agora voce pode programar com seu ambiente de produção.
Lembre-se que sempre que for trabalhar os conteiners devem estar rodando.
Os comando docker podem ser consultados na documentação. Mas segue abaixo uma lista de comandos uteis.

#### Comando Uteis

###### Para Buildar os Conteiners

```bash
sudo docker compose up --build --force-recreate

```

###### Para Rodar o Conteiner

```bash
sudo docker compose up

```

###### Para Rodar o Conteiner em Silencio

```bash
sudo docker compose up -d

```

###### Para Desligar o Conteiner

```bash
sudo docker compose down

```

###### Executar comando dentro do Conteiner

Com o conteiner rodando, faça:

```bash
docker exec djangoapp <comando>
```

Sem o conteiner Rodando:

```bash
docker compose run --rm djangoapp  <comando>
```

Ex.:

```bash
docker exec djangoapp python -V
```

resulta em:

```bash
Python 3.12.3
```

###### Executando o comando no Shell

```Bash
docker compose run --rm djangoapp sh -c '<comando'
```

Ex.:

```Bash
docker compose run --rm djangoapp sh -c 'echo  ola'
```

###### Executando o Terminal de Modo interativo

```bash
docker exec -it djangoapp sh
```
