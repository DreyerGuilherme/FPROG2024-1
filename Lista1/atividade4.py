# Pergunta
pergunta = "Qual é o verdadeiro nome do super-herói Batman?"

# Resposta correta
resposta_correta = 'a'

# Opções
opcoes = [
    "a) Bruce Wayne",
    "b) Clark Kent",
    "c) Peter Parker",
    "d) Tony Stark",
    "e) Steve Rogers",
]

# Imprime a pergunta
print(pergunta)

# Armazena as opções
for i, opcao in enumerate(opcoes, 1):
    print(f"{i}) {opcao}")

# Solicita ao usuário que digite sua resposta
resposta_usuario = input("Digite sua resposta: ")

# Exibe a resposta do usuário e a resposta correta
print(f"Você respondeu a alternativa {resposta_usuario}. ")
if resposta_usuario == resposta_correta:
    print("Muito bem, a resposta correta é a alternativa a.")
else:
    print(f"A resposta correta é a alternativa {resposta_correta}.")