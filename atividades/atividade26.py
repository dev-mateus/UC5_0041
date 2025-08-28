# Script python para resolver a seguinte atividade
# Jogo de Adivinhação (salvar como atividade26)
# Descrição: O programa escolhe um número aleatório entre 1 e 100.
# O aluno deve implementar a lógica para que o usuário tente adivinhar o número, recebendo dicas
import random
aleatorio = random.randint(1, 100)
while True:
    numero = int(input('Digite um numero: '))
    if numero == aleatorio:
        print('ACERTOU!')
        break
    elif numero < aleatorio:
        print('ERROU! Tente um número maior')
    else:
        print('ERROU! Tente um número menor')
