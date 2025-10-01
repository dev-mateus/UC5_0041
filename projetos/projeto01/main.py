"""
# Projeto 01 - Calculadora de Saúde

Este projeto apresenta um menu interativo para realizar cálculos relacionados à saúde:

- **IMC (Índice de Massa Corporal)**
- **Frequência Cardíaca**
- **Gasto Calórico**

"""

class Atividade:
    def __init__(self, nome, met):
        self.nome = nome
        self.met = met

class Paciente:
    def __init__(self, peso, altura, idade):
        self.peso = peso
        self.altura = altura
        self.idade = idade

    def calcular_imc(self):
        return self.peso / (self.altura ** 2)

    def calcular_frequencia_cardiaca(self):
        
        max_frequencia_cardiaca = 220 - self.idade
        max_q_gordura = max_frequencia_cardiaca * 0.7
        min_q_gordura = max_frequencia_cardiaca * 0.5
        max_cardio = max_frequencia_cardiaca * 0.85
        min_cardio = max_frequencia_cardiaca * 0.7
        
        return f'Queima de gordura: {min_q_gordura} b.p.m. a {max_q_gordura} b.p.m.\nCardio: {min_cardio} b.p.m. a {max_cardio} b.p.m.'

    
    def calcular_gasto_calorico(self, atividade, tempo):
        return atividade * self.peso * tempo / 60
    
    def __str__(self, tempo=None, atividade=None):
        return f'Peso: {self.peso} Kg\nAltura: {self.altura} m\nIdade: {self.idade}' + \
               f'\nIMC: {self.calcular_imc():.2f}' + \
               f'\nFrequência Cardíaca:\n{self.calcular_frequencia_cardiaca()}\n' + \
                (f'Gasto Calórico: {self.calcular_gasto_calorico(atividade.met, tempo):.2f} cal' if atividade and tempo else '')
    

atividade1 = Atividade('caminhada', 3)
atividade2 = Atividade('corrida', 8.3)

paciente1 = Paciente(70, 1.75, 25)
print(paciente1)
print('------------------- Com atividade e tempo-------------------')
print(paciente1.__str__(30, atividade2))
