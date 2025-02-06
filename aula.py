import tkinter as tk

def mudar_cor(cor):
    root.config(bg=cor)
          
root = tk.Tk()
root.title("Mudança de Cor")
root.geometry("200x200")

botao1 = tk.Button(root, text="Azul", command=lambda: mudar_cor("blue"))
botao1.place(x = 50, y = 50)

botao2 = tk.Button(root, text="Vermelho", command=lambda: mudar_cor("red"))
botao2.place(x = 100, y = 50)

botao3 = tk.Button(root, text="Verde", command=lambda: mudar_cor("green"))
botao3.place(x = 50, y = 100)

botao4 = tk.Button(root, text="Amarelo", command=lambda: mudar_cor("yellow"))
botao4.place(x = 100, y = 100)

root.mainloop()