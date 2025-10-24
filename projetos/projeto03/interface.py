# importando a biblioteca customtkinter e as classes Tarefa e ListaTarefas do módulo main
import customtkinter
from main import Tarefa, ListaTarefas

# definindo a classe Interface para criar a interface gráfica do gerenciador de tarefas
class Interface:
    def __init__(self):
        # configurando o tema da interface
        customtkinter.set_appearance_mode('dark')
        # definindo o tema de cores
        customtkinter.set_default_color_theme('dark-blue')
        # criando a janela principal
        self.janela = customtkinter.CTk()
        self.janela.geometry('600x500')
        self.janela.title('Tarefas')
        # criando o frame para as listas de tarefas
        self.frame_listas = customtkinter.CTkFrame(self.janela)
        self.frame_listas.pack(pady=10, padx=10, fill='both')
        self.frame_listas.grid_columnconfigure(0,weight=1)
        self.frame_listas.grid_columnconfigure(1,weight=0)

        # criando frames vazios para tarefas e opções de tarefas
        self.frame_tarefas = customtkinter.CTkFrame(self.janela)
        self.frame_opcoes_tarefas = customtkinter.CTkFrame(self.janela)

        # criando wigets para frame_listas
        self.entrada_nova_lista = customtkinter.CTkEntry(self.frame_listas, placeholder_text='Crie uma nova lista', width=220)
        self.entrada_nova_lista.grid(row=0, column=0, padx=10, pady=10, sticky='we')
        botao_adicionar_lista = customtkinter.CTkButton(self.frame_listas, text='CRIAR', command=lambda: [self.criar_frame_lista()])
        botao_adicionar_lista.grid(row=0, column=1, padx=10, pady=10)


    # método para criar o frame da lista de tarefas e seus widgets
    def criar_frame_lista(self):
        self.objeto_lista = ListaTarefas(self.entrada_nova_lista.get())
        # destruindo frames anteriores de tarefas e opções de tarefas, se existirem
        self.frame_tarefas.destroy()
        self.frame_opcoes_tarefas.destroy()
        # criando novos frames para tarefas e opções de tarefas
        self.frame_tarefas = customtkinter.CTkFrame(self.janela)
        self.frame_tarefas.pack(pady=10, padx=10, fill='both', expand=True)
        self.frame_tarefas.grid_columnconfigure(0,weight=1)
        self.frame_tarefas.grid_columnconfigure(1,weight=0)
        self.frame_opcoes_tarefas = customtkinter.CTkFrame(self.janela)
        self.frame_opcoes_tarefas.pack(pady=10, padx=10)
        # criando widgets para o frame de tarefas
        self.label_nome_lista = customtkinter.CTkLabel(self.frame_tarefas, text=self.objeto_lista.nome_lista, font=customtkinter.CTkFont(size=20, weight='bold'))
        self.label_nome_lista.grid(row=0, column=0, padx=10, pady=10, columnspan=2, sticky='we')
        self.entrada_nova_tarefa = customtkinter.CTkEntry(self.frame_tarefas, placeholder_text='Adicione uma nova a tarefa', width=220)
        self.entrada_nova_tarefa.grid(row=1, column=0, padx=10, pady=10, sticky='we')
        self.botao_adicionar_tarefa = customtkinter.CTkButton(self.frame_tarefas, text='ADICIONAR', command=lambda: self.criar_widgets_tarefa(self.entrada_nova_tarefa.get()))
        self.botao_adicionar_tarefa.grid(row=1, column=1, padx=10, pady=10)
        # criando botões para o frame de opções de tarefas
        self.botao_listar_pendentes = customtkinter.CTkButton(self.frame_opcoes_tarefas, text='Listar Tarefas Pendentes', command=lambda: self.mostrar_tarefas_pendentes())
        self.botao_listar_pendentes.grid(row=0, column=0, padx=10, pady=10, sticky='e')
        self.botao_salvar_arquivo = customtkinter.CTkButton(self.frame_opcoes_tarefas, text='Salvar Lista em Arquivo', command=lambda: self.objeto_lista.salvar_em_arquivo())
        self.botao_salvar_arquivo.grid(row=0, column=1, padx=10, pady=10, sticky='w')
        # limpa o texto escrito na entrada_nova_lista
        self.entrada_nova_lista.delete(0, 'end')
        self.frame_tarefas.focus()


    # método que criar os widgets de daca nova tarefa adicioanada
    def criar_widgets_tarefa(self, argumento):
        self.objeto_tarefa = Tarefa(argumento)
        self.objeto_lista.adicionar_tarefa(self.objeto_tarefa)
        self.nova_tarefa = customtkinter.CTkCheckBox(self.frame_tarefas, text=argumento, command=lambda tarefa=self.objeto_tarefa: self.marcar_desmarcar_tarefa(tarefa))
        self.nova_tarefa.grid(column=0, padx=10, pady=1, columnspan=2, sticky='we')
        self.entrada_nova_tarefa.delete(0, 'end')
    

    # método para marcar ou desmarcar uma tarefa
    def marcar_desmarcar_tarefa(self, tarefa):
        if tarefa.concluida is False:
            tarefa.concluir()
        else:
            tarefa.concluida = False

    
    # método para mostrar apenas as tarefas pendentes
    def mostrar_tarefas_pendentes(self):
        for widget in self.frame_tarefas.winfo_children():
            widget.destroy()
        
        self.label_nome_lista = customtkinter.CTkLabel(self.frame_tarefas, text=self.objeto_lista.nome_lista, font=customtkinter.CTkFont(size=20, weight='bold'))
        self.label_nome_lista.grid(row=0, column=0, padx=10, pady=10, columnspan=2, sticky='we')

        self.entrada_nova_tarefa = customtkinter.CTkEntry(self.frame_tarefas, placeholder_text='Adicione uma nova a tarefa', width=220)
        self.entrada_nova_tarefa.grid(row=1, column=0, padx=10, pady=10, sticky='we')

        self.botao_adicionar_tarefa = customtkinter.CTkButton(self.frame_tarefas, text='ADICIONAR', command=lambda: self.criar_widgets_tarefa(self.entrada_nova_tarefa.get()))
        self.botao_adicionar_tarefa.grid(row=1, column=1, padx=10, pady=10)

        linha = 2
        for tarefa in self.objeto_lista.tarefas:
            if not tarefa.concluida:
                nova_tarefa = customtkinter.CTkCheckBox(self.frame_tarefas, text=tarefa.descricao, command=lambda tarefa=tarefa: self.marcar_desmarcar_tarefa(tarefa))
                nova_tarefa.grid(row=linha, column=0, padx=10, pady=1, columnspan=2, sticky='we')
                linha += 1

if __name__ == '__main__':
    interface = Interface()
    interface.janela.mainloop()