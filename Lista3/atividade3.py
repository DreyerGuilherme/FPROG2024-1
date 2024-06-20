#leia um número do usuário
número = float(input('Digite um número: '))

#verifique se o número é positivo ou negativo
if número > 0:
    #o número é positivo, encontre seu dobro
    resultado = número * 2
    print(f'O dobro de {número} é {resultado}')
else:
    #o número é negativo, encontre seu triplo
    resultado = número * 3
    print(f'o triplo de {número} é {resultado}.')