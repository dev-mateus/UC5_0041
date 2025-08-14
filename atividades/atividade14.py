# escreva("Digite um numero inteiro: ")
# leia(numero)
numero = int(input('Digite um numero inteiro: '))
# contador <- 0
contador = 0
# soma <- 0
soma = 0
# enquanto contador < numero faca
while contador < numero:
    # contador <- contador + 1
    contador += 1
    # soma <- soma + contador
    soma += contador
# fimenquanto
# escreva("A soma de 1 até", numero, " é:", soma)
print("A soma de 1 até", numero, " é:", soma)
