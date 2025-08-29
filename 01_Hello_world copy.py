import tkinter as tk

janela = tk.Tk()
janela.title("SUPER BOM DIA")
janela.geometry("800x600+100+50")
janela.resizable(False, False)

janela.configure(bg="#FACADA")


label = tk.Label(janela, 
                 text="Qual o seu nome?",
                 bg="red",
                 font="papyrus",
                 foreground="blue")

##

label_b_dia = tk.Label (janela, 
                        text = f"",
                        font= ("Arial", 30),
                        foreground = "pink")



campo_texto = tk.Entry(janela)

nome_digitado = campo_texto.get
#função do botao

def desejar_bom_dia():
    """Essa função pega o nome digitado na caixa de texto de deseja um bom dia"""

#botao

botao = tk.Button (janela, text="clique em mim!")






#COLOCANDO ICONE
janela.iconbitmap("icon/adobe.ico")


label.pack()
botao.pack()
campo_texto.pack()
label_b_dia.pack(pady=20)
janela.mainloop()


