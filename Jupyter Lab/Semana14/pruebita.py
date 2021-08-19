# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 18:30:52 2020

@author: josed
"""
#%%
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.scrolledtext import ScrolledText
from tkinter import Label, Frame, Button, LabelFrame, Tk, StringVar
import serial
import threading
import time
import threading
class SerialChat:
    def __init__(self, master):
        self.master = master
        self.mensaje=StringVar(value='')
        self.puerto=StringVar(value='COM1')
        self.ser=""
        self.cont=0
        self.master.title(f"Serial Chat")
        self.master.geometry("+50+50")
        self.master.resizable(0, 0)
        
        # ---------------------- SERIAL PORT --------------------------
        self.serial = None
        self.select_puerto = StringVar()
        self.select_puerto.set("Seleccione puerto")
        
        # PUERTO:
        puertitos = serial.tools.list_ports.comports()
        self.listita = []
        for item in puertitos:
            self.listita.append(item.device)
        
        # ------------------------ FRAMES -----------------------------
        frm1 = tk.LabelFrame(self.master, text="Conexion")
        frm2 = tk.Frame(self.master)
        frm3 = tk.LabelFrame(self.master, text="Enviar mensaje")
        frm1.pack(padx=5, pady=5, anchor=tk.W)
        frm2.pack(padx=5, pady=5, fill='y', expand=True)
        frm3.pack(padx=5, pady=5)
        
        # ------------------------ FRAME 1 ----------------------------
        self.lblCOM = tk.Label(frm1, text="Puerto COM:") 
#        self.cboPort = ttk.Combobox(frm1, values=['COM1', 'COM2','COM3','COM4'],textvariable=self.puerto )
        self.cboPort = ttk.Combobox(frm1, values=self.listita, textvariable=self.select_puerto, state ="readonly")
        
        self.lblSpace = tk.Label(frm1, text="")
        self.btnConnect = ttk.Button(frm1, text="Conectar", width=16,command=self.conectar)
        self.lblCOM.grid(row=0, column=0, padx=5, pady=5)
        self.cboPort.grid(row=0, column=1, padx=5, pady=5)
        self.lblSpace.grid(row=1,column=1, padx=25, pady=5)
        self.btnConnect.grid(row=0, column=3, padx=5, pady=5)
        
        # ------------------------ FRAME 2 ---------------------------
        self.txtChat = ScrolledText(frm2, height=25, width=50, wrap=tk.WORD)
        self.txtChat.grid(row=0, column=0, columnspan=3, padx=5, pady=5)
                
        # ------------------------ FRAME 3 --------------------------
        self.lblText = tk.Label(frm3, text="Texto:")
        self.inText = tk.Entry(frm3, width=45, state='normal',textvariable=self.mensaje)
        self.btnSend = ttk.Button(frm3, text="Enviar", width=12, state='normal', command=self.envio_data)
        self.lblText.grid(row=0, column=0, padx=5, pady=5)
        self.inText.grid(row=0, column=1, padx=5, pady=5)
        self.btnSend.grid(row=0, column=2, padx=5, pady=5)
               
        # --------------------------- StatusBar -----------------------
        self.statusBar = tk.Label(self.master, bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.statusBar.pack(side=tk.BOTTOM, fill=tk.X)
            
        # ------------- Control del boton "X" de la ventana -----------
        #self.master.protocol("WM_DELETE_WINDOW", self.cerrar_puertos)
        
        
#        thr1 = threading.Thread(target=self.recibo_data, daemon=True)
#        thr1.start()
#        thr2 = threading.Thread(target=self.envio_data, daemon=True)
#        thr2.start()
#    def conexion(self):
#        PORT = self.puerto.get()
#        print("1")         
#        self.ser = serial.Serial(port=PORT, 
#                                baudrate=9600, 
#                                bytesize=8, 
#                                timeout=2, 
#                                stopbits=serial.STOPBITS_ONE)
#        self.master.after(1,self.Empieza_conexion)
#    def Empieza_conexion(self):
#        thr = threading.Thread(target=self.funcion, daemon=True)
#        print("1")
#        thr.start()
        
    
        
    
    def conectar(self):
        
        PORT = self.select_puerto.get()
        print(PORT)
        if self.cont==0:
            self.cont=1
            self.btnConnect.config(text="Desconectar")
             
            try:
                self.ser = serial.Serial(port = PORT,
                        baudrate=9600,
                        bytesize=8,
                        timeout=2,
                        stopbits=serial.STOPBITS_ONE)
                self.lblSpace.config(text=f"Conectado al puerto: {PORT}")

 
            except:
                print(f"puerto {PORT} no disponible")

        elif self.cont==1: 
            self.btnConnect.config(text="Conectar")
            self.cont=0
            self.ser.close()

            self.lblSpace.config(text=f"Desconectado")
            
            
                
    def funcion(self):
        PORT = self.puerto.get()
        self.ser = serial.Serial(port=PORT, 
                                baudrate=9600, 
                                bytesize=8, 
                                timeout=2, 
                                stopbits=serial.STOPBITS_ONE)
        self.master.after(1000,self.funcion)
    def recibo_data(self, evento):
        PORT = self.puerto.get()

        try:
            print(f"Estableciendo {PORT}...")
            
            print("Conexión extablecida")
        
            while True:
                try:
                    # Si hay datos en el butffer de entrada... 
                    if self.ser.in_waiting > 0:
                        # Se leen los datos y se espera el caracter EOL
                        data = self.ser.readline()
                        # Los datos recibidos son bytes. Para verlos es necesarios decodificarlos
                        string = data.decode('utf-8')
                        print(f"Rx: {string}")
                        self.txtChat.configure(state ='normal')
                        self.txtChat.insert(tk.INSERT,f"{PORT}: {string}")
                        self.txtChat.configure(state ='disabled')
                        break
                # Se calcela el programa con CTRL-C desde el terminal
                except KeyboardInterrupt:
                    print("Conexion cerrada")
                    self.ser.close()
                    break
        except:
            print(f"Puerto {PORT} no disponible")
#        PORT = self.puerto.get()
#        
#        
#                    # Si hay datos en el butffer de entrada...
#        print(f"Estableciendo comunicación  {PORT}...")
#        if self.ser.in_waiting > 0:
#                        # Se leen los datos y se espera el caracter EOL
#            data = self.ser.readline()
#                        # Los datos recibidos son bytes. Para verlos es necesarios decodificarlos
#            string = data.decode('utf-8')
#            print(f"Rx: {string}")
#            self.txtChat.configure(state ='normal')
#            self.txtChat.insert(tk.INSERT,f"{PORT}: {string}")
#            self.txtChat.configure(state ='disabled')
#                # Se calcela el programa con CTRL-C desde el terminal
#            
        
    def envio_data(self):
        PORT = self.puerto.get()

        try:
            
            while True:
                # Se ingresa el texto a enviar por el puerto
                string = self.mensaje.get()
                # Se define una palabra para cerrar el puerto
                if string == "END":
                    break
                else:
                    # Se codifica como bytes el texto a enviar y se envia por el puerto
                    data = string.encode("utf-8")
                    self.ser.write(data)
                    self.txtChat.configure(state ='normal')
                    self.txtChat.insert(tk.INSERT,f"{PORT}: {string}")
                    self.txtChat.configure(state ='disabled')
                    break
            print("Conexion cerrada")
            self.ser.close()
        except:
            print(f"Puerto {PORT} no disponible")
#        try:    
#            PORT = self.puerto.get()
#                    # Se ingresa el texto a enviar por el puerto
#                    
#            string = self.mensaje.get()
#                    # Se define una palabra para cerrar el puerto
#            
#            
#                        # Se codifica como bytes el texto a enviar y se envia por el puerto
#            print(f"Estableciendo comunicación con puerto serial {PORT}...")
#            print(f"{string}")
#            data = string.encode("utf-8")
#            self.ser.write(data)
#            self.txtChat.configure(state ='normal')
#            self.txtChat.insert(tk.INSERT,f"{PORT}: {string}")
#            self.txtChat.configure(state ='disabled') 
#                
#            print("Conexion cerrada")
#            self.ser.close()
#        except:
#            print(f"Puerto {PORT} no disponible")
    def cerrar_puertos(self):
        # Se cierran los puertos COM y la ventana de tkinter
        try:
            pass
            #self.serial.close()
        except:
            pass

        self.master.destroy()
    
    
root = tk.Tk()
app = SerialChat(root)
root.mainloop()
    