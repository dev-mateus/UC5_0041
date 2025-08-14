# escreva("Digite um numero inteiro positivo: ")
# leia(numero)
numero = int(input("Digite um numero inteiro positivo: "))
# enquanto numero >= 0 faca
while numero >= 0:
    # contador <- 0
    contador = 0
    # para divisor de 1 ate numero faca
    for divisor in range(1, numero + 1):
        # se (numero mod divisor = 0) entao
        if numero % divisor == 0:
            # contador <- contador + 1
            contador = contador + 1
        # fimse
    # fimpara
    # se (contador = 2) entao
    if contador == 2:
        # escreval("Numero primo")
        print("Numero primo")
    # senao
    else:
        # escreval("Numero não é primo")
        print("Numero não é primo")
    #fimse
    # escreva("Digite um numero inteiro positivo: ")
    # leia(numero)
    numero = int(input("Digite um numero inteiro positivo: "))
# fimenquanto
