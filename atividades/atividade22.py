# soma <- 0
soma = 0
# cont18 <- 0
cont18 = 0
# cont5 <- 0
cont5 = 0
# maior_idade <- 0
maior_idade = 0
# para controle de 1 ate 10 faca
for controle in range(1, 11):
    # escreva("Informe a idade: ")
    # leia(idade)
    idade = int(input("Informe a idade: "))
    # soma <- soma + idade
    soma = soma + idade
    # se (idade > 18) entao
    if idade > 18:
        # cont18 <- cont18 + 1
        cont18 = cont18 + 1
    # senao
    # se (idade < 5) entao
    elif idade < 5:
        # cont5 <- cont5 + 1
        cont5 = cont5 + 1
    # fimse
    # se (idade > maior_idade) entao
    if idade > maior_idade:
        # maior_idade <- idade
        maior_idade = idade
    # fimse
# fimpara
# media <- soma / 10
media = soma / 10
# escreval("A média das idades é:", media)
print("A média das idades é:", media)
# escreval("A quantidade de pessoas com mais de 18 anos é:", cont18)
print("A quantidade de pessoas com mais de 18 anos é:", cont18)
# escreval("A quantidade de pessoas com menos de 5 anos é:", cont5)
print("A quantidade de pessoas com menos de 5 anos é:", cont5)
# escreva("A maior idade é:", maior_idade)
print("A maior idade é:", maior_idade)