# define os vetores v1, v2 e v3
v1 = [1, 5, 9, 2, 5]
v2 = [7, 4, 13, 21, 6]
v3 = [8, -3, 5, 7, 12]

# criar a matriz M
M = [v1, v2, v3]

# multiplicar todos os elementos da matriz por 7
for i in range(len(M)):
    for j in range(len(M[i])):
        M[i][j] *= 7

# imprimir a matriz M após a multiplicação
print("Matriz M após a multiplicação por 7:")
print("[")
for linha in M:
    print(" ", linha)
print("]")