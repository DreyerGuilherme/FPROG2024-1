def comparar_palavras(palavra1, palavra2):
    if palavra1 == palavra2:
        print(f"{palavra1} e {palavra2} são iguais.")
    elif palavra1 < palavra2:
        print(f"{palavra1} vem antes de {palavra2} na ordem alfabética.")
    else:
        print(f"{palavra1} vem depois de {palavra2} na ordem alfabética.")

# exemplos de uso da função
comparar_palavras("gato", "cachorro")
comparar_palavras("cachorro", "gato")
comparar_palavras("casa", "casa")