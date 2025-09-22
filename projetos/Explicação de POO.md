## Revisão dos Projetos 02, 03 e 04: Conceitos de Programação Orientada a Objetos

Os projetos (Lista de Compras, Gerenciador de Tarefas e Controle de Estoque/Biblioteca) utilizam **Programação Orientada a Objetos (POO)**, um paradigma que organiza o código em torno de entidades chamadas **objetos**.

### Conceitos Fundamentais

#### 1. Classes
Uma **classe** é um molde (ou modelo) que define as características e comportamentos de um tipo de objeto. Ela descreve quais dados (atributos) e ações (métodos) os objetos daquele tipo terão.

Exemplo:
```python
class Item:
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade
```
Aqui, `Item` é uma classe que representa um produto de uma lista de compras.

#### 2. Atributos
**Atributos** são as variáveis que pertencem a uma classe ou a seus objetos. Eles armazenam o estado do objeto.

Exemplo:
- `nome` e `quantidade` são atributos da classe `Item`.

#### 3. Métodos
**Métodos** são funções definidas dentro de uma classe, que representam comportamentos dos objetos.

Exemplo:
```python
def __str__(self):
    return f'{self.nome} - {self.quantidade}'
```
O método `__str__` retorna uma representação em texto do objeto.

#### 4. Objetos e Instâncias
Um **objeto** (ou instância) é uma ocorrência concreta de uma classe, com valores próprios para seus atributos.

Exemplo:
```python
item1 = Item("Arroz", 2)
```
Aqui, `item1` é um objeto da classe `Item`.

### Aplicação nos Projetos

#### Projeto 02 - Lista de Compras
- Classes: `Item` e `ListaCompras`
- Objetos representam itens e listas de compras.
- Métodos permitem adicionar, remover, listar e salvar itens.

#### Projeto 03 - Gerenciador de Tarefas
- Classes: Provavelmente `Tarefa` e uma classe para gerenciar tarefas.
- Objetos representam tarefas individuais.
- Métodos para cadastrar, listar, marcar como concluída e salvar tarefas.

#### Projeto 04 - Controle de Estoque/Biblioteca
- Classes: `Leitor`, `Livro`, `Emprestimo`
- Objetos representam leitores, livros e empréstimos.
- Métodos para cadastrar, consultar, atualizar, remover e registrar empréstimos/devoluções.

### Resumo

A **POO** facilita a organização do código, tornando-o mais modular, reutilizável e fácil de manter. Cada projeto utiliza classes para modelar entidades do mundo real, atributos para armazenar dados e métodos para definir comportamentos. Objetos são criados a partir dessas classes, permitindo manipular dados e executar ações de forma estruturada e intuitiva.