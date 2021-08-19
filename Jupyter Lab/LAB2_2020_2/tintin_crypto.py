# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 18:56:21 2020

@author: ASUS
"""

#%%
import bs4 as bs
import requests as r
from tkinter import Label, Frame, Button, LabelFrame, Tk, StringVar
from tkinter.ttk import Notebook,Combobox,Treeview,Scrollbar
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import threading
import textwrap
from numpy import arange
from tkcalendar import DateEntry
import pandas as pd
from datetime import datetime,timedelta

class CryptoMonitor():
    def __init__(self,master):
        self.master = master
        self.master.geometry("700x600")
        #self.master.resizable(0,0)
        self.Coin = StringVar(value="BTC-USD")
        self.precio = 0
        startDate = datetime.now() - timedelta(days=7)

        endDate = datetime.now() - timedelta(days=1)
        Coins = ["Bitcoin","Ethereum","Bitcoin-Cash","Litecoin","Ethereum-Classic","Basic-Attention-Token","Zcash"]
        Coins2 = ["BTC-USD","ETH-USD","BCH-USD","LTC-USD","ETC-USD","BAT-USD","ZEC-USD"]
        Acronimos = ["BTC","ETH","BCH","LTC","ETC","BAT","ZEC"]
        self.Coins_dic = dict(zip(Coins2,Acronimos))
        self.Coins_dic2 = dict(zip(Coins2,Coins))
        
        frm = Frame(master)
        frm1 = LabelFrame(frm,text="Tokens")
        frm2 = LabelFrame(frm, text="Rango fecha")
        frm3 = LabelFrame(frm, text="Tablas y graficos")
        
        frm.pack()
        frm1.grid(column=0,row=0,padx=7,pady=5)
        frm2.grid(column=0,row=1)
        frm3.grid(column=0,row=2,padx=7,pady=7)
        
        fig = Figure(figsize=(7,4))
        self.ax = fig.add_subplot(111)    # facecolor='black'
        self.ax.set_xlabel('Fecha')
        self.ax.set_ylabel('Precio de Cierre ($)')
        
        cmbBox = Combobox(frm1, values=Coins2, textvariable=self.Coin)
        self.lblPrecio = Label(frm1, text="", width=25   ,fg="green",font="Arial 15 bold")
        
        self.dtEntry1 = DateEntry(frm2,width=24,locale="es_PE")
        self.dtEntry1.set_date(startDate)
        self.dtEntry2 = DateEntry(frm2,width=24,locale="es_PE")  
        self.dtEntry2.set_date(endDate)        
        btnAsignar = Button(frm2,text="Obtener datos", width=13, command=self.update_tablas)
        
        self.notebook = Notebook(frm3,width=500)
        self.notebook.pack()
        frmNote1 = Frame(self.notebook,bg="white")
        frmNote2 = Frame(self.notebook,height=80)
        frmNote3 = Frame(self.notebook)
        #self.lblInfo = Label(frmNote1,text="",bg="white",justify="left")
        scrollbary = Scrollbar(frmNote2, orient="vertical")
        self.tabla = Treeview(frmNote2, columns=["Open","High","Close"],
                              yscrollcommand=scrollbary.set)
        scrollbary.config(command=self.tabla.yview)
        self.graph = FigureCanvasTkAgg(fig, master=frmNote3)
        self.graph.get_tk_widget().pack(side='top', fill='both', expand=True)
        
        
        
        
        cmbBox.grid(column=0,row=0,padx=7,pady=10)
        self.lblPrecio.grid(column=1,row=0)
        
        self.dtEntry1.grid(column=0,row=0,padx=11)
        self.dtEntry2.grid(column=1,row=0,padx=8)
        btnAsignar.grid(column=2, row=0,padx=11,pady=5)
        
        #self.notebook.add(frmNote1,text="Info")
        self.notebook.add(frmNote2,text="Tabla")
        self.notebook.add(frmNote3, text="Grafico")
        #self.lblInfo.grid(padx=20,pady=15)
        self.tabla.pack(side="left",fill='both')
        scrollbary.pack(side="left", fill='y')
        
        self.tabla.heading("#0", text="Date")
        self.tabla.heading("#1", text="Open")
        self.tabla.heading("#2", text="High")
        #self.tabla.heading("#3", text="Low")
        self.tabla.heading("#3", text="Close")
                        
    
        self.tabla.column("#0", stretch=False, minwidth=80, width=150)
        self.tabla.column("#1", stretch=False, minwidth=60, width=110, anchor='e')
        self.tabla.column("#2", stretch=False, minwidth=60,  width=110, anchor='e')
        self.tabla.column("#3", stretch=False, minwidth=60,  width=110, anchor='e')
    
                     
        #self.update_info()
        self.update_tablas()
        #self.master.bind("<<ComboboxSelected>>",self.update_info)
        self.master.after(10,self.start_animation)
        
    def start_animation(self):
        thr = threading.Thread(target=self.animate_prices, daemon=True)
        thr.start()
        
    def animate_prices(self):
        self.update_prices()
        
    def update_prices(self):
        coin_json = r.get("https://api.coinbase.com/v2/prices/{}/spot".format(self.Coin.get()))
        #print(self.Coin.get(),"=====")
        precio_viejo = self.precio
        self.precio = float(coin_json.json()["data"]["amount"])

        if self.precio>precio_viejo:
            self.lblPrecio.config(text="{0:.4f} USD".format(self.precio),fg="green")
        elif self.precio<precio_viejo:
            self.lblPrecio.config(text="{0:.4f} USD".format(self.precio),fg="red")
        else:
            self.lblPrecio.config(text="{0:.4f} USD".format(self.precio))
            
        self.master.after(1000,self.update_prices)   
        
#    def update_info(self,handle=0):
#        moneda = self.Coin.get().lower()
#        if len(moneda.split()) > 1:
#            moneda = "-".join(moneda.split())
#        else:
#            pass
#        url = r.get("https://coinmarketcap.com/currencies/{}/".format(moneda))
#        soup = bs.BeautifulSoup(url.text,'lxml')
#        match = soup.find("div",class_="col-sm-8")
#        wrap = textwrap.TextWrapper(width=55)
#        wrapped_info = wrap.wrap(match.contents[2].text)
#        wrapped_info = "\n".join(wrapped_info)
#        self.lblInfo.config(text=wrapped_info)
#        self.update_tablas()
        
    def update_tablas(self):
        moneda2 = self.Coin.get()
        moneda = self.Coins_dic2[moneda2].lower()
        print(moneda)
#        if len(moneda.split()) > 1:
#            moneda = "-".join(moneda.split())
#        else:
#            pass
        
        start=self.dtEntry1.get_date()
        end=self.dtEntry2.get_date()
        if start == datetime.now():
            start = start - timedelta(days=1)
        elif end == datetime.now():
            end = end - timedelta(days=1)
        start="{}{:02d}{:02d}".format(start.year,start.month,start.day)
        end="{}{:02d}{:02d}".format(end.year,end.month,end.day)
        data = pd.read_html("https://coinmarketcap.com/currencies/{}/historical-data/?start={}v&end={}".format(moneda,start,end))
        print(start,"--",end)
        print(data[2])
        coin_dt = data[2]
        self.tabla.delete(*self.tabla.get_children())
        for date,open_,high,close in zip(coin_dt["Date"],coin_dt["Open*"],
                                             coin_dt["High"],coin_dt["Close**"]):
            self.tabla.insert("","end",text=date,values=[open_,high,close])
        coin_dt.set_index(pd.to_datetime(coin_dt["Date"]),inplace=True)
        coin_dt.drop(["Low","Volume","Market Cap"],axis=1,inplace=True)
        self.ax.cla()
        self.ax.set_title("Precio de Cierre ($) vs Fecha")
        self.ax.grid()
        coin_dt.plot(ax=self.ax )
        self.graph.draw()

root = Tk()
Crypto = CryptoMonitor(root)
root.mainloop()