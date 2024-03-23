#solicitar o peso do  prato do cliente em quilos
peso = float(input('Digite o peso do seu prato em quilos: '))

#calcular o valor a ser pago pelo cliente, considerando que o preço é de 40 reais por quilo
preço_total = peso * 40.00

print(f'O valor total a ser pago é R${preço_total:.2f}')