# escreva("Informe o valor do produto: ")
# leia(valorProduto)
valorProduto = float(input("Informe o valor do produto: "))
# se (valorProduto <= 100) entao
if valorProduto <= 100:
    # escreva("Produto sem desconto")
    print("Produto sem desconto")
# senao
else:
    # valorComDesconto <- valorProduto - valorProduto * 0.1
    valorComDesconto = valorProduto - valorProduto * 0.1
    # escreva("Valor com desconto: ", valorComDesconto)
    print("Valor com desconto: ", valorComDesconto)
# fimse
