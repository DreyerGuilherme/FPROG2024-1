import random

# Peça ao usuário que escolha uma opção (PAR ou ÍMPAR)
option = input("Você escolhe PAR ou ÍMPAR? ")

# Peça ao usuário que digite um número entre 0 e 5
number = int(input("Digite um número entre 0 e 5: "))

# Gerar um número aleatório entre 0 e 5
random_number = random.randint(0, 5)

# Imprimir o número aleatório
print(f"O número aleatório é {random_number}.")

# Calcule a soma dos números
sum_numbers = number + random_number

# Imprima a soma dos números
print(f"A soma dos números é {sum_numbers}.")

# Verifique se a soma dos números é par ou ímpar
if (option == "PAR" and sum_numbers % 2 == 0) or (option == "ÍMPAR" and sum_numbers % 2 != 0):
    print("Você venceu!")
else:
    print("O programa venceu!")
