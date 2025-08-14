# escreva("Informe o capital inicial: R$")
# leia(capital)
capital = float(input("Informe o capital inicial: R$"))
# escreva("Taxa de juros a.m. (%):")
# leia(taxa)
taxa = float(input("Taxa de juros a.m. (%):"))
# escreva("Informe quantidade de meses: ")
# leia(mesFinal)
mesFinal = int(input("Informe quantidade de meses: "))
# taxa <- taxa / 100
taxa = taxa / 100
# para mes de 1 ate mesFinal faca
for mes in range(1, mesFinal + 1):
    # montante <- capital * (1 + taxa) ^ mes
    montante = capital * (1 + taxa) ** mes
    # escreval(mes, "º : R$", montante)
    print(mes, "º : R$", montante)
# fimpara
