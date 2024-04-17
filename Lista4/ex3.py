while True:
    numero = int(input('Entre com um número entre 1 e 9: '))
    if 1 <= numero <= 9:
        break
    print('Número inválido. Tente novamente.')

for i in range(1, 11):
    resultado = numero * i
    print(f'{numero} x {i} = {resultado}')

continuar = input('Calcular outro número (s/n)? ').lower()
while True:
    if continuar[0] ==  's' or continuar[0]  == 'n':
        break
    print('Resposta inválida. Tente novamente.')
    continuar =  input('Calcular outro número (s/n)? ').lower()

if continuar[0] == 's':
    while True:
        numero =  int(input('Entre com um número entre 1 e 9: '))
        if 1 <= numero <= 9:
            break
        print('Número inválido. Tente novamente.')

    for i in range(1, 11):
        resultado = numero * i
        print(f'{numero} x {i} = {resultado}')