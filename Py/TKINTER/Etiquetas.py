# -*- coding: utf-8 -*-
"""
Created on Sun May  3 04:31:41 2020

@author: ASUS
"""

#%% EJEMPLO 4
from tkinter import*
v0 = Tk()
v0.config(background = "blue")
v0.geometry("500x300+100+100")
v0.resizable(width = False, height = False)

Label(v0, text = "!Etiqueta 1!", bg = "skyblue", fg = "white", font = ("verdana",20)).pack(side = "right")
Label(v0, text = "!Etiqueta 2!",bg = "red",fg = "black", font = ("verdana",16)).pack(side = "left")
Label(v0, text = "!Etiqueta 3!", bg = "orange", fg = "white", font = ("verdana",16)).pack(side = "top")
Label(v0, text = "!Etiqueta 2!",bg = "green", fg = "white", font = ("verdana",16)).pack(side = "bottom")

#Fin
v0.mainloop()
#%%
from tkinter import*
v0 = Tk()
v0.config(background = "green")
v0.geometry("450x450+100+100")

Label(v0, text = "UNO", bg = "skyblue", fg = "white", font = ("verdana",15)).grid(row = 1, column = 1)
Label(v0, text = "DOS", bg = "blue", fg = "white", font = ("Verdana",15)).grid(row = 2, column = 1)
Label(v0, text = "TRES", bg = "orange", fg = "white", font = ("verdana",15)).grid(row = 1, column = 2)
Label(v0, text = "CUATRO", bg = "black", fg = "white", font = ("verdana",15)).grid(row = 1, column = 3)
Label(v0, text = "CINCO", bg = "white", fg = "black", font = ("verdana",15)).grid(row = 3, column = 3)

#POSICIONAMIENTO RELATIVO
Label(v0, text = "PRUEBA", bg = "skyblue", fg = "white", font = ("verdana",15)).place(x = 100, y = 150)
#Fin
v0.mainloop()
#%% EJEMPLO 5: WIDGET BUTTON
from tkinter import*
v0 = Tk()
v0.config(background = "skyblue")
v0.geometry("450x450+100+100")

boton1 = Button(v0, text = "Boton1", bg = "blue", fg = "white", font = ("verdana",15)).place(x = 100, y = 100)
boton2 = Button(v0, text = "Boton", bg ="orange", fg = "white", font = ("verdana",15) ).place(x = 200, y = 100)
#Fin
v0.mainloop()

#%%









































