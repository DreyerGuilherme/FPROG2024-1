#leia os valores A, B e C
A = float(input('Digite o valor de A: '))
B = float(input('Digite o valor de B: '))
C = float(input('Digite o valor de C: '))

#calcule as somas de A + B e A + C
soma_ab = A + B
soma_ac = A + C

#veja se a soma de A + B é menor que A + C
if soma_ab < soma_ac:
    print(f'A soma de A + B é {soma_ab}, e é menor que A + C')
else:
    print(f'A soma de A + B é {soma_ab}, e é maior ou igual a A + C.')