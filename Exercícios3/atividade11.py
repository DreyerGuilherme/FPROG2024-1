def calcular_notas(valor):
    notas_disponiveis = [100, 50, 20, 10, 5, 1]
    quantidades_notas = [0] * len(notas_disponiveis)

    while valor > 0:
        for i in range(len(notas_disponiveis)):
            if valor >= notas_disponiveis[i]:
                quantidade_nota = valor // notas_disponiveis[i]
                quantidades_notas[i] = quantidade_nota
                valor -= quantidade_nota * notas_disponiveis[i]
                break

    for i in range(len(notas_disponiveis)):
        if quantidades_notas[i] > 0:
            print(f"{quantidades_notas[i]} nota(s) de R$ {notas_disponiveis[i]}")


if __name__ == "__main__":
    valor = float(input("Informe o valor a ser entregue: "))
    calcular_notas(valor)