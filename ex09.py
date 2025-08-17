import requests

siglaMoeda = input('Digite a sigla da moeda: ')

url = f'https://api.exchangerate-api.com/v4/latest/{siglaMoeda}'
res = requests.get(url)

if res.status_code == 200:
    dados = res.json()
    brl = dados['rates']['BRL']

    print(f'1 real equivale {siglaMoeda} {brl}')
else:
    print('erro')