# -*- coding: utf-8 -*-
"""
Created on Sun May  3 05:03:01 2020

@author: ASUS
"""

#%% EJEMPLO 7 WIDGET CAJA DE TEXTO (Para ingresar datos)

from tkinter import*
v0 = Tk()
v0.config(background = "green")
v0.geometry("450x450+100+100")

Label(v0, text = "Usuario: ", bg = "green", fg = "black", font = ("verdana",11)).place(x = 10, y = 100)
entrada = StringVar #Entrada es un objeto de la clase StringVar
caja = Entry(v0, textvariable = entrada).place(x = 80, y = 100)


#Fin
v0.mainloop()