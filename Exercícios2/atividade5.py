#ler o preço por litro e o valor disponível
preço_litro = float(input('Digite o preço por litro: '))
dinheiro_disponivel = float(input('Digite o  valor disponível: '))

#calcular a quantidade de litros que podem ser colocados no tanque
litros_tanque = dinheiro_disponivel / preço_litro

#exibir a quantidade de litros que podem ser colocados no tanque
print('Você pode colocar', litros_tanque, 'litros de gasolina no tanque')