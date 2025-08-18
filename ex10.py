# A API VIACEP NÃO FORNECE QUAL ZONA DE SÃO PAULO O CEP ESTÁ LOCALIZADO (ZONA NORTE, SUL, LESTE OU OESTE).
# PORTANTO, MAPEAMOS ALGUNS DOS BAIRROS MAIS FAMOSOS PARA CONCLUIR A ATIVIDADE.

def localizaZonas(bairro):
    zonas_sp = {
    "Centro": ["Sé", "República", "Bela Vista", "Liberdade", "Bom Retiro", "Cambuci", "Consolação", "Santa Cecília"],

    "Norte": ["Anhanguera", "Brasilândia", "Casa Verde", "Cachoeirinha", "Freguesia do Ó", "Jaçanã", "Jaraguá", "Limão", "Mandaqui", "Perus", "Pirituba", "Santana", "São Domingos", "Tremembé", "Tucuruvi", "Vila Maria", "Vila Medeiros", "Vila Guilherme"],

    "Sul": ["Morumbi", "Vila Mariana", "Campo Belo", "Jabaquara", "Moema", "Santo Amaro", "Campo Limpo", "Capão Redondo", "Vila Andrade", "Cidade Ademar", "Pedreira", "Socorro", "M'Boi Mirim", "Jardim Ângela", "Jardim São Luís", "Parelheiros", "Marsilac", "Grajaú", "Saúde", "Paraíso", "Ipiranga", "Sacomã"],

    "Leste": ["Mooca", "Tatuapé", "Vila Prudente", "São Mateus", "Brás", "Belém", "Pari", "Vila Formosa", "Itaquera", "Cidade Tiradentes", "Penha", "Aricanduva", "Carrão", "Vila Curuçá", "Itaim Paulista", "Guaianases", "Lajeado", "Vila Jacuí", "Sapopemba", "São Lucas", "São Miguel Paulista", "Vila Alpina", "Artur Alvim", "Ponte Rasa", "Ermelino Matarazzo", "Jardim Helena", "José Bonifácio"],

    "Oeste": ["Butantã", "Morumbi", "Vila Sônia", "Raposo Tavares", "Rio Pequeno", "Lapa", "Barra Funda", "Perdizes", "Vila Leopoldina", "Jaguara", "Jaguaré", "Pinheiros", "Alto de Pinheiros", "Itaim Bibi", "Jardim Paulista", "Vila Madalena"],
}
    
    for zona, bairros in zonas_sp.items():
        if bairro in bairros:
            print(f'Bairro localizado na Zona {zona} de São Paulo.')
            return


import requests

cep = input('Digite o CEP: ')

url = f'https://viacep.com.br/ws/{cep}/json/'
res = requests.get(url)

if res.status_code == 200:
    dados = res.json()
    bairro = dados['bairro']
    cidade = dados['localidade']
    
    if cidade != 'São Paulo':
        print(f'Este endereço está fora da cidade de São Paulo! Está localizado em {cidade}.')
        print(f'Bairro: {bairro}.')
    else:
        print(f'Bairro: {bairro}.')
        localizaZonas(bairro)
        
else:
    print('Erro. Verifique o CEP digitado e tente novamente.')