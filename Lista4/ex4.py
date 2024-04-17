divisor = int(input('Entre o valor do divisor: '))
inicioIntervalo = int(input('Inicio do intervalo: '))
finalIntervalo = int(input('Final do intervalo: '))

print(f'Números divisíveis por {divisor} no intervalo de {inicioIntervalo} a {finalIntervalo}')

for num in range(inicioIntervalo,  finalIntervalo + 1):
    if num % divisor == 0:
        print(num)