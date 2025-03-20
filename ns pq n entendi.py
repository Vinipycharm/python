import tkinter as tk 
from tkinter import *

root = tk.Tk()
root.title()
root.geometry("250x350")

lt1 = tk.Label(root, text="Nome")
lt1.place(x=20,y=50)

lt2 = tk.Label(root, text="telefone")
lt2.place(x=20,y=100)

lt3 = tk.Label(root, text="endereço")
lt3.place(x=20,y=150)

lt4 = tk.Label(root, text="distrito")
lt4.place(x=20,y=200)

lt5 = tk.Label(root, text="Pais")
lt5.place(x=20,y=250)

lt6 = tk.Label(root, text="Email")
lt6.place(x=20,y=300)

input1= tk.Entry(root)
input1.place(x=100,y=50)
root.mainloop()




