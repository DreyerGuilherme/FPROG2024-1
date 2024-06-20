#algoritmo que pede a cotação do dólar, quantidade de dólares que o turista quer comprar e calcula o valor total em reais

#definir a variável para a cotação do dólar
cotacao_dolar = 5.00

#solicitar ao usuário que digite a quantidade de dólares que ele quer comprar
quantidade_dolares = float(input('Digite a quantidade de dólares que você quer comprar: '))

#calcular o valor total a ser pago pelo turista em reais
valor_total = quantidade_dolares * cotacao_dolar

#exibir o resultado
print(f'Valor total a ser pago em reais: R${valor_total:.2f}')