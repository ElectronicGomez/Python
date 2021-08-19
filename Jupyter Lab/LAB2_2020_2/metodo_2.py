#%%
from bs4 import BeautifulSoup
import requests
import numpy as np
#import requests as r
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
from colors import red, green, black 

class CryptoMonitor():
    def __init__(self,master):
        self.master = master
        self.master.geometry("700x600")
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
        
        
        
        
        cmbBox.grid(column=1,row=0,padx=7,pady=10)
        self.lblPrecio.grid(column=2,row=0)
        
        self.dtEntry1.grid(column=0,row=0,padx=11)
        self.dtEntry2.grid(column=1,row=0,padx=8)
        btnAsignar.grid(column=2, row=0,padx=11,pady=5)
        
        #self.notebook.add(frmNote1,text="Info")
        self.notebook.add(frmNote2,text="Tabla de Precios")
        self.notebook.add(frmNote3, text="Grafico Precio")
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
        
        print("Actualización de precio de la moneda cada 5 segundos en tiempo real")
        print("===================================================================")
        
                     
        
        self.update_tablas()
        
        self.master.after(10,self.start_animation)
        
    def start_animation(self):
        thr = threading.Thread(target=self.animate_prices, daemon=True)
        thr.start()
        
    def animate_prices(self):
        self.update_prices()
        
    def update_prices(self):
                
        coin_json = requests.get("https://api.coinbase.com/v2/prices/{}/spot".format(self.Coin.get()))       
        self.precio_viejo = self.precio
        self.precio = float(coin_json.json()["data"]["amount"])
        
        resta = self.precio-self.precio_viejo
#         print(resta)
        if self.precio_viejo!=0:
            
            print (f"Precio Actual: ${self.precio_viejo}")
            print(f"Precio hace 5 segundos: ${self.precio}")
            if resta<0:
                
                self.lblPrecio.config(text="{0:.4f} USD".format(self.precio),fg="green")
                print(Fore.GREEN+f"Disminuyó la moneda en ${resta:,.2f}\n")
            elif resta>0:
                
                self.lblPrecio.config(text="{0:.4f} USD".format(self.precio),fg="red")
                print(Fore.RED+f"Aumento la moneda en ${resta:,.2f}\n")
            else:
                
                self.lblPrecio.config(text="{0:.4f} USD".format(self.precio),fg="black")
                print(Fore.BLACK+"La moneda no ha subido ni bajado de precio\n")

        self.master.after(1000,self.update_prices)   
        

        
    def update_tablas(self):
        #moneda2 = self.Coin.get()
        #moneda = self.Coins_dic2[moneda2].lower()
        moneda = self.Coin.get()
        #print(moneda)
#       
        start=self.dtEntry1.get_date()
        end=self.dtEntry2.get_date()
        
        start="{}{:02d}{:02d}".format(start.year,start.month,start.day)
        end="{}{:02d}{:02d}".format(end.year,end.month,end.day)
        #print(start,"--",end)
        
        dia_ini = pd.to_datetime(start)
        dia_fin = pd.to_datetime(end)
        #print(dia_ini,"==",dia_fin)
        dia_ini = int(dia_ini.timestamp())
        dia_fin = int(dia_fin.timestamp())
        #print(dia_ini,"==",dia_fin)
#        dia_ini = datetime.datetime(start)
#        dia_fin = datetime.datetime(end)
#        dia_ini = int(dia_ini.timestamp())
#        dia_fin = int(dia_fin.timestamp())
#        data = pd.read_html("https://coinmarketcap.com/currencies/{}/historical-data/?start={}v&end={}".format(moneda,start,end))
        
        url = f"https://finance.yahoo.com/quote/{moneda}/history?period1={dia_ini}&period2={dia_fin}&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true"
        
        r = requests.get(url)
       
        if r.status_code == requests.codes.ok:
            soup = BeautifulSoup(r.text, 'html')
        
        data_1=[]
        data_2=[]
        for i in soup.find_all("td",attrs={"class":"Py(10px) Ta(start) Pend(10px)"}):
            data_1.append(i.text)
        for i in soup.find_all("td",attrs={"class":"Py(10px) Pstart(10px)"}):
            data_2.append(((i.text).replace("-",str(np.nan)).replace(",","")))   
        lista=[]
        
        cont=0
        cont_2=0
        arreglo=[]
        for i in (data_2): 
            #print(i)
            if cont==0:
                
                arreglo.append(data_1[cont_2])
                arreglo.append(float(i))
                cont=cont+1
                cont_2=cont_2+1
            elif cont!=5:
                arreglo.append(float(i))
                cont=cont+1
            else:
                arreglo.append(float(i))
                cont=0
                lista.append(arreglo)
                arreglo=[]
                
        
            data_pag=pd.DataFrame(data=(lista),columns=["Fecha","Open","High","Low","Close","Add Close","Volume"])
            aux = pd.to_datetime(data_pag["Fecha"])
            aux2 = data_pag["Fecha"]
            #print(aux2)
            data_pag=data_pag.drop(columns=["Fecha"]).drop(columns=["Low"]).drop(columns=["Volume"]).drop(columns=["Add Close"])
            # data_pag
            data_pag.index=[x for x in range(len(data_pag))]
            for i in range(3):
                
                for item in range(len(data_pag)):
                    data_pag.loc[item] = data_pag.loc[item].astype(float)
                    
            data_pag.set_index(pd.to_datetime(aux),inplace=True)
            
            self.tabla.delete(*self.tabla.get_children())
            for date,open_,high,close in zip(aux2,data_pag["Open"],
                                                 data_pag["High"],data_pag["Close"]):
                self.tabla.insert("","end",text=date,values=[open_,high,close])
        data_pag.drop(["Open","High"],axis=1,inplace=True)
        self.ax.cla()
        self.ax.set_title("Precio de Cierre($) vs Fecha")
        self.ax.grid()
        data_pag.plot(ax=self.ax)
        self.graph.draw()
##
root = Tk()
Crypto = CryptoMonitor(root)
root.mainloop()