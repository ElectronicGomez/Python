# -*- coding: utf-8 -*-
"""
Created on Sun May  3 03:53:10 2020

@author: ASUS
"""
#%% EJEMPLO 1
from tkinter import * #Importamos los widgets del tikinter
v0 = Tk()             # Creamos la raiz y se crea un bucle
v0.title("Embebidos")
v0.config(background = "red") #Establecer color de fondo de la ventana
v0.geometry("600x300+300+300")  # Ancho x largo, posicion x = 300, y= 300
v0.resizable(width = FALSE, height = FALSE) #Ventana de tamaño fijo
v0.mainloop()
#%% EJEMPLO 2
from tkinter import *
v0 = Tk()
v0.config(background = "blue")
v0.geometry("300x300+100+100")
Label(v0, text = "Etiqueta", bg = "red", fg = "white", font = ("verdana",16)).place(x = 150, y = 100)
v1 = Toplevel(v0) #Ventana hija
v1.config(background = "skyblue")
v1.geometry("150x150+200+150")
#Fin
v0.mainloop()
#%% EJEMPLO 3
from tkinter import *

#Configuracion de la raiz
v0 = Tk()
v0.config(background = 'blue')
v0.geometry("300x300+100+100")
Label(v0, text = "!Hola mundo!").pack(side = "right")

#Fin
v0.mainloop()
#%%
from tkinter import *

#Configuracion de la raiz
v0 = Tk()
v0.config(background = 'blue')
v0.geometry("300x300+100+100")
Label(v0, text = "!Hola mundo!").pack(side = "right",fill="both")

#Fin
v0.mainloop()
#%%
from tkinter import*

#Configuracion de la raiz
v0 = Tk()
v0.config(background = "blue")
v0.geometry("300x300+100+100")
Label(v0, text = "!Hola mundo!").pack(side = "right",fill="both", expand = "yes")

#Fin
v0.mainloop()



































