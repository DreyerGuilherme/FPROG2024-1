def matriz_identidade(n):
    # inicializar a matriz como uma lista de listas
    matriz = [[0] * n for _ in range(n)]
    
    # preencher a diagonal principal com 1
    for i in range(n):
        matriz[i][i] = 1
    
    return matriz

# gerar e imprimir a matriz identidade 4x4
matriz_4x4 = matriz_identidade(4)
print("Matriz Identidade 4x4:")
for linha in matriz_4x4:
    print(linha)