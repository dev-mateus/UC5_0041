class Alunos:
    def __init__(self, nome, ra, email):
        self.nome = nome
        self.ra = ra
        self.email = email
        self.notas = []

    def adicionar_nota(self, nota):
        self.notas.append(nota)
    
    def exibir_media(self):
        if len(self.notas) == 0:
            print("Não há notas para calcular a média")
        else:
            media = sum(self.notas) / len(self.notas)
            print(f'A média é: {media:.2f}')
    
    def exibir_informacoes(self):
        print(f'Nome: {self.nome}\nRA: {self.ra}\nEmail: {self.email}\nNotas: {self.notas}')


#testes
aluno1 = Alunos('Diego', '122356', '1223562senacminas.edu.br')
aluno1.exibir_informacoes()
aluno1.exibir_media()

aluno1.adicionar_nota(4.2)
aluno1.adicionar_nota(4.8)
aluno1.exibir_informacoes()
aluno1.exibir_media()