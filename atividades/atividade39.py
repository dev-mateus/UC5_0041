class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class Carrinho:
    def __init__(self):
        self.produtos = []
    
    def adicionar_produto(self, produto: Produto):
        self.produtos.append(produto)
    
    def total(self):
        soma = 0
        for produto in self.produtos:
            soma += produto.preco
        print(f'Total: R${soma:.2f}')
    
    def listar(self):
        for produto in self.produtos:
            print(f'{produto.nome} - R${produto.preco}')


produto1 = Produto('Arroz 5Kg', 32.99)
produto2 = Produto('Café 500g', 29.99)

carrinho1 = Carrinho()
carrinho1.adicionar_produto(produto1)
carrinho1.adicionar_produto(produto1)
carrinho1.adicionar_produto(produto1)
carrinho1.adicionar_produto(produto1)
carrinho1.adicionar_produto(produto1)
carrinho1.adicionar_produto(produto2)
carrinho1.listar()
carrinho1.total()
