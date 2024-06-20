import numpy as np

# gerar a matriz 5x5 de números inteiros aleatórios entre -10 e 10
matriz = np.random.randint(-10, 11, size=(5, 5))

# exibir a matriz original
print("Matriz original:")
print(matriz)

# transformar os números negativos em positivos e vice-versa
matriz_transformada = matriz * -1
# exibir a matriz transformada
print("\nMatriz transformada:")
print(matriz_transformada)