# maior <- 0
maior = 0
# menor <- 0
menor = 0
# para controle de 1 ate 10 faca
for controle in range(1, 11):
    # escreva("Digite um numero: ")
    # leia(numero)
    numero = int(input("Digite um numero: "))
    # se (controle = 1) entao
    if controle == 1:
        # menor <- numero
        menor = numero
    # fimse
    # se (numero > maior) entao
    if numero > maior:
        # maior <- numero
        maior = numero
    # fimse
    # se (numero < menor) entao
    if numero < menor:
        # menor <- numero
        menor = numero
    # fimse
# fimpara
# escreva("O maior número informado é:", maior)
print('O maior numero informado é:', maior)
# print("O menor número informado é:", menor)
print('O menor numero informado é:', menor)
