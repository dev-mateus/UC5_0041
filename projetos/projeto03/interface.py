import customtkinter
from main import Tarefa, ListaTarefas

class Interface:
    def __init__(self):
        customtkinter.set_appearance_mode('dark')
        customtkinter.set_default_color_theme('dark-blue')

        self.janela = customtkinter.CTk()
        self.janela.geometry('600x500')
        self.janela.title('Tarefas')

        self.frame_listas = customtkinter.CTkFrame(self.janela)
        self.frame_listas.pack(pady=10, padx=10, fill='both')
        self.frame_listas.grid_columnconfigure(0,weight=1)
        self.frame_listas.grid_columnconfigure(1,weight=0)

        self.frame_tarefas = customtkinter.CTkFrame(self.janela)

        self.frame_opcoes_tarefas = customtkinter.CTkFrame(self.janela)

        self.entrada_nova_lista = customtkinter.CTkEntry(self.frame_listas, placeholder_text='Crie uma nova lista', width=220)
        self.entrada_nova_lista.grid(row=0, column=0, padx=10, pady=10, sticky='we')

        botao_adicionar_lista = customtkinter.CTkButton(self.frame_listas, text='CRIAR', command=lambda: [self.criar_frame_lista()])
        botao_adicionar_lista.grid(row=0, column=1, padx=10, pady=10)

    def criar_frame_lista(self):
        self.objeto_lista = ListaTarefas(self.entrada_nova_lista.get())
        
        self.frame_tarefas.destroy()
        self.frame_opcoes_tarefas.destroy()

        self.frame_tarefas = customtkinter.CTkFrame(self.janela)
        self.frame_tarefas.pack(pady=10, padx=10, fill='both', expand=True)
        self.frame_tarefas.grid_columnconfigure(0,weight=1)
        self.frame_tarefas.grid_columnconfigure(1,weight=0)

        self.frame_opcoes_tarefas = customtkinter.CTkFrame(self.janela)
        self.frame_opcoes_tarefas.pack(pady=10, padx=10)

        self.label_nome_lista = customtkinter.CTkLabel(self.frame_tarefas, text=self.objeto_lista.nome_lista, font=customtkinter.CTkFont(size=20, weight='bold'))
        self.label_nome_lista.grid(row=0, column=0, padx=10, pady=10, columnspan=2, sticky='we')

        self.entrada_nova_tarefa = customtkinter.CTkEntry(self.frame_tarefas, placeholder_text='Adicione uma nova a tarefa', width=220)
        self.entrada_nova_tarefa.grid(row=1, column=0, padx=10, pady=10, sticky='we')

        self.botao_adicionar_tarefa = customtkinter.CTkButton(self.frame_tarefas, text='ADICIONAR', command=lambda: self.criar_widgets_tarefa(self.entrada_nova_tarefa.get()))
        self.botao_adicionar_tarefa.grid(row=1, column=1, padx=10, pady=10)

        self.botao_listar_pendentes = customtkinter.CTkButton(self.frame_opcoes_tarefas, text='Listar Tarefas Pendentes', command=lambda: self.mostrar_tarefas_pendentes())
        self.botao_listar_pendentes.grid(row=0, column=0, padx=10, pady=10, sticky='e')

        self.botao_salvar_arquivo = customtkinter.CTkButton(self.frame_opcoes_tarefas, text='Salvar Lista em Arquivo', command=lambda: self.objeto_lista.salvar_em_arquivo())
        self.botao_salvar_arquivo.grid(row=0, column=1, padx=10, pady=10, sticky='w')

        self.entrada_nova_lista.delete(0, 'end')
        self.frame_tarefas.focus()


    def criar_widgets_tarefa(self, argumento):
        self.objeto_tarefa = Tarefa(argumento)
        self.objeto_lista.adicionar_tarefa(self.objeto_tarefa)
        self.nova_tarefa = customtkinter.CTkCheckBox(self.frame_tarefas, text=argumento, command=lambda tarefa=self.objeto_tarefa: self.marcar_desmarcar_tarefa(tarefa))
        self.nova_tarefa.grid(column=0, padx=10, pady=1, columnspan=2, sticky='we')
        self.entrada_nova_tarefa.delete(0, 'end')
    
    def marcar_desmarcar_tarefa(self, tarefa):
        if tarefa.concluida is False:
            tarefa.concluir()
        else:
            tarefa.concluida = False
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