def calcularFatorial(n):
    if n == 0:
        return 1
    else:
        return n * calcularFatorial(n-1)
    
while True:
    num = int(input('Digite um número: '))
    if num < 0:
        print('Entrada inválida. Insira um número inteiro não negativo')
    else:
        resultado = calcularFatorial(num)
        print(f'O fatorial de {num} é {resultado}')
        resposta = input('Calcular outro número (s/n)? ').lower()
        if resposta != 's':
            break

print('Adeus!')