# Validador de Senha (salvar como atividade27)
# Descrição: O sistema solicita uma senha ao usuário e
# só permite o acesso se ela atender a critérios (mínimo de caracteres, presença de números, etc.).
# O usuário tem 3 tentativas.
contador = 3
while True:
    contador = contador - 1
    senha = input('Informe a senha: ')
    if len(senha) >= 8 and not senha.isdigit() and not senha.isalpha():
        print('Senha aceita')
        break
    elif contador == 0:
        print('Senha bloqueada')
        break

    print('Tente novamente, você tem', contador, 'tentativas!')
