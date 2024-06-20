def converter_para_maiusculas(frase):
    # utiliza o upper() para converter todas as letras minúsculas para maiúsculas
    frase_maiusculas = frase.upper()
    return frase_maiusculas

# exemplo de uso
frase_original = input("Digite uma frase: ")
frase_convertida = converter_para_maiusculas(frase_original)

print(f"Frase original: {frase_original}")
print(f"Frase em maiúsculas: {frase_convertida}")