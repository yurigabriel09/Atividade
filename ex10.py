# A API VIACEP NÃO FORNECE QUAL ZONA DE SÃO PAULO O CEP ESTÁ LOCALIZADO (ZONA NORTE, SUL, LESTE OU OESTE).

import requests

cep = input('Digite o CEP: ')

url = f'https://viacep.com.br/ws/{cep}/json/'
res = requests.get(url)

if res.status_code == 200:
    dados = res.json()
    bairro = dados['bairro']
    cidade = dados['localidade']
    
    print(f'Bairro: {bairro}.')
    if cidade != 'São Paulo':
        print(f'Este endereço está fora da cidade de São Paulo! Está localizado em {cidade}.')
else:
    print('Erro')