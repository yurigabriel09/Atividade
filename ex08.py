import requests

nomePais = input('Digite o nome do pais (em inglês): ')

url = f'https://restcountries.com/v3.1/name/{nomePais}'
res = requests.get(url)

if res.status_code == 200:
    dados = res.json()

    fronteira = dados[0]['borders']
    moedas = dados[0]['currencies']
    codigo_moeda = list(moedas.keys())[0]
    linguagem = dados[0]['languages']
    cod_linguagem = list(linguagem.keys())[0]
    
    print(f'Nome do país: {dados[0]['name']['common']}')

    print(f'Capital do país: {dados[0]['capital'][0]}')

    print(f'Países que fazem fronteira: ')
    for i in range(len(fronteira)):
        print(fronteira[i], end=' / ')

    print(f'\nInformações da moeda: {codigo_moeda} / {moedas[codigo_moeda]['symbol']} / {moedas[codigo_moeda]['name']}')

    print(f'Região: {dados[0]['region']}')
    print(f'Subregião: {dados[0]['subregion']}')
    print(f'Linguagem: {linguagem[cod_linguagem]}')

else:
    print('Erro. Verifique o nome do país digitado e tente novamente.')