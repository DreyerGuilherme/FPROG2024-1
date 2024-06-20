import numpy as np

# definir o tamanho da matriz
num_alunos = 10
num_graus = 2  # Grau A e Grau B

# gerando notas aleatórias para Grau A e Grau B
notas_grau_a = np.random.uniform(0.0, 10.0, (num_alunos, 1))
notas_grau_b = np.random.uniform(0.0, 10.0, (num_alunos, 1))

# calculando a média das notas para Grau Parcial
notas_parcial = (notas_grau_a + notas_grau_b) / 2.0

# unindo as matrizes de Grau A, Grau B e Grau Parcial em uma única matriz
matriz_notas = np.hstack((notas_grau_a, notas_grau_b, notas_parcial))

# exibindo a matriz gerada
print("Matriz 10x3 com notas:")
print(matriz_notas)