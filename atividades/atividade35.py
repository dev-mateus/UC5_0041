# Objetivo: Criar uma função que gere um número aleatório e permita ao usuário tentar adivinhar.
# Desafio extra: implementar níveis de dificuldade e contagem de tentativas.
import random


def jogo_adivinhacao(nivel = 1):
    # nível fácil
    if nivel == 1:
        tentativa = 1
        aleatorio = random.randint(1, 100)
        while True:
            print(f'{tentativa}° tentativa! - nível fácil')
            tentativa += 1
            numero = int(input('Digite um numero: '))
            if numero == aleatorio:
                print('ACERTOU!')
                nivel += 1
                break
            elif numero < aleatorio:
                print('ERROU! Tente um número maior')
            else:
                print('ERROU! Tente um número menor')
    # nível médio
    elif nivel == 2:
        tentativa = 5
        aleatorio = random.randint(1, 100)
        while tentativa >= 1:
            print(f'Restam {tentativa} tentativa(s)!  - nível médio')
            tentativa -= 1
            numero = int(input('Digite um numero: '))
            if numero == aleatorio:
                print('ACERTOU!')
                nivel += 1
                break
            elif tentativa == 0:
                print('GAME OVER')
                break
            elif numero < aleatorio:
                print('ERROU! Tente um número maior')
            else:
                print('ERROU! Tente um número menor')
    # nível díficil
    elif nivel == 3:
        tentativa = 5
        aleatorio = random.randint(1, 1000)
        while tentativa >= 1:
            print(f'Restam {tentativa} tentativa(s)!  - nível dificil')
            tentativa -= 1
            numero = int(input('Digite um numero: '))
            if numero == aleatorio:
                print('ACERTOU!')
                break
            elif tentativa == 0:
                print('GAME OVER')
                break
            elif numero < aleatorio:
                print('ERROU! Tente um número maior')
            else:
                print('ERROU! Tente um número menor')
    else:
        print('Nível inexistente')



jogo_adivinhacao(int(input('Informe o nível de dificldade:\n [1] - Fácil\n [2] - Médio\n [3] - Dificil')))
