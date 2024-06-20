def eh_palindromo(palavra):
    # remover espaços em branco e converter para minúsculas
    palavra = palavra.replace(" ", "").lower()
    
    # verificar se a palavra é igual à sua inversa
    return palavra == palavra[::-1]

# exemplos de uso
palavra1 = "Ana"
palavra2 = "Osso"
palavra3 = "Arara"
palavra4 = "Python"

print(f"A palavra '{palavra1}' é um palíndromo? {eh_palindromo(palavra1)}")
print(f"A palavra '{palavra2}' é um palíndromo? {eh_palindromo(palavra2)}")
print(f"A palavra '{palavra3}' é um palíndromo? {eh_palindromo(palavra3)}")
print(f"A palavra '{palavra4}' é um palíndromo? {eh_palindromo(palavra4)}")