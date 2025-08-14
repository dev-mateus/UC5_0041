# escreva("Lado 1: ")
# leia(lado1)
lado1 = float(input('Lado 1: '))
# escreva("Lado 2: ")
# leia(lado2)
lado2 = float(input('Lado 2: '))
# escreva("Lado 3: ")
# leia(lado3)
lado3 = float(input('Lado 3: '))
# se (lado1 + lado2 > lado3) e (lado1 + lado3 > lado2) e (lado2 + lado3 > lado1)entao
if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    # se (lado1 = lado2) e (lado1 = lado3) entao
    if (lado1 == lado2) and (lado1 == lado3):
        print("Triangulo Equilátero")
    # senao se (lado1 = lado2) ou (lado2 = lado3) ou (lado3 = lado1) entao
    elif (lado1 == lado2) or (lado2 == lado3) or (lado3 == lado1):
        print("Triangulo Isósceles")
    # senao
    else:
        print("Triangulo Escaleno")
    # fimse
# senao
else:
    print("Os valores inseridos não formam um triangulo")
# fimse
