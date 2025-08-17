def calcular_conceito(media):
    if 9.0 <= media <= 10.0:
        return 'A'
    elif 7.5 <= media < 9.0:
        return 'B'
    elif 6.0 <= media < 7.5:
        return 'C'
    elif 4.0 <= media < 6.0:
        return 'D'
    else: 
        return 'E'

def main():
    try:
        nota1 = float(input('Digite a primeira nota: '))
        nota2 = float(input('Digite a segunda nota: '))

        if not (0 <= nota1 <= 10 and 0 <= nota2 <= 10):
            print("As notas devem estar entre 0 e 10.")
            return

        media = (nota1 + nota2) / 2
        conceito = calcular_conceito(media)

        print(f'\nNota 1: {nota1:.1f}')
        print(f'Nota 2: {nota2:.1f}')
        print(f'Média: {media:.1f}')
        print(f'Conceito: {conceito}')

        if conceito in ['A', 'B', 'C']:
            print('APROVADO')
        else:
            print('REPROVADO')

    except ValueError:
        print("Por favor, digite valores numéricos válidos.")

if __name__ == '__main__':
    main()
