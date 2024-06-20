#informe um número inteiro
número = int(input('Digite um número inteiro: '))

#verifique se o número é divisível por 3
if número % 3 == 0:
    print(f'{número} é divisível por 3')
else:
    print(f'{número} não é divisível por 3')