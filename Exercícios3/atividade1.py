#escreva dois números do ussuário
a = float(input('Escreva o primeiro número: '))
b = float(input('Escreva o segundo número: '))

#verifique se o divisor não é zero
if b != 0:

#faça a divisão
    resultado = a / b
    print(f'O resultado da divisão é {resultado}.')
else:
#escreva uma mensagem de erro
    print('Erro: A divisão por 0 não é permitida.')
    