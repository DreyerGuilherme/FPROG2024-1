print('Qual o nome verdadeiro do super-herói Batman?')

#apresente as alternativas
print('a) Bruce Wayne')
print('b) Clark Kent')
print('c) Peter Parker')
print('d) Tony Stark')
print('e) Steve Rogers')

#armazenar a alternativa correta
resposta_correta = "a"

#solicitar ao usuário que digite sua resposta
resposta_usuário = input('Digite a alternativa correspondente: ')

#exibir a resposta do usuário e a resposta correta
if resposta_usuário == resposta_correta:
    print('Você acertou! A resposta correta é a alternativa a.')
else:
    print('Você errou! A resposta correta é a alternativa a.')