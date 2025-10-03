class Cliente:
    def __init__(self, nome, cpf, email):
        self.nome = nome
        self.cpf = cpf
        self.email = email
    
    def __str__(self):
        return f'Nome: {self.nome}\nCPF: {self.cpf}\nEmail: {self.email}'

class ContaBancaria:
    def __init__(self, numero, cliente: Cliente):
        self.numero = numero
        self.cliente = cliente
        self.saldo = 0.0

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print('Saldo insuficiente!')

    def exibir_saldo(self):
        print(f'Saldo: R$ {self.saldo}')

    def exibir_dados(self):
        print(f'Numero da conta: {self.numero}')
        print(self.cliente)

# testes
cliente1 = Cliente('João','000.111.222-44', 'joaosilva@gmail.com')
cliente2 = Cliente('Maria','999.888.777-66', 'mariadasgracas@gmail.com')

conta1 = ContaBancaria('2546', cliente1)
conta2 = ContaBancaria('7889', cliente2)
conta1.exibir_saldo()
conta1.depositar(250)
conta1.exibir_saldo()
conta1.sacar(45)
conta1.exibir_saldo()

conta1.exibir_dados()
conta2.exibir_dados()
