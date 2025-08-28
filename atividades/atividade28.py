# Tabuada Interativa (salvar como atividade28)
# Descrição: O usuário escolhe um número e o programa exibe a tabuada de 1 a 10. Após isso,
# pergunta se deseja ver outra tabuada.
# Conceitos trabalhados: for, while, input(), if.
while True:
    numero = int(input("Informe um número: "))
    for i in range(1, 11):
        resultado = numero * i
        print(i, "x", numero, "=", resultado)
    entrada = input("Digite [S] se deseja ver outra tabuada: ")
    if entrada != 'S':
        break

