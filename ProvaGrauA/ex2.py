def divisivelPorN(a, b):
    if b == 0:
        print("Não é possível efetuar divisão por zero!")
        return False
    return a % b == 0

print('Digite o primeiro número inteiro: ')
print('Digite o segundo número inteiro: ')