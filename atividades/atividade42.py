class Jogador:
    def __init__(self, nome, posicao, idade):
        self.nome = nome
        self.posicao = posicao
        self.idade = idade
    
    def __str__(self):
        return f'---------------------\nNome: {self.nome}\nPosição: {self.posicao}\nIdade: {self.idade}'

class Time:
    def __init__(self, nome, cidade):
        self.nome = nome
        self.cidade = cidade
        self.jogadores = []

    def adicionar_jogador(self, jogador: Jogador):
        self.jogadores.append(jogador)
    
    def total_jogadores(self):
        print(f'---------------------\nTotal de Jogadores: {len(self.jogadores)}')
    
    def media_idade(self):
        
        soma = 0
        for jogador in self.jogadores:
            soma += jogador.idade
        media = soma / len(self.jogadores)
        
        print(f'---------------------\nMédia de idade do time {self.nome} é {media}')
    
    def listar_jogadores(self):
        print(f'---------------------\nLista de jogadores do time {self.nome}')
        for jogador in self.jogadores:
            print(jogador)
            


#teste
jogador1 = Jogador("João", "Atacante", 25)
jogador2 = Jogador("Pedro", "Defensor", 30)
jogador3 = Jogador("Lucas", "Meio-campo", 22)
jogador4 = Jogador("Carlos", "Goleiro", 28)
jogador5 = Jogador("Rafael", "Atacante", 27)

time = Time("A", "Cidade X")
time.adicionar_jogador(jogador1)
time.adicionar_jogador(jogador2)
time.adicionar_jogador(jogador3)
time.adicionar_jogador(jogador4)
time.adicionar_jogador(jogador5)
time.total_jogadores()
time.media_idade()
time.listar_jogadores()