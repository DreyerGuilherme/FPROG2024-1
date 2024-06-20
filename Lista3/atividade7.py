print('desconto_previdenciario')
salario = float(input('Digite o salário: '))
if salario * 0.11 > 318.20:
    desconto = 318.20
else:
    desconto = salario * 0.11
print('O desconto é: ', desconto)
