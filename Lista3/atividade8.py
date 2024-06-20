def calcular_preco_venda():
    produto_preco = float(input("Digite o preço do produto: "))

    if produto_preco < 20:
        lucro_porcentagem = 45
    elif produto_preco <= 50:
        lucro_porcentagem = 35
    else:
        lucro_porcentagem = 25

    lucro_valor = (produto_preco * lucro_porcentagem) / 100
    preco_venda = produto_preco + lucro_valor

    print(f"O preço de venda do produto é: R$ {preco_venda:.2f}")

if __name__ == "__main__":
    calcular_preco_venda()