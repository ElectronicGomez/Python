# -*- coding: utf-8 -*-
#%%
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.scrolledtext import ScrolledText
import serial
import threading
from tkinter import *
import time
import textwrap
import serial.tools.list_ports

class Chat_personal:
    def __init__(self,master):
        self.master = master
        self.master.title("Serial chat")
        self.master.resizable(0, 0)
        self.master.geometry("+200+20")
        self.cont = 0
        #objetos
        self.chat1 = ''
        self.port_select1 = StringVar()
        self.envia1 = StringVar()
        self.status = StringVar()
        self.status.set("Sin conexión")    
        
        
        
        frm1 = tk.LabelFrame(self.master, text="Usuario")
        frm1.pack(padx=10, pady=5, anchor=tk.W)
        frm2 = tk.LabelFrame(self.master, text="Enviar mensaje")
        frm2.pack(padx=5, pady=5, fill='y', expand=True)
        ports = serial.tools.list_ports.comports()
        self.port_list = []
        for port in ports:
            self.port_list.append(port.device)
        
        
        # -------------------- frm1 -----------------------
        self.lblPort1 = Label(frm1, text="Puerto COM:")
        self.cboCOM1 = ttk.Combobox(frm1, values=self.port_list, textvariable=self.port_select1, state="readonly")
      
        self.cboCOM1.set("Ninguno")
        self.btnConn1 = Button(frm1, text="Conectar", width=12, command=self.conectar,bg='white')
        self.text1 = ScrolledText(frm1, width=50, height=30, state="disabled")
        self.lblText1 = Label(frm2, text="Texto:")
        self.inText1 = Entry(frm2, width=40, textvariable=self.envia1, state= "disabled")
        self.btnEnviar1 = Button(frm2, text="Enviar", width=12, command=self.envia_mensaje1, state="disabled")
        
        self.text1.insert(END, self.chat1)
#        self.lblSpace = tk.Label(frm1, text="")
        
        
        self.lblPort1.grid(row=0, column=0, padx=5, pady=5)
        self.cboCOM1.grid(row=0, column=1, padx=5, pady=5)
#        self.lblSpace.grid(row=0,column=2, padx=30, pady=5)
        self.btnConn1.grid(row=0, column=2, padx=5, pady=5)
        self.text1.grid(row=1, column=0, columnspan=3, padx=5, pady=5)
        
        self.lblText1.grid(row=0, column=0, padx=5, pady=5)
        self.inText1.grid(row=0, column=1, padx=5, pady=5)
        self.btnEnviar1.grid(row=0, column=2, padx=5, pady=5)
        
        # Manejo del boton "X" de la ventana en Windows
        self.master.protocol("WM_DELETE_WINDOW", self.closing)
        
        # --------------------------- StatusBar -----------------------
        self.statusBar = tk.Label(self.master,textvariable=self.status, bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.statusBar.pack(side=tk.BOTTOM, fill=tk.X)        

    def conectar(self):
        if self.cont==0:
            self.cont=1
          
            self.btnConn1.config(text="Desconectar")
                        
            try:
                self.ser1 = serial.Serial(port=self.port_select1.get(), timeout=2)
                self.status.set("Conexión establecida")
                self.btnEnviar1.config(state="normal")
                self.inText1.config(state="normal")
                self.text1.config(state="readonly")
                            
            except:
                self.text1.insert(END, "No se pudo realizar la conexion"+ '\n')
                
            th = threading.Thread(target=self.Response_loop, daemon=True)
            th.start()
            
            
            
        elif self.cont==1:
            self.btnConn1.config(bg='white')
            self.btnConn1.config(text="Conectar")
            self.cont=0
            self.ser1.close()
            self.status.set("Conexión cerrada")
            self.btnEnviar1.config(state="disabled")
            self.inText1.config(state="disabled") 
            self.text1.config(state="disabled")
                            
            
            
            
                
    def envia_mensaje1(self):
        
        try:
            
            
            data = ( self.cboCOM1.get() +": "+self.envia1.get()).encode('utf-8')
            self.status.set("Mensaje enviado")
            self.text1.config(state="normal")
            
            #se envia la data por el puerto
            self.ser1.write(data)
            self.text1.insert('end', self.cboCOM1.get() +": "+self.chat1 + self.envia1.get() + '\n')
            self.text1.config(state="disabled")
            
           
            self.envia1.set('')
        except:
            self.text1.insert(END, "No hay conexion a puertos"+ '\n')
    
    def Response_loop(self):
        self.Recibe_dato()
    def Recibe_dato(self):
        if self.ser1.in_waiting > 0:
            data2 = self.ser1.readline()
            self.status.set("Mensaje recibido")
            self.text1.config(state="normal")
            strSerial = data2.decode('utf-8')
            self.text1.insert(END, self.chat1 + strSerial + '\n')
            self.text1.config(state="disabled")
#            
        self.master.after(100, self.Response_loop)
    
    def closing(self):
        #cierra puertos seriales
        try:
            if self.ser1.is_open==True:
                self.ser1.close()
            else:
                pass
            self.master.destroy()
        except:
            self.master.destroy()
    
        
root = tk.Tk()
app = Chat_personal(root)
root.mainloop()