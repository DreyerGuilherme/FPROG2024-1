# A) Gerar e escrever todos os números inteiro do intervalo [0,100]

for i in range(101):
    print(i)

# B) Gerar e escrever os números pares do intervalo [20,50]

for i in range(20, 51):
    if i % 2 == 0:
        print(i)

# C) Gerar e escrever os números inteiros do intervalo [25,70] em ordem descrescente

for i in range(70, 24, -1):
    print(i)

# D) Gerar e escrever os números ímpares do intervalo [25,95] em ordem descrescente

for i in range(95, 24, -1):
    if i % 2 != 0:
        print(i)

# E) Ler 15 números e escrever a soma e a média dos números lidos

soma = 0
for i in range(15):
    num = int(input("Digite um número: "))
    soma += num
print("A soma dos números é: ")
print("A média dos números é: ", soma / 15)

# F) Ler 10 números inteiros e escrever a quantidade de números pares e a quantidade de números ímpares lidos

qntPares = 0
qntImpares = 0

for i in range(10):
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        qntPares += 1
    else:
        qntImpares += 1
print("A quantidade de números pares é: ", qntPares)
print("A quantidade de números ímpares é: ", qntImpares)

# G) Sortear 20 números inteiros entre -10 e 10 e imprimi-los acompanhados da mensagem "POSITIVO", "NEGATIVO" ou "NULO", conforme o caso. No final, imprimir  a quantidade de números positivos e  negativos lidos

import random
qntPositivos = 0
qntNegativos = 0
for i in range(20):
    num = random.randint(-10, 10)
    if num > 0:
        print(num, "POSITIVO")
        qntPositivos += 1
    elif num < 0:
        print(num, "NEGATIVO")
        qntNegativos += 1
    else:
        print(num, "NULO")
print("A quantidade de números positivos é: ", qntPositivos)
print("A quantidade de números negativos é: ", qntNegativos)

# H) Ler n números e imprimir no final a soma dos números lidos (obs: n é a quantidade de números que deverão ser lidos e também deve ser lido no teclado)

n = int(input("Digite a quantidade de números a serem lidos: "))
soma = 0
for i in range(n):
    num = int(input("Digite um número: "))
    soma += num
print("A soma dos números é:  ", soma)