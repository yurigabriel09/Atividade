def quantidade_notas_cem(dinheiro):
    notas_cem = dinheiro // 100
    resto = dinheiro % 100
    print(f'{notas_cem} nota(s) de R$ 100,00')
    quantidade_notas_cinquenta(resto)

def quantidade_notas_cinquenta(resto):
    notas_cinquenta = resto // 50
    resto = resto % 50
    print(f'{notas_cinquenta} nota(s) de R$ 50,00')
    quantidade_notas_dez(resto)

def quantidade_notas_dez(resto):
    notas_dez = resto // 10
    resto = resto % 10
    print(f'{notas_dez} nota(s) de R$ 10,00')
    quantidade_notas_cinco(resto)

def quantidade_notas_cinco(resto):
    notas_cinco = resto // 5
    resto = resto % 5
    print(f'{notas_cinco} nota(s) de R$ 5,00')
    quantidade_notas_um(resto)

def quantidade_notas_um(resto):
    notas_um = resto
    print(f'{notas_um} nota(s) de R$ 1,00')

def main():
    try:
        dinheiro = int(input('Informe a quantia em dinheiro (entre 10 e 600): '))
        if 10 <= dinheiro <= 600:
            quantidade_notas_cem(dinheiro)
        else:
            print('Valor inválido! Digite um valor entre 10 e 600 reais.')
    except ValueError:
        print('Por favor, insira um valor numérico válido.')

if __name__ == '__main__':
    main()
