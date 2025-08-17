def main():
    valores = []

    while True:
        try:
            n = float(input("Digite um valor (ou -1 para encerrar): "))
            if n == -1:
                break
            valores.append(n)
        except ValueError:
            print("Valor inválido, digite um número.")

    if len(valores) == 0:
        print("Nenhum valor foi informado.")
        return

    quantidade = len(valores)
    soma = sum(valores)
    media = soma / quantidade
    acima_media = sum(1 for v in valores if v > media)

    print(f"\nQuantidade de valores lidos: {quantidade}")

    print("Valores na ordem informada:", end=" ")
    for v in valores:
        print(v, end=" ")
    print()

    print("Valores na ordem inversa:", end=" ")
    for v in reversed(valores):
        print(v, end=" ")
    print()

    print(f"Soma dos valores: {soma}")
    print(f"Média dos valores: {media:.2f}")
    print(f"Quantidade de valores acima da média: {acima_media}")

if __name__ == "__main__":
    main()
