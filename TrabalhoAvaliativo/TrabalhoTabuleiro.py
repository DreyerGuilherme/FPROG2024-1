import random
import math

# Status do jogador
class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.posicao = 0
        self.relacionamento = "solteiro"
        self.fama = False
        self.num_filhos = 0
        self.status_loteria = 0
        self.perdeu_rodada = False
        self.esta_vivo = True

    def info(self):
        return f"{self.nome}: Posição {self.posicao}, Relacionamento: {self.relacionamento}, Fama: {self.fama}, Filhos: {self.num_filhos}, Status de loteria: {self.status_loteria}, Vivo: {self.esta_vivo}"

# Função para girar a roleta
def girar_roleta():
    return random.randint(1, 6)

# Função para executar ações baseadas na posição
def executa_regras(jogador):
    if jogador.posicao == 1:
        dado = girar_roleta()
        if dado == 1:
            jogador.posicao += 1
        elif dado == 3:
            jogador.posicao -= 1
        elif dado == 6:
            jogador.perdeu_rodada = True

    elif jogador.posicao == 2:
        jogador.esta_vivo = False
        print("Morreu! Game Over!!")

    elif jogador.posicao == 3:
        desafio_matematico(jogador)

    elif jogador.posicao == 4:
        formatura(jogador)

    elif jogador.posicao == 5:
        ter_filho(jogador)

    elif jogador.posicao == 6:
        casar(jogador)

    elif jogador.posicao == 7:
        ficar_famoso(jogador)

    elif jogador.posicao == 8:
        divorciar(jogador)

    elif jogador.posicao == 9:
        loteria(jogador)

    elif jogador.posicao == 10:
        casar(jogador)

    elif jogador.posicao == 11:
        resetar(jogador)

    elif jogador.posicao == 12:
        jogador.esta_vivo = False
        print("Morreu! Game Over!!")

    elif jogador.posicao == 13:
        desafio_matematico(jogador)

    elif jogador.posicao == 14:
        formatura(jogador)

    elif jogador.posicao == 15:
        ter_filho(jogador)

    elif jogador.posicao == 16:
        casar(jogador)

    elif jogador.posicao == 17:
        ficar_famoso(jogador)

    elif jogador.posicao == 18:
        divorciar(jogador)

    elif jogador.posicao == 19:
        loteria(jogador)

    elif jogador.posicao == 20:
        casar(jogador)

    elif jogador.posicao == 21:
        resetar(jogador)
        
# Desafios Matemáticos
def desafio_matematico(jogador):
    print("Desafio matemático!")
    primos_ate_100 = [x for x in range(2, 101) if all(x % y != 0 for y in range(2, x))]
    print("---------------------------------------------------------------------------")
    print(f"Números primos até 100: {primos_ate_100}")

    somatorio = sum(range(1, 11))
    print("---------------------------------------------------------------------------")
    print(f"Somatório dos números de 1 a 10: {somatorio}")

    fibonacci = [0, 1]
    while len(fibonacci) < 10:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    print("---------------------------------------------------------------------------")
    print(f"Série de Fibonacci até o 10º elemento: {fibonacci}")

    area_circulo = math.pi * 2.5 * 2.5
    print("---------------------------------------------------------------------------")
    print(f"Área de um círculo com raio 2.5: {area_circulo:.2f}")

    fatorial = math.factorial(5)
    print("---------------------------------------------------------------------------")
    print(f"Fatorial de 5: {fatorial}")

    divisiveis_por_2_5 = [x for x in range(1, 101) if x % 2 == 0 and x % 5 == 0][:5]
    print("---------------------------------------------------------------------------")
    print(f"Os 5 primeiros números divisíveis por 2 e 5: {divisiveis_por_2_5}")

# Funções relacionadas ao jogo
def formatura(jogador):
    print("---------------------------------------------------------------------------")
    print("Você se formou! Vamos ver qual curso...")
    print("---------------------------------------------------------------------------")
    curso = girar_roleta()
    cursos = {
        1: "Direito",
        2: "Medicina",
        3: "Jogos Digitais",
        4: "Segurança da Informação",
        5: "Engenharia Civil",
        6: "Administração"
    }
    print("---------------------------------------------------------------------------")
    print(f"Seu curso é: {cursos[curso]}")
    print("---------------------------------------------------------------------------")

def ter_filho(jogador):
    print("---------------------------------------------------------------------------")
    print("Você teve um filho!")
    dado = girar_roleta()
    if dado == 5:
        print("---------------------------------------------------------------------------")
        print("Você teve gêmeos!")
        jogador.num_filhos += 2
    else:
        jogador.num_filhos += 1

def casar(jogador):
    if jogador.relacionamento == "solteiro":
        print("---------------------------------------------------------------------------")
        print("Você se casou!")
        jogador.relacionamento = "casado"
    elif jogador.relacionamento == "divorciado":
        print("---------------------------------------------------------------------------")
        print("Você encontrou um novo amor e se casou novamente!")
        jogador.relacionamento = "casado"

def ficar_famoso(jogador):
    print("---------------------------------------------------------------------------")
    print("Você ficou famoso!")
    jogador.fama = True

def divorciar(jogador):
    if jogador.relacionamento == "casado":
        print("---------------------------------------------------------------------------")
        print("Você se divorciou!")
        jogador.relacionamento = "divorciado"

def loteria(jogador):
    premio = girar_roleta()
    valores = {
        1: 2.50,
        2: 5000,
        3: 50000,
        4: 500000,
        5: 5000000,
        6: 100000000
    }
    print("---------------------------------------------------------------------------")
    print(f"Você ganhou na loteria! Valor do prêmio: R$ {valores[premio]}")
    jogador.status_loteria = valores[premio]

def resetar(jogador):
    print("---------------------------------------------------------------------------")
    print("Você caiu na máquina do tempo! Tudo será resetado!")
    jogador.posicao = 0
    jogador.relacionamento = "solteiro"
    jogador.fama = False
    jogador.num_filhos = 0
    jogador.perdeu_rodada = False

# Jogo
def jogar():
    print("---------------------------------------------------------------------------")
    print("Bem-vindo ao Jogo da Vida!")
    num_jogadores = int(input("Quantos jogadores estão participando? (1 ou 2): "))

    if num_jogadores == 1:
        print("---------------------------------------------------------------------------")
        jogador1 = Jogador(input("Nome do jogador 1: "))
        jogadores = [jogador1]
    elif num_jogadores == 2:
        print("---------------------------------------------------------------------------")
        jogador1 = Jogador(input("Nome do jogador 1: "))
        print("---------------------------------------------------------------------------")
        jogador2 = Jogador(input("Nome do jogador 2: "))
        print("---------------------------------------------------------------------------")
        jogadores = [jogador1, jogador2]

    while True:
        for jogador in jogadores:
            if jogador.esta_vivo:
                if not jogador.perdeu_rodada:
                    print("---------------------------------------------------------------------------")
                    input(f"{jogador.nome}, pressione Enter para girar o dado...")
                    movimento = girar_roleta()
                    jogador.posicao += movimento
                    print("---------------------------------------------------------------------------")
                    print(f"{jogador.nome} avançou para a posição {jogador.posicao}.")
                    executa_regras(jogador)

                    if jogador.posicao >= 22:
                        print("---------------------------------------------------------------------------")
                        print(f"Parabéns, {jogador.nome}! Você atingiu a casa final!")
                        return
                else:
                    print("---------------------------------------------------------------------------")
                    print(f"{jogador.nome} perdeu uma rodada.")
                    print("---------------------------------------------------------------------------")
                    jogador.perdeu_rodada = False
                    
jogar()