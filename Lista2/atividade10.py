#ler o número de camisetas, calças e cintos
num_camisetas = int(input('Digite o número de camisetas: '))
num_calças = int(input('Digite o número de calças: '))
num_cintos = int(input('Digite o número de cintos: '))

#calcular o valor total da compra
valor_da_compra = (num_camisetas * 25) + (num_calças * 100) + (num_cintos * 40)

#calcular o preço com desconto
valor_com_desconto = valor_da_compra - (valor_da_compra *10/100)

#exibir o valor do desconto e o preço com desconto
print('O valor do desconto é: R$ ', valor_da_compra * 10/100)
print('O preço com desconto é: R$ ', valor_com_desconto)