#valor da compra
compra = float(input('Digite o valor da compra: '))

#fazer o desconto de quinze por cento
preço_com_desconto = (compra * 15/100)

#valor final
preço_final = compra - preço_com_desconto
print('o valor final da compra com o desconto é: ', preço_final, 'reais')