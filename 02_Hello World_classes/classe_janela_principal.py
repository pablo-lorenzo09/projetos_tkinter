import ttkbootstrap as tk

class Janela_principal():
    """Classe para a criação da janela principal"""

    def __init__(self):
        
        self.janela = tk.Window(themename="vapor")

        self.janela.title("SUPER BOM DIA")
        self.janela.geometry("800x600+100+50")
        self.janela.resizable(False, False)

        self.janela.configure(bg="black")


        self.label = tk.Label(self.janela, 
                        text="Qual o seu nome?",
                        font=("Arial", 30),
                        foreground="white"
        )

        ##

        self.label_b_dia = tk.Label (self.janela, 
                                text = f"",
                                font= ("Arial", 30),
                                foreground = "white")



        self.campo_texto = tk.Entry(self.janela)



        #botao

        self.botao = tk.Button (self.janela, 
                        text="clique em mim!",
                        command= self.desejar_bom_dia,
                        style="danger")



        #COLOCANDO ICONE
        self.janela.iconbitmap("adobe.ico")


        self.label.pack()
        self.campo_texto.pack()
        self.botao.pack()
        self.label_b_dia.pack(pady=20)

    def run(self):
        """Executa a janela"""
        #Loop da janela
        self.janela.mainloop()


    #função do botao
    def desejar_bom_dia(self):
        """Essa função pega o nome digitado na caixa de texto de deseja um bom dia"""
        
        nome = self.campo_texto.get()
        self.label_b_dia.configure(text=f"Bom dia, {nome}!")

