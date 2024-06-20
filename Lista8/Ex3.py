def cebolinha(frase):
    # substituir todas as ocorrências de 'r' por 'l' na string
    frase_cebolinha = frase.replace('r', 'l')
    frase_cebolinha = frase_cebolinha.replace('R', 'L') 
    return frase_cebolinha

# exemplo de uso
frase_original = "O rato roeu a roupa do rei de Roma"
frase_cebolinha = cebolinha(frase_original)

print(f"Frase original: {frase_original}")
print(f"Frase transformada: {frase_cebolinha}")