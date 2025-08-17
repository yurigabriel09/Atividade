def alcool():
    quantidade = float(input('Informe quantos litros deseja: '))
    preco_por_litro = 1.90

    if quantidade <= 20:
        preco = (quantidade * preco_por_litro) * (1 - 0.03)
    else:
        preco = (quantidade * preco_por_litro) * (1 - 0.05)
        
    print(f'Preço  a pagar: {preco}')


def gasolina():
    quantidade = float(input('Informe quantos litros deseja: '))
    preco_por_litro = 2.50

    if quantidade <= 20:
        preco = (quantidade * preco_por_litro) * (1 - 0.04)
    else:
        preco = (quantidade * preco_por_litro) * (1 - 0.06)

    print(f'Preço  a pagar: {preco}')

if __name__ == '__main__':
    while True:
        combustivel = input('Informe "A" para álcool e "G" para gasolina: ')

        if(combustivel.upper() != 'A' and combustivel.upper() != 'G'):
            print('Informe um valor válido!')
        else:
            if combustivel.upper() == 'A':
                alcool()
                break
            else:
                gasolina()
                break
    