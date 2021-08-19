# -*- coding: utf-8 -*-
"""
Created on Fri May 15 13:54:18 2020

@author: ASUS
"""

from tkinter import *
from tkinter import messagebox

def obtener():
    messagebox.showinfo("Mensaje","tu seleccionaste" + valor.get())
    messagebox.showwarning("Advertencia", "Peligro")
    
ventana = Tk()
valor = StringVar()
ventana.title("Uso de SpinBox con tkinter")
ventana.geometry("400x300")
# Colocando valores
etiqueta = Label(ventana, text = "Ejemplo de SpinBox").place(x = 20, y = 20)
combo = Spinbox(ventana, values = ("UNO","DOS","TRES","CUATRO","CINCO")).place(x = 20, y = 50 )
#Haciendo un rango
etiqueta2 = Label(ventana, text = "Ejemplo 2 de SpinBox").place(x = 20, y = 80)
combo2 = Spinbox(ventana,from_= 1, to = 10, textvariable = valor).place(x = 20, y = 110)
boton = Button(ventana, text = "Obtener valor SpinBox", command = obtener).place(x = 80, y = 140)


ventana.mainloop()