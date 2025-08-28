# Calculadora de Média com Validação (salvar como atividade29)
# Descrição: O aluno cria um programa que solicita 4 notas entre 0 e 10. Se o valor for inválido,
# o sistema pede novamente. Ao final, exibe a média e uma mensagem de aprovação ou reprovação.
# Conceitos trabalhados: while, if, float, input().
soma = 0
for i in range(1, 5):
    while True:
        nota = float(input(f'Informe a nota {i}: '))
        if 0 <= nota <= 10:
            soma += nota
            break
media = soma / 4
print(f'A média é: {media}')
if media < 7:
    print('Reprovado')
else:
    print('Aprovado')
