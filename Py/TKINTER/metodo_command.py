# -*- coding: utf-8 -*-
"""
Created on Sun May  3 05:16:18 2020

@author: ASUS
"""
#%%
from tkinter import*
import time

def parpadear():
    v0.iconify()
    time.sleep(1)
    v0.deiconify()

#Configuracion de la raiz
v0 = Tk()
v0.config(background = "green")
v0.geometry("450x450+100+100")

boton1 = Button(v0, text = "Pulse", bg = "blue", fg = "white", font = ("verdana",15), command = parpadear).place(x = 100, y = 100)

#Fin
v0.mainloop()