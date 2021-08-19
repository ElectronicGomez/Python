# -*- coding: utf-8 -*-

#%%


import numpy as np
import requests as r
from tkinter import Label, Frame, Button, LabelFrame, Tk, StringVar
from tkinter.ttk import Notebook,Combobox,Treeview,Scrollbar
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import threading
import tkinter as tk

from tkcalendar import DateEntry
import pandas as pd
from datetime import datetime,timedelta


class CryptoMonitor():
    def __init__(self,master):
        self.master = master
        self.master.geometry("700x650+300+0")
        self.master.title('Crypto Monitor') 
        #self.master.resizable(0,0)
        self.Coin = StringVar(value="BTC-USD")
        self.precio = 0
        startDate = datetime.now()+timedelta(-30)

        endDate = datetime.now()
        Coins = ["Bitcoin","Ethereum","Bitcoin-Cash","Litecoin","Ethereum-Classic","Basic-Attention-Token","Zcash"]
        Coins2 = ["BTC-USD","ETH-USD","BCH-USD","LTC-USD","ETC-USD","BAT-USD","ZEC-USD"]
        Acronimos = ["BTC","ETH","BCH","LTC","ETC","BAT","ZEC"]
        self.Coins_dic = dict(zip(Coins2,Acronimos))
        self.Coins_dic2 = dict(zip(Coins2,Coins))
        
        frm = Frame(master)
        frm1 = LabelFrame(frm,text="Precio")
        frm2 = LabelFrame(frm, text="Rango de fecha")
        frm3 = LabelFrame(frm, text="Tabla y graficos")
        
        frm.pack()
        frm1.grid(column=0,row=0,padx=7,pady=5)
        frm2.grid(column=0,row=1)
        frm3.grid(column=0,row=2,padx=7,pady=7)
        
        fig = Figure(figsize=(7,4))
        self.ax = fig.add_subplot(111)    # facecolor='black'
        self.ax.set_xlabel('Fecha')
        self.ax.set_ylabel('Precio de Cierre ($)')
        
        self.mon = Label(frm1, text="Moneda").grid(column = 0, 
          row = 0, padx = 10, pady = 25)
        cmbBox = Combobox(frm1, values=Coins2, textvariable=self.Coin)
        self.lblPrecio = Label(frm1, text="", width=23   ,fg="green",font="Arial 15 bold")
        
        self.dtEntry1 = DateEntry(frm2,width=24,locale="es_PE")
        self.dtEntry1.set_date(startDate)
        self.dtEntry2 = DateEntry(frm2,width=24,locale="es_PE")  
        self.dtEntry2.set_date(endDate)        
        btnAsignar = Button(frm2,text="Obtener datos", width=13, command=self.update_tablas)
        
        self.notebook = Notebook(frm3,width=500)
        self.notebook.pack()
       
        frmNote2 = Frame(self.notebook,height=80)
        frmNote3 = Frame(self.notebook)
       
        scrollbary = Scrollbar(frmNote2, orient="vertical")
        self.tabla = Treeview(frmNote2, columns=["Open","High","Close"],
                              yscrollcommand=scrollbary.set)
        scrollbary.config(command=self.tabla.yview)
        self.graph = FigureCanvasTkAgg(fig, master=frmNote3)
        self.graph.get_tk_widget().pack(side='top', fill='both', expand=True)
        
        
        
        
        cmbBox.grid(column=1,row=0,padx=7,pady=10)
        self.lblPrecio.grid(column=2,row=0)
        
        self.dtEntry1.grid(column=0,row=0,padx=11)
        self.dtEntry2.grid(column=1,row=0,padx=8)
        btnAsignar.grid(column=2, row=0,padx=11,pady=5)
        
     
        self.notebook.add(frmNote2,text="Tabla de Precios")
        self.notebook.add(frmNote3, text="Grafico Precio")
        
        self.tabla.pack(side="left",fill='both')
        scrollbary.pack(side="left", fill='y')
        
        self.tabla.heading("#0", text="Date")
        self.tabla.heading("#1", text="Open")
        self.tabla.heading("#2", text="High")
       
        self.tabla.heading("#3", text="Close")
                        
    
        self.tabla.column("#0", stretch=False, minwidth=80, width=150)
        self.tabla.column("#1", stretch=False, minwidth=60, width=110, anchor='e')
        self.tabla.column("#2", stretch=False, minwidth=60,  width=110, anchor='e')
        self.tabla.column("#3", stretch=False, minwidth=60,  width=110, anchor='e')
    
        self.statusBar = tk.Label(self.master, text="", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.statusBar.pack(side=tk.BOTTOM, fill=tk.X)
        
        cmbBox.bind("<Enter>", lambda x: self.statusBar.config(text="Seleccione el tipo de moneda"))
        cmbBox.bind("<Leave>", lambda x: self.statusBar.config(text=""))
        self.lblPrecio.bind("<Enter>", lambda x: self.statusBar.config(text="Precio de moneda en tiempo real"))
        self.lblPrecio.bind("<Leave>", lambda x: self.statusBar.config(text=""))
        self.dtEntry1.bind("<Enter>", lambda x: self.statusBar.config(text="Seleccione la fecha inicial del rango de fecha"))
        self.dtEntry1.bind("<Leave>", lambda x: self.statusBar.config(text=""))
        self.dtEntry2.bind("<Enter>", lambda x: self.statusBar.config(text="Seleccione la fecha final del rango de fecha"))
        self.dtEntry2.bind("<Leave>", lambda x: self.statusBar.config(text=""))
        btnAsignar.bind("<Enter>", lambda x: self.statusBar.config(text="Actualizar la tabla de precios y grafico de precios"))
        btnAsignar.bind("<Leave>", lambda x: self.statusBar.config(text=""))
        
        self.notebook.bind("<Enter>", lambda x: self.statusBar.config(text="Seleccione una de estas pestañas"))
        self.notebook.bind("<Leave>", lambda x: self.statusBar.config(text=""))
        self.tabla.bind("<Enter>", lambda x: self.statusBar.config(text="Tabla de Precios"))
        self.tabla.bind("<Leave>", lambda x: self.statusBar.config(text=""))
        frmNote3.bind("<Enter>", lambda x: self.statusBar.config(text="Grafico Precio"))
        frmNote3.bind("<Leave>", lambda x: self.statusBar.config(text=""))
        
                     
        
        self.update_tablas()
        
        self.master.after(10,self.start_animation)
        
    def start_animation(self):
        thr = threading.Thread(target=self.animate_prices, daemon=True)
        thr.start()
        
    def animate_prices(self):
        self.update_prices()
        
    def update_prices(self):
        coin_json = r.get("https://api.coinbase.com/v2/prices/{}/spot".format(self.Coin.get()))
       
        precio_viejo = self.precio
        self.precio = float(coin_json.json()["data"]["amount"])
        print(precio_viejo)
        if self.precio>precio_viejo:
            self.lblPrecio.config(text="{0:,.2f} USD".format(self.precio),fg="green")
        elif self.precio<precio_viejo:
            self.lblPrecio.config(text="{0:,.2f} USD".format(self.precio),fg="red")
        else:
            self.lblPrecio.config(text="{0:,.2f} USD".format(self.precio),fg="black")
            
        self.master.after(5000,self.update_prices)   
        

        
    def update_tablas(self):
        #moneda2 = self.Coin.get()
        #moneda = self.Coins_dic2[moneda2].lower()
        moneda = self.Coin.get()
        #print(moneda)
#       
        start=self.dtEntry1.get_date()
        end=self.dtEntry2.get_date()
        if start == datetime.now():
            start = start - timedelta(days=1)
        elif end == datetime.now():
            end = end - timedelta(days=1)
        start="{}{:02d}{:02d}".format(start.year,start.month,start.day)
        end="{}{:02d}{:02d}".format(end.year,end.month,end.day)
#        print(start,"--",end)
        dia_ini = pd.to_datetime(start)
        dia_fin = pd.to_datetime(end)
#        print(dia_ini,"==",dia_fin)
        dia_ini = int(dia_ini.timestamp())
        dia_fin = int(dia_fin.timestamp())
#        print(dia_ini,"==",dia_fin)
#        data = pd.read_html("https://coinmarketcap.com/currencies/{}/historical-data/?start={}v&end={}".format(moneda,start,end))
        
        data = pd.read_html("https://finance.yahoo.com/quote/{}/history?period1={}&period2={}&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true".format(moneda,dia_ini,dia_fin))
       
        
#        print(f'Número total de tablas: {len(data)}')
        
        coin_dt = data[0]
#        print(coin_dt)
        coin_dt.drop(len(coin_dt)-1,inplace=True)
#        print("====")
        
        self.tabla.delete(*self.tabla.get_children())
        for date,open_,high,close in zip(coin_dt["Date"],coin_dt["Open"],
                                             coin_dt["High"],coin_dt["Close*"]):
            self.tabla.insert("","end",text=date,values=[open_,high,close])
        
        for i in range(3):    
            for item in range(len(coin_dt)):
                b = coin_dt.loc[item]
#                print(b[i])
                if (b[i]=="-"):
                    b[i]= np.nan
#                    print("no es entero")
                    
        
        #print(type(b[i]))
#        print("==")
        coin_dt.dropna(inplace=True)
        coin_dt.index=[x for x in range(len(coin_dt))]
        
        aux = coin_dt["Date"]      
        #coin_dt.set_index(pd.to_datetime(coin_dt["Date"]),inplace=True)
        
        coin_dt.drop(["Low","Volume","Adj Close**","Volume","Date"],axis=1,inplace=True)
        for i in range(3):
    
            for item in range(len(coin_dt)):
                coin_dt.loc[item] = coin_dt.loc[item].astype(float)
        coin_dt.set_index(pd.to_datetime(aux),inplace=True)
        
        
#        print(coin_dt)
        
        coin_dt.drop(["Open","High"],axis=1,inplace=True)
        
        self.ax.cla()
        self.ax.set_title("Precio de Cierre ($) vs Fecha")
        self.ax.grid()
        coin_dt.plot(ax=self.ax)
        self.graph.draw()
##
root = Tk()
Crypto = CryptoMonitor(root)
root.mainloop()