import random

# Inicializar o vetor com números sorteados de 10 a 90
v = [random.randint(10, 90) for _ in range(10)]

# imprimir o vetor
def print_vetor(vetor):
    print(vetor)

# verificar se existe o valor 50
def existe_valor_50(vetor):
    return 50 in vetor

# contar o número de ocorrências do valor 50 
def contar_ocorrencias_50(vetor):
    return vetor.count(50)

# calcular a média dos valores do vetor
def calcular_media(vetor):
    return sum(vetor) / len(vetor)

# encontrar o maior e o menor valor dos elementos 
def maior_menor(vetor):
    return max(vetor), min(vetor)

# imprimir a soma e o produto acumulado dos valores dos elementos
def soma_produto(vetor):
    soma = sum(vetor)
    produto = 1
    for num in vetor:
        produto *= num
    return soma, produto

# imprimir o vetor em ordem inversa
def imprimir_inverso(vetor):
    return vetor[::-1]

# copiar os elementos em ordem inversa para outro vetor
def copiar_inverso(vetor):
    return vetor[::-1]

# criar vetores vPares e vImpares
def separar_pares_impares(vetor):
    vPares = [x for x in vetor if x % 2 == 0]
    vImpares = [x for x in vetor if x % 2 != 0]
    return vPares, vImpares

# Executar os algoritmos
print("Vetor inicial:", v)
print_vetor(v)

print("Existe o valor 50?", "Sim" if existe_valor_50(v) else "Não")

print("Número de ocorrências do valor 50:", contar_ocorrencias_50(v))

print("Média dos valores do vetor:", calcular_media(v))

maior, menor = maior_menor(v)
print("Maior valor do vetor:", maior)
print("Menor valor do vetor:", menor)

soma, produto = soma_produto(v)
print("Soma dos valores do vetor:", soma)
print("Produto acumulado dos valores do vetor:", produto)

print("Vetor em ordem inversa:", imprimir_inverso(v))

v_inverso = copiar_inverso(v)
print("Vetor copiado em ordem inversa:", v_inverso)

vPares, vImpares = separar_pares_impares(v)
print("Vetor com elementos pares:", vPares)
print("Vetor com elementos ímpares:", vImpares)