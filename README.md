# Projeto criado pelo Template Python

 O Template Python tem como proposito facilitar a criação e adaptação de automações em Python. Este template te dar uma estrutura de API com uso do [Framework FastAPI](https://fastapi.tiangolo.com/).

## Rodar Local no seu ambiente

 Os comando abaixo são assumindo que seu terminal está aberto na raiz desse projeto. 

### Criação de ambientes virtuais

A criação de ambientes virtuais é feita executando o comando `venv`. No terminal execute o comando:

```
python -m venv .venv
```


Para ativar seu ambiente virtual, execute o comando abaixo:

```
.venv\Scripts\activate
```

### Instalando bibliotecas

Com o ambiente virtual ativado, você irá fazer a instalação das bibliotecas no arquivo requirements.txt com comando abaixo:

```
pip install -r requirements.txt
```

### Rodar o projeto no localhost

#### Rodar arquivo python

```
python src\api_main.py
```

Obs: Caso esteja utilizando VScode deixamos em `.vscode\launch.json` pronto para depurar seu código.

## Rodar o dockerfile

Para rodar o docker e criar uma imagem basta usar os comandos abaixo:

1. Faça o build da imagem
```
docker build -t fastapi .
```

2. Iniciar container
```
docker run -p 5000:5000 --name template_app fastapi 
```


