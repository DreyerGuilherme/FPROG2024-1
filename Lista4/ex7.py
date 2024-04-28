nomes = []

for i in range(5):
    nome = input(f"Informe o nome {i + 1}: ")
    nomes.append(nome)

nomesOrdenados = sorted(nomes)

primeiroNome = nomesOrdenados[0]

print(f"O primeiro nome em ordem alfabética é: {primeiroNome}.")