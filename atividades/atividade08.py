# escreva("Digite seu salário :R$")
# leia(salario_inicial)
salario_inicial = float(input('Digite seu salário :R$'))
# se salario_inicial < 1500 entao
if salario_inicial < 1500:
    # aumento <- 0.2
    aumento = 0.2
# senao
else:
    # aumento <- 0.1
    aumento = 0.1
# fimse
# salario_final = salario_inicial + salario_inicial * aumento
salario_final = salario_inicial + salario_inicial * aumento
# escreva("Salário após o aumento: R$",salario_final)
print(f'Salário após o aumento: R${salario_final}')
