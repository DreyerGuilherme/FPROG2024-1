def contar_letras_e_palavras(frase):

#  Esta função recebe uma frase como entrada e retorna um dicionário com a quantidade total de letras e palavras na frase.

  #Argumentos:
    #frase (str): A frase a ser analisada.
    
  #Retorna:
   # dict: Um dicionário com as chaves 'letras' e 'palavras', contendo os valores correspondentes à quantidade de letras e palavras na frase.

  numero_de_letras = 0
  numero_de_palavras = 0

  for caractere in frase:
    if caractere.isalpha():
      numero_de_letras += 1
  
  palavras = frase.split()
  numero_de_palavras = len(palavras)

  return {'letras': numero_de_letras, 'palavras': numero_de_palavras}

def main():
  
  #Esta função solicita ao usuário uma frase, chama a função 'contar_letras_e_palavras' para obter a contagem de letras e palavras e imprime o resultado na tela.

  frase = input("Digite uma frase: ")
  contagem = contar_letras_e_palavras(frase)

  print(f"A frase '{frase}' possui:")
  print(f"- {contagem['letras']} letras")
  print(f"- {contagem['palavras']} palavras")

if __name__ == "__main__":
  main()