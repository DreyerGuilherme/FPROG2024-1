x = int(input("Digite o número de alunos: "))
media_geral = 0

for i in range(x):
    grau_A = float(input("Digite a nota do grau A: "))
    grau_B = float(input("Digite a nota do grau B: "))
    media = (grau_A * 1/3) + (grau_B * 2/3)

    if media >= 6:
        print("APROVADO")
    else:
        grau_C = float(input("Digite a nota do grau C: "))
        escolha = input("Qual nota deseja substituir (A ou B)? ").upper()
        if escolha == "A":
            grau_A = grau_C
        elif escolha == "B":
            grau_B = grau_C
        else:
            print("Opção inválida")
            continue
        media = (grau_A * 1/3) + (grau_B * 2/3)
        if media >= 6:
            print("APROVADO")
        else:
            print("REPROVADO")
    media_geral += media

media_geral /= x
print("Média geral dos alunos: ", media_geral)