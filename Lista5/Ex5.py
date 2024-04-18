import os

def menu():
  print('\n..:: Desenvolvendo programas com menus ::..\n')
  os.system('cls' if os.name == 'nt' else 'clear') 
  print('1 - Somar')
  print('2 - Subtrair')
  print('3 - Multiplicar')
  print('4 - Dividir')
  print('0 - Sair\n')
  item = input('Escolha uma opção: ')
  return item

def somar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        raise ValueError("Divisão por zero não é permitida")
    return x / y

def main():
    global num1, num2
    while True:
        try:
            num1 = float(input("Digite o primeiro número real: "))
            num2 = float(input("Digite o segundo número real: "))
            break
        except ValueError:
            print("Por favor, digite apenas números reais.")

    escolha = ''
    while(escolha != '0'):
        escolha = menu()
        if escolha == '1':
            resultado = somar(num1, num2)
        elif escolha == '2':
            resultado = subtrair(num1, num2)
        elif escolha == '3':
            resultado = multiplicar(num1, num2)
        elif escolha == '4':
            try:
                resultado = dividir(num1, num2)
            except ValueError as e:
                print(e)
                continue
        elif escolha == '0':
            print('\nSaindo...\n')
            break
        else:
            print('\nOpção desconhecida!\n')
            continue
        print(f'\nResultado: {resultado}\n')
        input('Pressione ENTER para continuar')

if __name__ == "__main__":
    main()

    ### REVISAR ###