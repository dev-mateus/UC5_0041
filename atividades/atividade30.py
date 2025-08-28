#  Menu de Operações Matemáticas (salvar como atividade30)
# Descrição: Criar um menu com opções de soma, subtração, multiplicação, divisão e sair.
# O usuário escolhe a operação e insere os números.
# Conceitos trabalhados: while, if, elif, break, float
while True:
    opcao = input('Informe:\n 1 - Adição\n 2 - Subtração\n 3 - Multiplicação\n 4 - Divisão\n 5 - Sair\n')
    if opcao == '5':
        print('Tchauu!')
        break
    numero1 = float(input('Informe o primeiro: '))
    numero2 = float(input('Informe o segundo: '))
    if opcao == '1':
        print(f'{numero1} + {numero2} = {numero1 + numero2}')
    elif opcao == '2':
        print(f'{numero1} - {numero2} = {numero1 - numero2}')
    elif opcao == '3':
        print(f'{numero1} * {numero2} = {numero1 * numero2}')
    elif opcao == '4' and numero2 != 0:
        print(f'{numero1} / {numero2} = {numero1 / numero2}')
