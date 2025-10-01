class Lampada:
    def __init__(self, cor, potencia):
        self.cor = cor
        self.potencia = potencia
        self.ligada = False

    def ligar(self):
        self.ligada = True
    
    def desligar(self):
        self.ligada = False

    def alternar(self):
        if self.ligada is True:
            self.desligar()
        else:
            self.ligar()
    
    def status(self):
        print(self.ligada)

# testes
lampada1 = Lampada('branca', 9)
lampada1.status()

lampada1.ligar()
lampada1.status()

lampada1.desligar()
lampada1.status()

lampada1.alternar()
lampada1.status()

lampada1.alternar()
lampada1.status()