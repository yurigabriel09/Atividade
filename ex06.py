def calcular_salario_atual(salario_inicial, ano_contratacao=1995, ano_atual=2025):
    aumento_percentual = 1.5  
    salario = salario_inicial

    salario += salario_inicial * (aumento_percentual / 100)

    for ano in range(1997, ano_atual + 1):
        aumento_percentual *= 2
        salario += salario * (aumento_percentual / 100)

    return salario

def main():
    try:
        entrada = input("Digite o salário inicial do funcionário em 1995 (pressione Enter para R$ 1000): ")
        if entrada.strip() == '':
            salario_inicial = 1000.0
        else:
            salario_inicial = float(entrada)
            if salario_inicial <= 0:
                print("Salário inicial deve ser maior que zero.")
                return
    except ValueError:
        print("Valor inválido. Digite um número válido para o salário.")
        return

    ano_atual = 2025 
    salario_atual = calcular_salario_atual(salario_inicial, ano_atual=ano_atual)
    print(f"Salário atual em {ano_atual}: R$ {salario_atual:.2f}")

if __name__ == "__main__":
    main()
