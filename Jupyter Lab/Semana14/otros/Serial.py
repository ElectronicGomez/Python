# -*- coding: utf-8 -*-
"""
Created on FRI Nov 08 15:47:18 2019

"""

#%%
from tkinter import Tk, Label, Entry, Button
from tkinter.ttk import Combobox, Labelframe
from tkinter.scrolledtext import ScrolledText
import serial.tools.list_ports
import serial
#import threading
from tkinter import *

class ChatApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Chat Serial")
        self.master.resizable(0, 0)
        self.cont = 0
        self.cont2 = 0
        #objetos
        self.chat1 = ''
        self.chat2 = ''
        self.port_select1 = StringVar()
        self.port_select2 = StringVar()
        self.envia1 = StringVar()
        self.envia2 = StringVar()
        global ser1
        global ser2
        
        frm1 = Labelframe(self.master, text="Usuario 1")
        frm2 = Labelframe(self.master, text="Usuario 1")
        frm1.pack(side='left', padx=10, pady=10)
        frm2.pack(side='left', padx=10, pady=10)
        
        ports = serial.tools.list_ports.comports()
        self.port_list = []
        for port in ports:
            self.port_list.append(port.device)
        
        
        # -------------------- frm1 -----------------------
        self.lblPort1 = Label(frm1, text="Puerto:")
        self.cboCOM1 = Combobox(frm1, values=self.port_list, textvariable=self.port_select1)
        self.btnConn1 = Button(frm1, text="Conectar", width=12, command=self.conectar,bg='white')
        self.text1 = ScrolledText(frm1, width=40, height=30)
        self.lblText1 = Label(frm1, text="Texto:")
        self.inText1 = Entry(frm1, width=40, textvariable=self.envia1)
        self.btnEnviar1 = Button(frm1, text="Enviar", width=12, command=self.envia_mensaje1)
        
        self.text1.insert(END, self.chat1)
        
        self.lblPort1.grid(row=0, column=0, padx=5, pady=5)
        self.cboCOM1.grid(row=0, column=1, padx=5, pady=5)
        self.btnConn1.grid(row=0, column=2, padx=5, pady=5)
        self.text1.grid(row=1, column=0, columnspan=3, padx=5, pady=5)
        self.lblText1.grid(row=2, column=0, padx=5, pady=5)
        self.inText1.grid(row=2, column=1, padx=5, pady=5)
        self.btnEnviar1.grid(row=2, column=2, padx=5, pady=5)
    
        
        # -------------------- frm2 -----------------------
        self.lblPort2 = Label(frm2, text="Puerto:")
        self.cboCOM2 = Combobox(frm2, values=self.port_list,textvariable=self.port_select2)
        self.btnConn2 = Button(frm2, text="Conectar", width=12, command=self.conectar2,bg='white')
        self.text2 = ScrolledText(frm2, width=40, height=30)
        self.lblText2 = Label(frm2, text="Texto:")
        self.inText2 = Entry(frm2, width=40, textvariable=self.envia2)
        self.btnEnviar2 = Button(frm2, text="Enviar", width=12, command=self.envia_mensaje2)
        
        self.text2.insert(END, self.chat2)
        
        self.lblPort2.grid(row=0, column=0, padx=5, pady=5)
        self.cboCOM2.grid(row=0, column=1, padx=5, pady=5)
        self.btnConn2.grid(row=0, column=2, padx=5, pady=5)
        self.text2.grid(row=1, column=0, columnspan=3, padx=5, pady=5)
        self.lblText2.grid(row=2, column=0, padx=5, pady=5)
        self.inText2.grid(row=2, column=1, padx=5, pady=5)
        self.btnEnviar2.grid(row=2, column=2, padx=5, pady=5)

    def conectar(self):
        global ser1
        if self.cont==0:
            self.cont=1
            self.btnConn1.config(bg='#A9A9A9')
            self.btnConn1.config(text="Desconectar")
                        
            try:
                ser1 = serial.Serial(port=self.port_select1.get(), timeout=2)
                self.text1.insert(END, "Conexion establecida"+ '\n')
            #    print("Conexion establecida")
                
            
                    
            except:
            #    print(f"No se puede abrir el puerto {self.port_select1.get()}")
                self.text1.insert(END, "No se pudo realizar la conexion"+ '\n')
                
            
            
        elif self.cont==1:
            self.btnConn1.config(bg='white')
            self.btnConn1.config(text="Conectar")
            self.cont=0
            ser1.close()
            self.text1.insert(END, "Conexion cerrada"+ '\n')
            
    def conectar2(self):
        global ser2
        if self.cont2==0:
            self.cont2=1
            self.btnConn2.config(bg='#A9A9A9')
            self.btnConn2.config(text="Desconectar")
            try:
                ser2 = serial.Serial(port=self.port_select2.get(), timeout=2)
                self.text2.insert(END, "Conexion establecida"+ '\n')
            except:
                self.text2.insert(END, "No se pudo realizar la conexion"+ '\n')
            
        elif self.cont2==1:
            self.btnConn2.config(bg='white')
            self.btnConn2.config(text="Conectar")
            self.cont2=0
            ser2.close()
            self.text2.insert(END, "Conexion cerrada"+ '\n')
            
    def envia_mensaje1(self):
        
        self.text1.insert(END, '\t \t \t \t'+self.chat1 + self.envia1.get() + '\n')
        
        
        #Port 1 envia y port2 recibe
        
        data = self.envia1.get().encode('utf-8')
        #se envia la data por el puerto
        ser1.write(data)
        #   Recibir
       
        if ser2.in_waiting > 0:
            data2 = ser2.readline()
            strSerial = data2.decode('utf-8')
            self.text2.insert(END, self.chat2 + strSerial + '\n')
              
        self.envia1.set('')
        self.envia2.set('')
        
        
    def envia_mensaje2(self):
               
        self.text2.insert(END,'\t \t \t \t'+ self.chat2 + self.envia2.get() + '\n')
        #self.text2.config(fg='red')
        
        
        #Port 2 envia y port1 recibe
        
        data = self.envia2.get().encode('utf-8')
        #se envia la data por el puerto
        ser2.write(data)
        #   Recibir
      
        if ser1.in_waiting > 0:
            data2 = ser1.readline()
            strSerial = data2.decode('utf-8')
            #print(strSerial)
            self.text1.insert(END, self.chat1 + strSerial + '\n')
                            
           
        self.envia1.set('')
        self.envia2.set('')
        
