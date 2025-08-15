import tkinter as tk



janela = tk.Tk()
janela.title("Hello world ")
label2 = tk.Label(janela, text=f"")
janela.geometry("800x600+100+50")

janela.configure(bg="#FACADA")

label = tk.Label(janela, 
                 text="Qual o seu nome?",
                 bg="red",
                 font="papyrus",
                 foreground="blue")

def acao_do_botao():
    label2 = tk.Label(janela, text=f"Bom dia {campo_texto}")

botao = tk.Button (janela, text="clique em mim!", command= acao_do_botao)

campo_texto = tk.Entry(janela)



#COLOCANDO ICONE
janela.iconbitmap("icon/adobe.ico")


label.pack()
botao.pack()
campo_texto.pack()
label2.pack()

janela.mainloop()


