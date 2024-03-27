def converter_moedas():
    real = 1

    dolar = float(input("Digite a cotação do dólar em relação ao real: "))
    euro = float(input("Digite a cotação do euro em relação ao real: "))

    while True:
        print("""
        1 - Converter de Real para Euro
        2 - Converter de Real para Dólar
        3 - Converter de Euro para Dólar
        4 - Converter de Euro para Real
        5 - Converter de Dólar para Euro
        6 - Converter de Dólar para Real
        0 - Sair
        """)

        opcao = int(input("Escolha uma opção: "))

        if opcao == 0:
            break

        if opcao == 1:
            valor_real = float(input("Digite o valor em real: "))
            valor_euro = valor_real / euro
            print(f"O valor em euro é: {valor_euro:.2f}")

        elif opcao == 2:
            valor_real = float(input("Digite o valor em real: "))
            valor_dollar = valor_real / dolar
            print(f"O valor em dólar é: {valor_dollar:.2f}")

        elif opcao == 3:
            valor_euro = float(input("Digite o valor em euro: "))
            valor_dollar = valor_euro / dolar
            print(f"O valor em dólar é: {valor_dollar:.2f}")

        elif opcao == 4:
            valor_euro = float(input("Digite o valor em euro: "))
            valor_real = valor_euro * euro
            print(f"O valor em real é: {valor_real:.2f}")

        elif opcao == 5:
            valor_dollar = float(input("Digite o valor em dólar: "))
            valor_euro = valor_dollar * dolar
            print(f"O valor em euro é: {valor_euro:.2f}")

        elif opcao == 6:
            valor_dollar = float(input("Digite o valor em dólar: "))
            valor_real = valor_dollar * dolar
            print(f"O valor em real é: {valor_real:.2f}")

        else:
            print("Opção inválida")

if __name__ == "__main__":
    converter_moedas()