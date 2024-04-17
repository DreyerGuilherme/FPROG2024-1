import random

numeroSorteado = random.randint(1, 10)
tentativas = 3

for i in range(tentativas):
    chute = int(input('Tente adivinhar o número enter 1 e 10: '))
    if chute < numeroSorteado:
        print('O número sorteado é maior que o digitado.')
    elif chute > numeroSorteado:
        print('O número sorteado é menor do que o digitado.')
    else:
        print('Parabéns! Você acertou o número.')
        break
else:
    print('Você esgotou suas tentativas. O número sorteado era: ', numeroSorteado)