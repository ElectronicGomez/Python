
#%%
import tkinter as tk
import tkinter.ttk as ttk
import tkcalendar
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


import matplotlib.pyplot as plt
import requests
from datetime import datetime,timedelta
import threading
from tkinter.messagebox import showerror, showinfo, askokcancel


from bs4 import BeautifulSoup

import pandas as pd
from matplotlib.figure import Figure

tipo_moneda = ["BTC-USD","ETH-USD","BCH-USD","LTC-USD","ETC-USD","BAT-USD","ZEC-USD"]


class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Crypto Monitor")
        self.master.resizable(0, 0)
        # Se intercepta el evento de cerrar ventana TopLevel
        self.master.protocol("WM_DELETE_WINDOW", self.close_app)
        
        self.URL      = tk.StringVar() 
        self.anterior = 0  
            
        frm = tk.Frame(self.master)
        frm.pack(padx=5, pady=5)
        
        frm1 = tk.LabelFrame(frm, text="PRECIO", width=2, font='Arial 10')
        frm2 = tk.LabelFrame(frm, text="RANGO DE FECHA", width=2, font='Arial 10')
        frm3 = tk.LabelFrame(frm, text="TABLA Y GRAFICOS", width=2, font='Arial 10')
        
        frm1.pack(padx=5, pady=5)
        frm2.pack(padx=5, pady=5)
        frm3.pack(padx=5, pady=5)

        # -------------------------- frm1 --------------------------
        
        
        self.lblMoneda    = tk.Label(frm1, text="Moneda:")
        self.cboMoneda    = ttk.Combobox(frm1, width=20, value = tipo_moneda)
        self.cboMoneda.current(0)
        self.lblPrecioAct = tk.Label(frm1, width=11, font='Arial 14 bold')
        
        self.lblMoneda.grid(row=0, column=0,padx=10, pady=10)
        self.cboMoneda.grid(row=0, column=1,padx=10, pady=10)
        self.lblPrecioAct.grid(row=0, column=2,padx=10, pady=10)
        
        self.cboMoneda.bind("<<ComboboxSelected>>", self.Tipo)
        
        # -------------------------- frm2 --------------------------
        
        self.cal_ini  = tkcalendar.DateEntry(frm2, width=15, date_pattern='dd/mm/y')
        self.cal_ini.set_date(datetime.now() + timedelta(-30))

        self.cal_fin  = tkcalendar.DateEntry(frm2, width=15, date_pattern='dd/mm/y') 
        self.cal_fin.set_date(datetime.now())

        self.btnObtener = tk.Button(frm2, text="Obtener Datos", width=14, command=self.obtDatos)
        
        self.cal_ini.grid(row=0, column=0,padx=10, pady=10)
        self.cal_fin.grid(row=0, column=1,padx=10, pady=10)
        self.btnObtener.grid(row=0, column=2,padx=10, pady=10)
        
        # -------------------------- frm3 --------------------------
    
        self.notebook = ttk.Notebook(frm3)
        
        #---
        self.tabA = ttk.Treeview(self.notebook, columns=[1,2,3]) # 3 columnas
        self.tabA.grid(row=0, column=0, columnspan=2, padx=5, pady=5) #expandido en 2 columnas      
        self.tabA.heading("#0", text="Date", anchor=tk.W)
        self.tabA.heading("#1", text="Open")
        self.tabA.heading("#2", text="High")
        self.tabA.heading("#3", text="Close")
        self.tabA.column("#0", stretch=False, minwidth=150, width=150)
        self.tabA.column("#1", stretch=False, minwidth=80, width=80, anchor=tk.CENTER)
        self.tabA.column("#2", stretch=False, minwidth=80, width=80, anchor=tk.CENTER)
        self.tabA.column("#3", stretch=False, minwidth=80, width=80, anchor=tk.CENTER)                   
        #---        
        self.B = tk.Frame(self.notebook, bg='#FFFFFF')       
        self.fig = Figure(figsize=(7,4))
        self.ax = self.fig.add_subplot(111)
