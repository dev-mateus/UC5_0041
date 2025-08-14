# escreva("Informe o salario: R$")
# leia(salario)
salario = float(input("Informe o salario: R$"))
# se (salario <= 1900) entao
if salario <= 1900:
    # imposto <- salario * 0
    imposto = salario * 0
# senao se (salario <= 2800) entao
elif salario <= 2800:
    # imposto <- salario * 0.075
    imposto = salario * 0.075
# senao se (salario <= 3700) entao
elif salario <= 3700:
    # imposto <- salario * 0.15
    imposto = salario * 0.15
# senao
else:
    # imposto <- salario * 0.225
    imposto = salario * 0.225
# fimse
# escreva("Imposto é: R$", imposto)
print("Imposto é: R$", imposto)
