import os
import random

def menu():
    os.system('cls' if os.name == 'nt' else 'clear') 
    print('---------------------------------------')
    print('1 - Abrir uma caixa')
    print('---------------------------------------')
    print('2 - Consultar itens')
    print('---------------------------------------')
    print('0 - Sair\n')
    item = input('Escolha uma opção: ')
    return item

def abrir_caixa(inventario):
    probabilidade = random.random()  
    if probabilidade < 0.01: 
        inventario['lendario'] += 1
        print('\nVocê coletou 1 item lendário!')
    elif probabilidade < 0.20:  
        inventario['raro'] += 1
        print('\nVocê coletou 1 item raro!')
    else:
        inventario['comum'] += 1
        print('\nVocê coletou 1 item comum!')

def consultar_itens(inventario):
    print(f'\nItens comuns: {inventario["comum"]}')
    print('---------------------------------------')
    print(f'Itens raros: {inventario["raro"]}')
    print('---------------------------------------')
    print(f'Itens lendários: {inventario["lendario"]}')

def main():
    inventario = {
        'comum': 0,
        'raro': 0,
        'lendario': 0
    }

    escolha = ''
    while escolha != '0':
        escolha = menu()
        if escolha == '1':
            abrir_caixa(inventario)
        elif escolha == '2':
            consultar_itens(inventario)
        elif escolha == '0':
            print('\nSaindo...\n')
        else:
            print('\nOpção desconhecida!\n')
        input('Pressione ENTER para continuar')

if __name__ == '__main__':
    main()