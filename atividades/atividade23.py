# par <- 0
par = 0
# impar <- 0
impar = 0
# para controle de 1 ate 6 faca
for controle in range(1, 7):
    # escreva("Digite um numero:")
    # leia(numero)
    numero = int(input("Digite um numero:"))
    # se (numero mod 2 = 0) entao
    if numero % 2 == 0:
        # par <- par + 1
        par = par + 1
    # senao
    else:
        # impar <- impar + 1
        impar = impar + 1
    # fimse
# fimpara
# escreval("A quantidade de numero par é:", par)
print("A quantidade de numero par é:", par)
# escreva("A quantidade de numero impar é:", impar)
print("A quantidade de numero impar é:", impar)
