# -*- coding: utf-8 -*-
"""
Created on Sun May  3 05:45:44 2020

@author: ASUS
"""
#%%
from tkinter import*

def operacion():
    numero = var1.get()
    if opcion.get() == 1:
        total = numero*10
    elif opcion.get() == 2:
        total = numero*20
    elif opcion.get() == 3:
        total = numero*30
    elif opcion.get() == 4:
        total = numero *40
    elif opcion.get() == 5:
        total = numero*50
    else:
        total = numero**2
    print("el total de la operación es ",total)
        
    

v0 = Tk()
v0.geometry("400x300+100+100")
v0.title("Prueba 3")

var1 = IntVar(value = " ")
opcion = IntVar()

etiqueta1= Label(v0, text = "Escribe el numero ").place(x = 10, y =10)
caja1 = Entry(v0, textvariable = var1).place(x = 160, y = 10)

etiqueta2 = Label(v0, text = "Escribe tu opcion").place(x = 10, y = 50)

x10 = Radiobutton(v0, text = "x10", value = 1, variable = opcion).place(x = 10, y = 90 )
x20 = Radiobutton(v0, text = "x20", value = 2, variable = opcion).place(x = 70, y = 90 )
x30 = Radiobutton(v0, text = "x30", value = 3, variable = opcion).place(x = 120, y = 90 )
x40 = Radiobutton(v0, text = "x40", value = 4, variable = opcion).place(x = 10, y = 130 )
x50 = Radiobutton(v0, text = "x50", value = 5, variable = opcion).place(x = 70, y = 130 )
cuadrado = Radiobutton(v0, text = "cuadrado", value = 6, variable = opcion).place(x = 120, y = 130 )

boton1 = Button(v0, text = "Ejecutar operacion", command = operacion).place(x = 10, y = 170)

#Fin
v0.mainloop()













