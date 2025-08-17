def main():
    cardapio = {
        100: ("Cachorro Quente", 1.20),
        101: ("Bauru Simples", 1.30),
        102: ("Bauru com ovo", 1.50),
        103: ("Hambúrguer", 1.20),
        104: ("Cheeseburguer", 1.30),
        105: ("Refrigerante", 1.00)
    }

    total_geral = 0.0

    while True:
        try:
            codigo = int(input("Digite o código do item (ou 0 para encerrar): "))
            if codigo == 0:
                break

            if codigo not in cardapio:
                print("Código inválido! Tente novamente.")
                continue

            quantidade = int(input(f"Quantidade de {cardapio[codigo][0]}: "))
            if quantidade <= 0:
                print("Quantidade deve ser maior que zero. Tente novamente.")
                continue

            nome_item, preco = cardapio[codigo]
            valor_item = preco * quantidade
            total_geral += valor_item
            print(f"{quantidade} x {nome_item} = R$ {valor_item:.2f}")

        except ValueError:
            print("Entrada inválida! Digite números inteiros para código e quantidade.")

    print(f"\nTotal a pagar: R$ {total_geral:.2f}")

if __name__ == '__main__':
    main()
