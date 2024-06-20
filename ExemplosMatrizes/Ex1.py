import random

# Função que imprime os elementos de uma matriz, 
def imprimirVetor(V):
    n = len(V)
    for i in range(n):
        print(V[i], end= ' ')

#------------------------------------------------------------------------------------

# Criação de uma matriz com 3 linhas e 4 colunas - matriz 3 x 4

      #0  1  2  3
M = [ [1, 2, 3, 4],     # 0
      [5, 6, 7, 8],     # 1
      [9, 10, 11, 12]]  # 2

print(M)

print(len(M))

print(len(M[0]))




nLinhas = len(M)
nColunas = len(M[0])

# Percorrendo (fazendo a varredura) a matriz utilizando os índices de linha e coluna
for l in range(nLinhas):
    for c in range(nCOlunas):
        # Dentro do contexo do segundo for, podemos acessar o elemento com índice e linha e coluna
        print(M[l][c], end=' ')
        # .. pode ter mais comandos aqui!
      #dentro do contexto do primeiro for, podemos fazer operações utilizando a linha inteira
    print()


# ler do usuario o nro de linhas e colunas que a matriz tera













#criação de um array vazio
vet = []

# ler do usuario do nro de elementos do array
n = int(input('Digite o nro de elementos do array: '))

# preencher o vetor com numeros lidos do usuario
for i in range(n):
    #ler o valor e armazenar no elemento em uma variavel
    valor = int(input('Digite o valor do elemento: '))
    vet.append(valor)

    imprimirVetor(vet)