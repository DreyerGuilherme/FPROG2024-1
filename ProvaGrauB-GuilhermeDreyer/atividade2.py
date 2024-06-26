import random

def GerarToupeiras():
    matriz = [['-' for _ in range(4)] for _ in range(4)]
    
#colocar as toupeiras em lugares aleatorios
    ToupeirasColocadas = 0
    while ToupeirasColocadas < 4:
        i = random.randint(0, 3)
        j = random.randint(0, 3)
        if matriz[i][j] == '-':
            matriz[i][j] = 'T'
            ToupeirasColocadas += 1
    
    return matriz

def ImprimirMatriz(matriz):
    for linha in matriz:
        print(' '.join(linha))

if __name__ == "__main__":
    for geraçao in range(1, 4):
        print(f"Geração {geraçao}:")
        matriz = GerarToupeiras()
        ImprimirMatriz(matriz)
        print()
