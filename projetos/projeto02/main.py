import datetime  # Importa o módulo datetime para trabalhar com datas


class Item:
    """Classe que representa um item da lista de compras."""

    def __init__(self, nome, quantidade):
        """Inicializa os atributos do item."""
        self.nome = nome
        self.quantidade = quantidade

    def __str__(self):
        """Retorna uma representação em string do item."""
        return f'{self.nome} - {self.quantidade}'


class ListaCompras:
    """Classe que representa uma lista de compras."""

    def __init__(self, nome_lista):
        """Inicializa os atributos da lista de compras."""
        self.nome_lista = nome_lista
        self.data = datetime.date.today()  # Data atual do sistema
        self.itens = []  # Lista para armazenar os itens

    def adicionar_item(self, obj_item: Item):
        """Adiciona um item à lista."""
        self.itens.append(obj_item)

    def remover_item(self, nome_item):
        """Remove um item da lista pelo nome."""
        for item in self.itens:
            if item.nome == nome_item:
                self.itens.remove(item)
                break  # Remove apenas o primeiro item encontrado

    def listar_itens(self):
        """Imprime todos os itens da lista."""
        for item in self.itens:
            print(item)

    def salvar_em_arquivo(self):
        """Salva a lista de compras em um arquivo de texto."""
        nome_arquivo = f'{self.nome_lista}_{self.data}.txt'
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
            for item in self.itens:
                arquivo.write(f'{item.nome} - {item.quantidade}\n')


