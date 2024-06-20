import random

def preencher_matriz_aleatoria(num_linhas, num_colunas, min_value, max_value):
    matriz = []
    for i in range(num_linhas):
        linha = [random.randint(min_value, max_value) for _ in range(num_colunas)]
        matriz.append(linha)
    return matriz

def encontrar_maior_valor(matriz):
    # inicializar o maior valor com o primeiro elemento da matriz
    maior = matriz[0][0]

    # percorrer a matriz para encontrar o maior valor
    for linha in matriz:
        for elemento in linha:
            if elemento > maior:
                maior = elemento

    return maior

def encontrar_menor_valor(matriz):
    # inicializar o menor valor com o primeiro elemento da matriz
    menor = matriz[0][0]

    # percorrer a matriz para encontrar o menor valor
    for linha in matriz:
        for elemento in linha:
            if elemento < menor:
                menor = elemento

    return menor

# definir os parâmetros da matriz
num_linhas = 4
num_colunas = 6
min_value = -10
max_value = 10

# preencher a matriz com valores aleatórios
matriz = preencher_matriz_aleatoria(num_linhas, num_colunas, min_value, max_value)

# imprimir a matriz
print("Matriz 4x6 gerada:")
for linha in matriz:
    print(linha)

# incontrar o maior e o menor valor da matriz
maior_valor = encontrar_maior_valor(matriz)
menor_valor = encontrar_menor_valor(matriz)

# imprimir o maior e o menor valor da matriz
print("\nMaior valor da matriz:", maior_valor)
print("Menor valor da matriz:", menor_valor)