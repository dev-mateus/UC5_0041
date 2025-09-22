import os  # Importa o módulo os para comandos do sistema operacional
from main import Item, ListaCompras  # Importa as classes Item e ListaCompras do arquivo main.py


class Menu:
    """Classe responsável pelo menu interativo."""

    def __init__(self):
        """Inicializa o dicionário de listas de compras."""
        self.listas = {}

    def limpar_tela(self):
        """Limpa a tela do terminal conforme o sistema operacional."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def exibir_menu(self):
        """Exibe e controla o menu interativo."""
        while True:
            self.limpar_tela()
            print("\n--- MENU LISTA DE COMPRAS ---")
            print("1. Criar nova lista")
            print("2. Adicionar item à lista")
            print("3. Remover item da lista")
            print("4. Listar itens da lista")
            print("5. Salvar lista em arquivo")
            print("6. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                nome = input("Nome da nova lista: ")
                self.listas[nome] = ListaCompras(nome)
                print(f"Lista '{nome}' criada.")
                input("Pressione ENTER para continuar...")
            elif opcao == '2':
                nome = input("Nome da lista: ")
                if nome in self.listas:
                    item_nome = input("Nome do item: ")
                    try:
                        quantidade = int(input("Quantidade: "))
                    except ValueError:
                        print("Quantidade deve ser um número inteiro.")
                        input("Pressione ENTER para continuar...")
                        continue
                    self.listas[nome].adicionar_item(Item(item_nome, quantidade))
                    print("Item adicionado.")
                else:
                    print("Lista não encontrada.")
                input("Pressione ENTER para continuar...")
            elif opcao == '3':
                nome = input("Nome da lista: ")
                if nome in self.listas:
                    item_nome = input("Nome do item para remover: ")
                    self.listas[nome].remover_item(item_nome)
                    print("Item removido (se existia).")
                else:
                    print("Lista não encontrada.")
                input("Pressione ENTER para continuar...")
            elif opcao == '4':
                nome = input("Nome da lista: ")
                if nome in self.listas:
                    print(f"Itens da lista '{nome}':")
                    self.listas[nome].listar_itens()
                else:
                    print("Lista não encontrada.")
                input("Pressione ENTER para continuar...")
            elif opcao == '5':
                nome = input("Nome da lista: ")
                if nome in self.listas:
                    self.listas[nome].salvar_em_arquivo()
                    print("Lista salva em arquivo.")
                else:
                    print("Lista não encontrada.")
                input("Pressione ENTER para continuar...")
            elif opcao == '6':
                print("Saindo...")
                break
            else:
                print("Opção inválida.")
                input("Pressione ENTER para continuar...")


if __name__ == "__main__":
    menu = Menu()
    menu.exibir_menu()