root = Tk()
app = ChatApp(root)
root.mainloop()
#%%
#Chat serial personal
from tkinter import Tk, Label, Entry, Button
from tkinter.ttk import Combobox, Labelframe
from tkinter.scrolledtext import ScrolledText
import serial.tools.list_ports
import serial
import threading
from tkinter import *

class Chat_personal:
    def __init__(self,master):
        self.master = master
        self.master.title("Chat Serial")
        self.master.resizable(0, 0)
        self.cont = 0
        #objetos
        self.chat1 = ''
        self.port_select1 = StringVar()
        self.envia1 = StringVar()
        
        
        frm1 = Labelframe(self.master, text="Usuario 1")
        frm1.pack(side='left', padx=10, pady=10)
        
        ports = serial.tools.list_ports.comports()
        self.port_list = []
        for port in ports:
            self.port_list.append(port.device)
        
        
        # -------------------- frm1 -----------------------
        self.lblPort1 = Label(frm1, text="Puerto:")
        self.cboCOM1 = Combobox(frm1, values=self.port_list, textvariable=self.port_select1)
        self.btnConn1 = Button(frm1, text="Conectar", width=12, command=self.conectar,bg='white')
        self.text1 = ScrolledText(frm1, width=40, height=30)
        self.lblText1 = Label(frm1, text="Texto:")
        self.inText1 = Entry(frm1, width=40, textvariable=self.envia1)
        self.btnEnviar1 = Button(frm1, text="Enviar", width=12, command=self.envia_mensaje1)
        
        self.text1.insert(END, self.chat1)
        
        self.lblPort1.grid(row=0, column=0, padx=5, pady=5)
        self.cboCOM1.grid(row=0, column=1, padx=5, pady=5)
        self.btnConn1.grid(row=0, column=2, padx=5, pady=5)
        self.text1.grid(row=1, column=0, columnspan=3, padx=5, pady=5)
        self.lblText1.grid(row=2, column=0, padx=5, pady=5)
        self.inText1.grid(row=2, column=1, padx=5, pady=5)
        self.btnEnviar1.grid(row=2, column=2, padx=5, pady=5)
        
        # Manejo del boton "X" de la ventana en Windows
        self.master.protocol("WM_DELETE_WINDOW", self.closing)
        
    def conectar(self):
        if self.cont==0:
            self.cont=1
            self.btnConn1.config(bg='#A9A9A9')
            self.btnConn1.config(text="Desconectar")
                        
            try:
                self.ser1 = serial.Serial(port=self.port_select1.get(), timeout=2)
                self.text1.insert(END, "Conexion establecida"+ '\n')
                            
            except:
                self.text1.insert(END, "No se pudo realizar la conexion"+ '\n')
                
            th = threading.Thread(target=self.Response_loop, daemon=True)
            th.start()
            
            
            
        elif self.cont==1:
            self.btnConn1.config(bg='white')
            self.btnConn1.config(text="Conectar")
            self.cont=0
            self.ser1.close()
            self.text1.insert(END, "Conexion cerrada"+ '\n')
            
                
    def envia_mensaje1(self):
        
        try:
            
                    
            #Port 1 envia y port2 recibe
            data = self.envia1.get().encode('utf-8')
            #se envia la data por el puerto
            self.ser1.write(data)
            self.text1.insert(END, '\t \t \t \t'+self.chat1 + self.envia1.get() + '\n')
            #   Recibir
           
            self.envia1.set('')
        except:
            self.text1.insert(END, "No hay conexion a puertos"+ '\n')
    
    def Response_loop(self):
        self.Recibe_dato()
    def Recibe_dato(self):
        if self.ser1.in_waiting > 0:
            data2 = self.ser1.readline()
            strSerial = data2.decode('utf-8')
            self.text1.insert(END, self.chat1 + strSerial + '\n')
            
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
    
        
root = Tk()
app = Chat_personal(root)
root.mainloop()
    


