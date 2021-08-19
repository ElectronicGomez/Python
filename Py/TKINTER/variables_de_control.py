# -*- coding: utf-8 -*-
"""
Created on Sun May  3 05:26:52 2020

@author: ASUS
"""
#%%
from tkinter import*
v0 = Tk()
#v0.config(background = "green")
v0.geometry("400x400+100+100")
nombre = StringVar()
apellidoP = StringVar()
apellidoM = StringVar()
edadE = IntVar(value = " ")

def ImprimirSaludo():
    print("Hola "+nombre.get()+" "+apellidoP.get()+" "+apellidoM.get()+" "+str(edadE.get()))


v0.title("Examen")
etiqueta1 = Label(v0, text = "Escribe tu nombre").place(x = 10, y = 10)
etiqueta2 = Label(v0, text = "Ingresa apellido paterno").place(x = 10, y = 50)
etiqueta3 = Label(v0, text = "Igresa apellido materno").place(x = 10, y = 90)
etiqueta4 = Label(v0, text = "Ingresa edad").place(x = 10, y = 130)
boton1 = Button(v0, text = "Pulsar saludo", command = ImprimirSaludo).place(x = 10, y = 170)

caja1 = Entry(v0, textvariable = nombre).place(x = 150, y = 10)
caja2 = Entry(v0, textvariable = apellidoP).place(x = 150, y = 50)
caja3 = Entry(v0, textvariable = apellidoM).place(x = 150, y = 90)
caja4 = Entry(v0, textvariable = edadE).place(x = 150, y = 130)



#Fom
v0.mainloop()

















