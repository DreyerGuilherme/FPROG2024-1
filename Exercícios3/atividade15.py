def calcular_preco_produto(preco, condicao_pagamento):
    if condicao_pagamento == 1:
        desconto = 15
    elif condicao_pagamento == 2:
        desconto = 10
    elif condicao_pagamento in (3, 4):
        desconto = 0
    else:
        print("Código de condição de pagamento inválido!")
        return None

    preco_final = preco * (100 - desconto) // 100

    if condicao_pagamento == 3:
        print(f"Preço a ser pago em 2x: R$ {preco_final:.2f}")
    elif condicao_pagamento == 4:
        juros = preco_final * 10 // 100
        preco_final += juros
        print(f"Preço a ser pago em 3x: R$ {preco_final:.2f} (com juros de 10%)")
    else:
        print(f"Preço a ser pago: R$ {preco_final:.2f}")

preco = float(input("Digite o preço do produto: R$ "))
condicao_pagamento = int(input("Digite a codificação da condição de pagamento: "))

calcular_preco_produto(preco, condicao_pagamento)