import tkinter as tk 
from tkinter import *
from tkinter import ttk 

root = tk.Tk()

root.title("Restaurante Brasa & Lenha")
root.geometry("800x600")
root.config(bg="#6959CD")

lt1 = tk.Label(root, text="Brasa & Lenha",bg="#6959CD",fg='#F0F0F0',font=('none',30))
lt1.place(x=250,y=50) 

bt1 = tk.Button(root, text='Add prato',bg="#FFFFFF",fg="#000000",font=('none',20))
bt1.place(x=100,y=170)          





















root.mainloop()
tk.Label 