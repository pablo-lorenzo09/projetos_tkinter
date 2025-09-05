import ttkbootstrap as tk

class Janela:
    def __init__(self):
        """Executa os atributos da janela"""
        self.janela = tk.Window (themename="united")
        self.janela.title ("Dr. Gastronom")
        self.janela.geometry("1000x800+450+50")
        self.janela.resizable(False, False)

        self.janela.configure(bg="white")


        self.label = tk.Label(self.janela, 
                        text="Consultório do Dr. Gastronom",
                        font=("Arial", 30),
                        foreground="black"
        )
        self.label.pack(pady=5)#

        self.label_instrução = tk.Label(self.janela,
                                        text="Faça uma pergunta referente a jantar e irei te responder",
                                        font=("Arial", 15),
                                        foreground="black")
        
        self.label_instrução.pack(pady=20)#

        self.campo_pergunta = tk.Entry(self.janela)

        self.campo_pergunta.pack()#
        
        self.campo_pergunta.place(width=900,
                                  height=50,
                                  x= 50,
                                  y=170)

        self.botao_verde = tk.Button (self.janela, 
                        text="Responder",
                        #command= self.responder_gentil,
                        style="success")

        
        self.botao_verde.pack()#
        self.botao_verde.place(x= 250,
                               y= 250,
                               width= 150,
                               height= 70)
        
        self.botao_vermelho = tk.Button (self.janela, 
                        text="Responder",
                        #command= self.responder_nao_gentil,
                        style="danger")

        
        self.botao_vermelho.pack()
        self.botao_vermelho.place(x= 450,
                                y= 250,
                                width= 150,
                                height= 70)
        
    def run(self):
        """Executa a janela"""
        #Loop da janela
        self.janela.mainloop()