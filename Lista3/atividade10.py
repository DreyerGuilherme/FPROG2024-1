import random

def sortear_dado(numero_faces):
    if numero_faces < 4 or numero_faces > 16:
        print("O número de faces do dado deve ser um inteiro entre 4 e 16.")
        return

    numero_sorteado = random.randint(1, numero_faces)
    print(f"O número sorteado é: {numero_sorteado}")

if __name__ == "__main__":
    numero_faces = int(input("Informe o número de faces do dado: "))
    sortear_dado(numero_faces)