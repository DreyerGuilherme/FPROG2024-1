def calcular_plano_saude():
    idade = int(input("Digite a idade do conveniado: "))
    adicional = 0

    if idade < 10:
        adicional = 100
    elif idade >= 10 and idade <= 30:
        adicional = 220
    elif idade > 30 and idade <= 60:
        adicional = 395
    else:
        adicional = 480

    if idade < 18:
        print("Valor a ser pago pelo plano de saúde: R$ 300,00")
    else:
        valor_total = 300 + adicional
        print(f"Valor a ser pago pelo plano de saúde: R$ {valor_total:.2f}")

if __name__ == "__main__":
    calcular_plano_saude()