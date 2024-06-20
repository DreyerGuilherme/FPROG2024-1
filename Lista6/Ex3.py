import random

def testar_dado_viciado(N):
    # inicializar um array com 6 posições para contar os resultados de cada face do dado
    resultados = [0] * 6

    # lançar o dado N vezes
    for _ in range(N):
        lance = random.randint(1, 6)  # Sorteia um número entre 1 e 6
        resultados[lance - 1] += 1

    # calcular e imprimir o percentual de cada face
    print("O percentual de cada face é: ")
    for i in range(6):
        percentual = (resultados[i] / N) * 100
        print(f"Face {i + 1}: {percentual:.2f}%")

# ler o número de lançamentos do usuário
N = int(input("Digite o número de lançamentos do dado: "))

# testar se o dado é viciado
testar_dado_viciado(N)