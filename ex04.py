def aplicar_prova():
    gabarito = ['A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'E']
    respostas = []

    print("Responda as 10 questões (letras maiúsculas de A a E):")
    for i in range(10):
        while True:
            resposta = input(f"Questão {i+1}: ").strip().upper()
            if resposta in ['A', 'B', 'C', 'D', 'E']:
                respostas.append(resposta)
                break
            else:
                print("Resposta inválida. Digite A, B, C, D ou E.")

    acertos = sum(1 for i in range(10) if respostas[i] == gabarito[i])
    print(f"Você acertou {acertos} questão(ões).")
    return acertos

def main():
    acertos_alunos = []

    while True:
        acertos = aplicar_prova()
        acertos_alunos.append(acertos)

        outro = input("Deseja registrar outro aluno? (S/N): ").strip().upper()
        while outro not in ['S', 'N']:
            outro = input("Resposta inválida. Digite S para sim ou N para não: ").strip().upper()

        if outro == 'N':
            break

    if acertos_alunos:
        print("\nResumo final:")
        print(f"Maior número de acertos: {max(acertos_alunos)}")
        print(f"Menor número de acertos: {min(acertos_alunos)}")
        print(f"Total de alunos que utilizaram o sistema: {len(acertos_alunos)}")
    else:
        print("Nenhum aluno realizou a prova.")

if __name__ == '__main__':
    main()
