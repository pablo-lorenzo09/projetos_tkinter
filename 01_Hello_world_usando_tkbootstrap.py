import ttkbootstrap as tk

class Janela_principal():
    """Classe para a criação da janela principal"""

    def __init__(self):

        self.janela = tk.Window(themename="vapor")

        janela.title("SUPER BOM DIA")
        janela.geometry("800x600+100+50")
        janela.resizable(False, False)

        janela.configure(bg="black")


        label = tk.Label(janela, 
                        text="Qual o seu nome?",
                        font=("Arial", 30),
                        foreground="white"
        )

        ##

        label_b_dia = tk.Label (janela, 
                                text = f"",
                                font= ("Arial", 30),
                                foreground = "white")



        campo_texto = tk.Entry(janela)



        #botao

        botao = tk.Button (janela, 
                        text="clique em mim!",
                        command= desejar_bom_dia,
                        style="danger")



        #COLOCANDO ICONE
        janela.iconbitmap("icon/adobe.ico")


        label.pack()
        campo_texto.pack()
        botao.pack()
        label_b_dia.pack(pady=20)

    def run():
        """Executa a janela"""
        #Loop da janela
        janela.mainloop()


    #função do botao
    def desejar_bom_dia():
        """Essa função pega o nome digitado na caixa de texto de deseja um bom dia"""
        
        nome = campo_texto.get()
        label_b_dia.configure(text=f"Bom dia, {nome}!")