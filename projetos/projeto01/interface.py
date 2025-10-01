from imc import calcula_imc
from frequencia_cardiaca import calcula_frequencia_cardiaca
from gasto_calorico import calcula_gasto_calorico


def menu():
    while True:
        print('=========== menu ===========')
        print('1 - IMC')
        print('2 - Frequencia cardiaca')
        print('3 - Gasto calorico')
        print('0 - Sair')

        opcao = int(input('Informe a opção desejada: '))

        if opcao == 0:
            break
        elif opcao == 1:
            in_peso = input('Informe seu peso em Kg: ')
            in_altura = input('Infome sua altura em m: ')
            calcula_imc(in_peso, in_altura)
        else:
            print('Opção inválida!')

menu()