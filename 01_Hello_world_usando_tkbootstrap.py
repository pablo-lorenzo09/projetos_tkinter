import tkinter as tk

janela = tk.Tk()
janela.title("SUPER BOM DIA")
janela.geometry("800x600+100+50")
janela.resizable(False, False)

janela.configure(bg="black")


label = tk.Label(janela, 
                 text="Qual o seu nome?",
                 bg="black",
                 font=("Arial", 30),
                 foreground="white"
)

##

label_b_dia = tk.Label (janela, 
                        text = f"",
                        bg= "black",
                        font= ("Arial", 30),
                        foreground = "white")



campo_texto = tk.Entry(janela)


#função do botao

def desejar_bom_dia():
    """Essa função pega o nome digitado na caixa de texto de deseja um bom dia"""
    nome = campo_texto.get()
    label_b_dia.configure(text=f"Bom dia, {nome}!")
#botao

botao = tk.Button (janela, text="clique em mim!",
                   command= desejar_bom_dia)






#COLOCANDO ICONE
janela.iconbitmap("icon/adobe.ico")


label.pack()
botao.pack()
campo_texto.pack()
label_b_dia.pack(pady=20)
janela.mainloop()


