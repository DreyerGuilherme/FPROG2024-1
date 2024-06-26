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
    "Poção de Cura": {"Pó de Fênix": 30, "Essência Celestial": 20, "Flores secas": 20, "Lágrimas de unicórnio": 10},
    "Poção Força da Floresta": {"Orvalho Lunar": 20, "Raiz de Dragão": 30, "Flores secas": 30},
    "Poção Sabedoria da Riqueza": {"Essência Celestial": 30, "Pó de Fênix": 50},
    "Poção Sorte no Amor": {"Orvalho Lunar": 10, "Flores secas": 50, "Lágrimas de unicórnio": 5},
    "Poção Malvada": {"Elixir amargo": 10, "Raiz de Dragão": 15}
}

# Função para exibir os ingredientes disponíveis
def consultar_ingredientes():
    print("Ingredientes disponíveis:")
    print("----------------------------------------")
    for ingrediente, quantidade in ingredientes.items():
        print(f"{ingrediente}: {quantidade}")
        print("----------------------------------------")

# Função para preparar uma poção
def preparar_pocao(nome_pocao):
    if nome_pocao not in poções:
        print("Poção não encontrada!")
        return

    ingredientes_necessarios = poções[nome_pocao]
    ingredientes_faltando = []
    for ingrediente, quantidade_necessaria in ingredientes_necessarios.items():
        if ingrediente not in ingredientes or ingredientes[ingrediente] < quantidade_necessaria:
            ingredientes_faltando.append(ingrediente)

    if len(ingredientes_faltando) > 0:
        print("Falta de ingredientes:")
        print(len(ingredientes_faltando))
        for ingrediente in ingredientes_faltando:
            print(ingrediente)
    else:
        for ingrediente, quantidade_necessaria in ingredientes_necessarios.items():
            ingredientes[ingrediente] -= quantidade_necessaria
        print("Poção criada com sucesso!")

# Função principal
def main():
    while True:
        print("\nMenu:")
        print("1. Preparar poção")
        print("2. Consultar ingredientes disponíveis")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("----------------------------------------")
            nome_pocao = input("Digite o nome da poção a ser preparada: ")
            preparar_pocao(nome_pocao)
            print("----------------------------------------")
        elif opcao == "2":
            consultar_ingredientes()
        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()