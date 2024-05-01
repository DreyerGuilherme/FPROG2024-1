import random

def sorteio(inicio, fim):
    return random.randint(inicio, fim)

numSorteado = sorteio(1, 10)
print('O número sorteado é: ', numSorteado)