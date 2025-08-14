# escreva("O primeiro valor: ")
# leia(primeiro)
primeiro = int(input("O primeiro valor: "))
# escreva("O ultimo valor: ")
# leia(ultimo)
ultimo = int(input("O ultimo valor: "))
# escreva("O incremento: ")
# leia(incremento)
incremento = int(input("O incremento: "))
# se (primeiro <= ultimo) entao
if primeiro <= ultimo:
    # enquanto primeiro <= ultimo faca
    while primeiro <= ultimo:
        # escreva(primeiro)
        print(primeiro)
        # primeiro <- primeiro + incremento
        primeiro += incremento
    # fimenquanto
# senao
else:
    # enquanto primeiro >= ultimo faca
    while primeiro >= ultimo:
        # escreva(primeiro)
        print(primeiro)
        # primeiro <- primeiro - incremento
        primeiro -= incremento
    # fimenquanto
# fimse
# escreva(" Acabou!")
print(" Acabou!")
