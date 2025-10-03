import datetime

class Autor:
    def __init__(self, nome, nacionalidade, ano_nascimento):
        self.nome = nome
        self.nacionalidade = nacionalidade
        self.ano_nascimento = ano_nascimento
    
    def apresentacao(self):
        print(f'Meu nome é {self.nome}, sou um autor {self.nacionalidade} e nasci no ano de {self.ano_nascimento}')

class Livro:
    def __init__(self, titulo, ano_publicacao, autor: Autor):
        self.titulo  = titulo
        self.ano_publicacao = ano_publicacao
        self.autor = autor
    
    def exibir_informacoes(self):
        print(f'Título: {self.titulo}\nAno: {self.ano_publicacao}\nNome do Autor: {self.autor.nome}')
    
    def idade_do_livro(self):
        idade = datetime.datetime.now().year - self.ano_publicacao
        print(f'O livro {self.titulo} tem {idade} anos de publicação.')

# testes
autor1 = Autor('Diego', 'brasileiro', 2007)
autor1.apresentacao()
livro1 = Livro('Teste 000', 2004, autor1)
livro1.idade_do_livro()
