#ler a quantidade de smartphones e tablets vendidos
num_smartphones = int(input('Digite a quantidade de smartphones vendidos: '))
num_tablets = int(input('Digire a quantidade de tablets vendidos: '))

#calcule o total de dinheiro arrecadado com a venda de smartphones e tablets
valor_smartphones = num_smartphones  *1000.0
valor_tablets  = num_tablets * 1500.0
total_arrecadado = valor_smartphones + valor_tablets

#exibir o total de dinheiro arrecadado com a venda de smartphones e tablets
print('O total de dinheiro arrecadado com a venda de smartphones e tablets é: R$ ', total_arrecadado)