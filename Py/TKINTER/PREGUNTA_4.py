# -*- coding: utf-8 -*-
"""
Created on Fri May 15 21:27:39 2020

@author: ASUS
"""
from tkinter import*
import random


def cambiar():
    lista_colores=['yellow','deep sky blue','orange','lawn green']
    color=random.choice(lista_colores)
    boton1.config(background=color)
    
root=Tk()
root.config()
root.geometry("400x300")
root.resizable(0,0)
root.title('Cambio de Colores')


boton1=Button(root,text='Click cambia color',
              bg='Yellow',fg='White', font=('Comic Sans MS',13),
              command=cambiar)
boton1.place(x=10,y=10)
root.mainloop()

