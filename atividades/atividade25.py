# escreva("Informe N termo de Fibonacci: ")
# leia(numero)
numero = int(input("Informe N termo de Fibonacci: "))
# fa <- 1
fa = 1
fn = 0
# para x de 1 ate numero faca
for x in range(1, numero + 1):
    # fb <- fa
    fb = fa
    # fa <- fn
    fa = fn
    # fn <- fa + fb
    fn = fa + fb
    # escreval(fn)
    print(fn)
# fimpara
