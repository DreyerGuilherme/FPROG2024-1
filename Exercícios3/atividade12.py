def classificar_nadador(idade):
    if idade >= 18:
        print("Sênior")
    elif idade >= 14:
        print("Juvenil B")
    elif idade >= 11:
        print("Juvenil A")
    elif idade >= 8:
        print("Infantil B")
    elif idade >= 5:
        print("Infantil A")
    else:
        print("idade invalida")

if __name__ == "__main__":
    idade = int(input("Digite a idade do nadador: "))
    classificar_nadador(idade)