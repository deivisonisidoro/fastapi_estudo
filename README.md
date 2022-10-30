# CAT42 - ICMS ST

Este projeto tem como objetivo fazer a leitura de arquivos xml

## Criando Ambiente de Virtual

Para iniciar a api na sua maquina é recomentado ter um ambiente virtual, para criar o ambiente use o comando:

`python -m venv .\venv`

Para ativar a virtual env no windows use o comando:

`venv\Scripts\activate`

no linux:

`source venv/bin/activate`

## Instalando dependências

Para instalar as dependências do projeto é necessário usar o comando:

`pip install -r requirements.txt`

## Iniciando o servidor

Para iniciar o servidor é necessário usar o comando:

`uvicorn main:app --reload`

## Banco de dados

Usamos o alembic como forma de controle de migrações, e temos que rodar dois comandos para adicionar uma nova revisão, e executar essa revisão

## Gerando revisão

Use o comando:

`alembic revision --autogenerate -m "Texto descrevendo revisão"`

## Executando revisão

use o comando:

`alembic upgrade head`
