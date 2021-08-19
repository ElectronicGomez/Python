# -*- coding: utf-8 -*-
"""
Created on Fri May 15 21:51:07 2020

@author: ASUS
"""

from  tkinter import *
import time

#FUNCION PARA ACTUALIZAR LA HORA
def times():
    current_time=time.strftime("%H:%M:%S") 
    clock.config(text=current_time,bg="orange",fg="blue",font="Arial 50 bold")
    clock.after(200,times)
    
#VENTANA
root=Tk()
root.geometry("485x250")
root.title("Reloj digital con Tkinter")
clock=Label(root,font=("times",50,"bold"))

clock.grid(row=2,column=1,pady=25,padx=100)
times()

digi=Label(root,text=" Hora Actual",font="times 24 bold",fg="deep sky blue")
digi.grid(row=0,column=1)

root.mainloop()