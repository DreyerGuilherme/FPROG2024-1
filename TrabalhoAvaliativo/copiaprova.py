ingredientes = {
     "Pó de Fênix": 100,
    "Essência Celestial": 50,
    "Raiz de Dragão": 45,
    "Orvalho Lunar": 30,
    "Flores secas": 200,
    "Elixir amargo": 20,
    "Lágrimas de unicórnio": 15
}

poções = {
    1: {"Pó de Fênix": 30, "Essência Celestial": 20, "Flores secas": 20, "Lágrimas de unicórnio": 10},
    2: {"Orvalho Lunar": 20, "Raiz de Dragão": 30, "Flores secas": 30},
    3: {"Essência Celestial": 30, "Pó de Fênix": 50},
    4: {"Orvalho Lunar": 10, "Flores secas": 50, "Lágrimas de unicórnio": 5},
    5: {"Elixir amargo": 10, "Raiz de Dragão": 15}
}

def consultar_ingredientes():
    print("Ingredientes disponíveis:")
    for ingrediente, quantidade in ingredientes.items():
        print(f"{ingrediente}: {quantidade}g/ml")

def preparar_pocao(numero_pocao):
    if numero_pocao not in poções:
        print("Número de poção inválido.")
        return

    ingredientes_necessarios = poções[numero_pocao]
    ingredientes_faltando = []

    for ingrediente, quantidade in ingredientes_necessarios.items():
       if ingrediente not in ingredientes or ingredientes[ingrediente] < quantidade:
           ingredientes_faltando.append(ingrediente)

           if ingredientes_faltando:
               print(f"Não é possível preparar a poção. Faltam os seguintes ingredientes: {', '.join(ingredientes_faltando)}")
           else:
               for ingrediente, quantidade in ingredientes_necessarios.items():
                   ingredientes[ingrediente] -= quantidade
print("Poção criada com sucesso!")
               
def main():
            
    while True:
        print("\nMenu:")
        print("1. Preparar poção")
        print("2. Consultar ingredientes")
        print("3. Sair")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            numero_pocao = int(input("Digite o número da poção a ser preparada: "))
            preparar_pocao(numero_pocao)
        elif opcao == 2:
            consultar_ingredientes()
        elif opcao == 3:
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
