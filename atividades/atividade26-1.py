# soma <- 0
soma = 0
# numero <- 0
numero = 0
# repita
while True:
    # soma <- soma + numero
    soma = soma + numero
    # escreva("Informe um numero: ")
    print("Informe um numero: ")
    # leia(numero)
    numero = float(input())
    # ate numero = 0
    if numero == 0:
        break
# escreva("A soma é:", soma)
print("A soma é:", soma)
