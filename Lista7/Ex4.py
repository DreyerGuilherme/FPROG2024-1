import random

def preencher_matriz_aleatoria(num_linhas, num_colunas, min_value, max_value):
    matriz = []
    for i in range(num_linhas):
        linha = [random.randint(min_value, max_value) for _ in range(num_colunas)]
        matriz.append(linha)
    return matriz

def soma_segunda_linha(matriz):
    # somar os elementos da segunda linha (índice 1)
    soma = sum(matriz[1])
    return soma

def soma_quinta_coluna(matriz):
    # somar os elementos da quinta coluna (índice 4)
    soma = sum(matriz[i][4] for i in range(len(matriz)))
    return soma

def soma_multiplicacao_primeira_quarta_linha(matriz):
    # calcular a multiplicação dos elementos da primeira linha pelos elementos da quarta linha
    multiplicacao = 0
    for j in range(len(matriz[0])):
        multiplicacao += matriz[0][j] * matriz[3][j]
    return multiplicacao

def soma_colunas_indices_pares(matriz):
    # somar os elementos das colunas com índices pares
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if j % 2 == 0:
                soma += matriz[i][j]
    return soma

def soma_linhas_indices_impares(matriz):
    # somar os elementos das linhas com índices ímpares
    soma = 0
    for i in range(len(matriz)):
        if i % 2 != 0: 
            soma += sum(matriz[i])
    return soma

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

# calcular e imprimir as somas solicitadas
print("\nSomas:")
print("a. Soma dos elementos da segunda linha:", soma_segunda_linha(matriz))
print("b. Soma dos elementos da quinta coluna:", soma_quinta_coluna(matriz))
print("c. Soma da multiplicação dos elementos da primeira linha pelos elementos da quarta linha:",
      soma_multiplicacao_primeira_quarta_linha(matriz))
print("d. Soma dos elementos das colunas com índices pares:", soma_colunas_indices_pares(matriz))
print("e. Soma dos elementos das linhas com índices ímpares:", soma_linhas_indices_impares(matriz))