def calcular_media_unisinos():
    nota_a = float(input("Digite a nota do Grau A: "))
    nota_b = float(input("Digite a nota do Grau B: "))

    media_final = (nota_a + 2 * nota_b) / 3

    print(f"Média final do aluno: {media_final:.2f}")

    if media_final >= 5.0:
        print("O aluno foi aprovado!")
    else:
        print("O aluno está em recuperação (Grau C)")

        nota_c = float(input("Digite a nota do Grau C: "))

        if nota_a < nota_b:
            nota_a = nota_c
        else:
            nota_b = nota_c

        media_final = (nota_a + 2 * nota_b) / 3

        if media_final >= 5.0:
            print(f"O aluno foi aprovado com média final de {media_final:.2f}!")
        else:
            print(f"O aluno foi reprovado com média final de {media_final:.2f}!")

if __name__ == "__main__":
    calcular_media_unisinos()