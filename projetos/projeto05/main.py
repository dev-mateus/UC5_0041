import customtkinter


class Interface:
    def __init__(self):
        
        self.janela = customtkinter.CTk()
        self.janela.title("Minha Janela")
        self.janela.geometry("400x300")

        self.entrada = customtkinter.CTkEntry(self.janela, placeholder_text="Digite algo aqui")
        self.entrada.pack(pady=20)

        self.botao = customtkinter.CTkButton(self.janela, text="Clique aqui", command=self.botao_clicado)
        self.botao.pack(pady=10)

        self.saida = customtkinter.CTkLabel(self.janela, text="Saída aparecerá aqui")
        self.saida.pack(pady=20)

        self.janela.mainloop()

    def botao_clicado(self):
        texto = self.entrada.get()
        self.saida.configure(text=texto)

if __name__ == "__main__":
    Interface()
