# -*- coding: utf-8 -*-
"""
Created on Sun May  3 06:35:08 2020

@author: ASUS
"""
#%%

from tkinter import*

def var_estados():
    print("Masculinos %d Femeninos: %d"%(var1.get(),var2.get()))

v0 = Tk()
Label(v0, text = "su Sexo es:").grid(row = 1, sticky = W)
var1 = IntVar()
Checkbutton(v0, text = "Masculino", variable = var1).grid(row = 1, sticky = W)
var2 = IntVar()
Checkbutton(v0, text = "Femenino", variable = var2).grid(row = 2, sticky = W)
boton1 = Button(v0, text = "Salir", command = v0.destroy).grid(row = 3, sticky = W, pady = 4)
boton2 = Button(v0, text = "Mostrar", command = var_estados).grid(row = 4, sticky = W, pady = 4)


#Fin
v0.mainloop()