#        self.fig, self.ax = plt.subplots(figsize=(5, 4))
        self.fig.set_facecolor('#FFFFFF')   
        self.graph = FigureCanvasTkAgg(self.fig, master=self.B)
        self.graph.get_tk_widget().pack()
        #---       
        self.notebook.add(self.tabA, text="Tabla de Precios")
        self.notebook.add(self.B, text="Grafico Precio")        
        self.notebook.pack()
        
        # ------------------------ Menu inferior ------------------------------
        self.statusBar = tk.Label(self.master, text="", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.statusBar.pack(side=tk.BOTTOM, fill=tk.X)
        
        self.cboMoneda.bind("<Enter>", lambda x: self.statusBar.config(text="Seleccione el tipo de moneda"))
        self.cboMoneda.bind("<Leave>", lambda x: self.statusBar.config(text=""))
        self.lblPrecioAct.bind("<Enter>", lambda x: self.statusBar.config(text="Precio actualizado"))
        self.lblPrecioAct.bind("<Leave>", lambda x: self.statusBar.config(text=""))
        self.cal_ini.bind("<Enter>", lambda x: self.statusBar.config(text="Seleccione la fecha inicial del rango de fecha"))
        self.cal_ini.bind("<Leave>", lambda x: self.statusBar.config(text=""))
        self.cal_fin.bind("<Enter>", lambda x: self.statusBar.config(text="Seleccione la fecha final del rango de fecha"))
        self.cal_fin.bind("<Leave>", lambda x: self.statusBar.config(text=""))
        self.btnObtener.bind("<Enter>", lambda x: self.statusBar.config(text="Dar click para actualizar la tabla y graficos"))
        self.btnObtener.bind("<Leave>", lambda x: self.statusBar.config(text=""))
        
        self.notebook.bind("<Enter>", lambda x: self.statusBar.config(text="Seleccione una pestaña"))
        self.notebook.bind("<Leave>", lambda x: self.statusBar.config(text=""))
        self.tabA.bind("<Enter>", lambda x: self.statusBar.config(text="Tabla de Precios"))
        self.tabA.bind("<Leave>", lambda x: self.statusBar.config(text=""))
        self.B.bind("<Enter>", lambda x: self.statusBar.config(text="Grafico Precio"))
        self.B.bind("<Leave>", lambda x: self.statusBar.config(text=""))
        
        
        
        self.Tipo(self.cboMoneda.get())
        self.obtDatos()
        #self.master.after(10,self.paralelo)
        
    def Tipo(self, event):
        #print(self.cboMoneda.get())
        self.anterior = 0 
        self.obtDatos()
        self.master.after(5000, self.paralelo)
        
        
    def paralelo(self):
        thr = threading.Thread(target=self.ActPrecio, daemon=True)
        thr.start()
    
    
    def ActPrecio(self):
        xd = self.cboMoneda.get()         
        URL = f"https://api.coinbase.com/v2/prices/{xd}/spot"
        r = requests.get(URL) 
        data = r.json()
        act = float(data['data']['amount'])

        res = act - self.anterior                    
        #print(res)
        
        if self.anterior!=0:
            if   res< 0: self.lblPrecioAct.config(text=f"{act:,.3f} USD", fg="red")
            elif res> 0: self.lblPrecioAct.config(text=f"{act:,.3f} USD", fg="green")
            elif res==0: self.lblPrecioAct.config(text=f"{act:,.3f} USD", fg="black")
        else:
            self.lblPrecioAct.config(text=f"{act:,} USD", fg="black")
                    
        self.anterior = float(data['data']['amount']) 
        # REPITE -----------------------------------------------
        self.master.after(5000, self.ActPrecio)
    
        
    def obtDatos(self):
        #print(self.cal_ini.get_date())
        #print(self.cal_fin.get_date())
        #print(self.cal_ini.get_date()<self.cal_fin.get_date())
          
        if self.cal_ini.get_date() > self.cal_fin.get_date():
            showerror("Error", "RANGO DE FECHA INCORRECTO")
            self.cal_ini.set_date(datetime.datetime.now() + datetime.timedelta(-30))
            self.cal_fin.set_date(datetime.datetime.now())
        select = self.cboMoneda.get()     
        
        dia_ini = self.cal_ini.get_date()
        dia_fin = self.cal_fin.get_date()
        
#        if dia_ini == datetime.now():
#            dia_ini = dia_ini - timedelta(days=1)
#        elif dia_fin == datetime.now():
#            dia_fin = dia_fin - timedelta(days=1)
            
        dia_ini="{}{:02d}{:02d}".format(dia_ini.year,dia_ini.month,dia_ini.day)
        dia_fin="{}{:02d}{:02d}".format(dia_fin.year,dia_fin.month,dia_fin.day)
        
        dia_ini = pd.to_datetime(dia_ini)
        dia_fin = pd.to_datetime(dia_fin)
        dia_ini = int(dia_ini.timestamp())
        dia_fin = int(dia_fin.timestamp())
        
                 
#        asd1,asd2,asd3 = f"{self.cal_ini.get_date()}".split('-')
#        asd4,asd5,asd6 = f"{self.cal_fin.get_date()}".split('-')       
#        dia_ini = datetime.datetime(int(asd1), int(asd2), int(asd3))
#        dia_fin = datetime.datetime(int(asd4), int(asd5), int(asd6))
#        dia_ini = int(dia_ini.timestamp())
#        dia_fin = int(dia_fin.timestamp())
##        print(dia_ini)
#        print(dia_fin)
                
        #url_ = "https://finance.yahoo.com/quote/"+select+"/history?period1="+str(dia_ini)+"&period2="+str(dia_fin) 
        url = f"https://finance.yahoo.com/quote/{select}/history?period1={dia_ini}&period2={dia_fin}&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true"
        
        #print(url_)
        rr = requests.get(url)

        soup = BeautifulSoup(rr.text, 'html')
        info_completa = []
        info_parte = []        
        info_completat = []
        info_partet = []
        
        for info in soup.find_all('tr', attrs={"class":"BdT Bdc($seperatorColor) Ta(end) Fz(s) Whs(nw)"}):
            info_parte = [] 
            info_partet = [] 
            for idx, i in enumerate (info.find_all('td'), start=0):
                #print(i.text)
                if idx == 0: info_parte.append(i.text)
                elif idx in [1,2,4]: 
                    if i.text=='-': info_parte.append('-')
                    else: info_parte.append(float(i.text.replace(',','')))
                if idx in [0,1,2,4]: info_partet.append(i.text)
            #print(info_parte)
            info_completa.append(info_parte) 
            info_completat.append(info_partet) 
        
                       
        self.tabA.delete(*self.tabA.get_children())
        # Se llenan la tabla con las notas de la lista data
        for i in info_completat:
            self.tabA.insert("", tk.END, text=i[0] , values=i[1:])
        
        # Grafica        
        data = [ii for ii in info_completa]        
        historial = pd.DataFrame(data, columns=['Date', 'Open', 'High', 'Close'])
        historial.index = pd.DatetimeIndex(pd.to_datetime(historial["Date"]))
        historial.drop(columns="Date", inplace= True)
        historial.drop(historial[historial['Close'].apply(lambda x: isinstance(x, str))].index, inplace=True)
        print(historial)
        historial.drop(["Open","High"],axis=1,inplace=True)
        self.ax.cla()
        
        #self.ax.legend(['Close**'])
        self.ax.set_xlabel("Fecha")
        historial.plot(ax=self.ax,color='blue')
        self.graph.draw()
        
    def close_app(self):
        # Se muestra una ventana emergente para confirmar la salida de la aplicacion
        if askokcancel("Salir", "Desea salir de la aplicacion?"):
            self.master.destroy()            

root = tk.Tk()
app = App(root)
root.mainloop()