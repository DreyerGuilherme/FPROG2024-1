def divisivelPor2(num):
    if num % 2 == 0:
        return True
    else:
        return False
    
num = int(input('Digite um numero inteiro: '))
if divisivelPor2(num):
    print(num, "é divisível por 2")
else:
    print(num, "não é divisível por 2")
