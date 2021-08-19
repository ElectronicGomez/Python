# -*- coding: utf-8 -*-
from tkinter import Tk, Label, Entry, Button, Frame, StringVar, INSERT, END
from tkinter.ttk import Combobox, Labelframe
from tkinter.scrolledtext import ScrolledText
import serial.tools.list_ports
import serial
import threading
import tkinter as tk
import emoji
import time

class ChatApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Chat Serial")
        self.master.resizable(0, 0)
        
        frm = Frame(self.master)
        frm.pack(padx=5, pady=5)
        
        frm1 = Labelframe(frm, text="Conexion", width=2)
        frm2 = Frame(frm, width=2)
        frm3 = Labelframe(frm, text="Enviar Mensaje", width=2)  
        frm3_1 = Frame(frm3, width=2) 
        frm3_2 = Frame(frm3, width=2) 
        
        frm1.pack(padx=5, pady=5)
        frm2.pack(padx=5, pady=5)
        frm3.pack(padx=5, pady=5)
        frm3_1.pack(padx=5, pady=10)
        frm3_2.pack(padx=5, pady=1)
        
        self.port_list = []
        ports = serial.tools.list_ports.comports()
        for port in ports:
            self.port_list.append(port.device)
        
         
        # -------------------- frm1 -----------------------
        self.lblPort = Label(frm1, text="Puerto COM:")
        self.cboCOM = Combobox(frm1, values=self.port_list, state="readonly")
        self.btnConn = Button(frm1, text="Conectar", width=12, state="disable", command=self.conectar1)
        
        self.lblPort.grid(row=0, column=0, padx=5, pady=5)
        self.cboCOM.grid(row=0, column=1, padx=5, pady=5)
        self.btnConn.grid(row=0, column=2, padx=(70,5), pady=5)
               
        # -------------------- frm2 -----------------------
        self.text = ScrolledText(frm2, width=49, height=20, state="disable")
        self.text.grid(row=0, column=0, columnspan=3, padx=5, pady=5)
                
        # -------------------- frm3 -----------------------
        self.lblText = Label(frm3_1, text="Texto:")
        
        self.mensaje = StringVar()
        self.inText = Entry(frm3_1, width=40, textvariable=self.mensaje, state="disable")
        self.btnEnviar = Button(frm3_1, text="Enviar", width=12, state="disable", command=self.publicar)
        
        self.lblText.grid(row=0, column=0, padx=5, pady=5)
        self.inText.grid(row=0, column=1, padx=5, pady=5)
        self.btnEnviar.grid(row=0, column=2, padx=5, pady=5)

        self.b1 = PushButton(frm3_2, text=u'\U0001F642', width=4, state="disable", command=lambda:self.inText.insert(INSERT, '\U0001F642'))
        self.b2 = Button(frm3_2, text=u'\U0001F605', width=4, state="disable", command=lambda:self.inText.insert(INSERT, '\U0001F605'))
        self.b3 = Button(frm3_2, text=u'\U0001F606', width=4, state="disable", command=lambda:self.inText.insert(INSERT, '\U0001F606'))
        self.b4 = Button(frm3_2, text=u'\U0001F923', width=4, state="disable", command=lambda:self.inText.insert(INSERT, '\U0001F923'))
        self.b5 = Button(frm3_2, text=u'\U0001F604', width=4, state="disable", command=lambda:self.inText.insert(INSERT, '\U0001F604'))
        self.b6 = Button(frm3_2, text=u'\U0001F609', width=4, state="disable", command=lambda:self.inText.insert(INSERT, '\U0001F609'))
        self.b7 = Button(frm3_2, text=u'\U0001F607', width=4, state="disable", command=lambda:self.inText.insert(INSERT, '\U0001F607'))
        self.b8 = Button(frm3_2, text=u'\U0001F60D', width=4, state="disable", command=lambda:self.inText.insert(INSERT, '\U0001F60D'))
        self.b9 = Button(frm3_2, text=u'\U0001F929', width=4, state="disable", command=lambda:self.inText.insert(INSERT, '\U0001F929'))
        
        self.b1.grid(row=0, column=1, padx=1, pady=1)
        self.b2.grid(row=0, column=2, padx=1, pady=1)
        self.b3.grid(row=0, column=3, padx=1, pady=1)
        self.b4.grid(row=0, column=4, padx=1, pady=1)
        self.b5.grid(row=0, column=5, padx=1, pady=1)
        self.b6.grid(row=0, column=6, padx=1, pady=1)
        self.b7.grid(row=0, column=7, padx=1, pady=1)
        self.b8.grid(row=0, column=8, padx=1, pady=1)
        self.b9.grid(row=0, column=9, padx=1, pady=1)
        
        self.b10 = Button(frm3_2, text=u'\U0001F60B', width=4, state="disable", command=lambda:self.inText.insert(INSERT, '\U0001F60B'))
        self.b11 = Button(frm3_2, text=u'\U0001F62C', width=4, state="disable", command=lambda:self.inText.insert(INSERT, '\U0001F62C'))
        self.b12 = Button(frm3_2, text=u'\U0001F917', width=4, state="disable", command=lambda:self.inText.insert(INSERT, '\U0001F917'))
        self.b13 = Button(frm3_2, text=u'\U0001F914', width=4, state="disable", command=lambda:self.inText.insert(INSERT, '\U0001F914'))
        self.b14 = Button(frm3_2, text=u'\U0001F610', width=4, state="disable", command=lambda:self.inText.insert(INSERT, '\U0001F610'))
        self.b15 = Button(frm3_2, text=u'\U0001F612', width=4, state="disable", command=lambda:self.inText.insert(INSERT, '\U0001F612'))
        self.b16 = Button(frm3_2, text=u'\U0001F614', width=4, state="disable", command=lambda:self.inText.insert(INSERT, '\U0001F614'))
        self.b17 = Button(frm3_2, text=u'\U0001F62A', width=4, state="disable", command=lambda:self.inText.insert(INSERT, '\U0001F62A'))
        self.b18 = Button(frm3_2, text=u'\U0001F637', width=4, state="disable", command=lambda:self.inText.insert(INSERT, '\U0001F637'))
        
        self.b10.grid(row=1, column=1, padx=1, pady=1)
        self.b11.grid(row=1, column=2, padx=1, pady=1)
        self.b12.grid(row=1, column=3, padx=1, pady=1)
        self.b13.grid(row=1, column=4, padx=1, pady=1)
        self.b14.grid(row=1, column=5, padx=1, pady=1)
        self.b15.grid(row=1, column=6, padx=1, pady=1)
        self.b16.grid(row=1, column=7, padx=1, pady=1)
        self.b17.grid(row=1, column=8, padx=1, pady=1)
        self.b18.grid(row=1, column=9, padx=1, pady=1)
        
        
        
        
        
        # ----- Comandos ----
        self.cboCOM.bind("<<ComboboxSelected>>", self.select_puerto)
        self.inText.bind("<Return>", self.publicarE)
        
        # --------------- Control del boton "X" de la ventana ---------------
        self.master.protocol("WM_DELETE_WINDOW", self.cerrar_puertos)
    
         
    
         # ------------------------ Menu inferior ------------------------------
        self.statusBar = Label(self.master, text="", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.statusBar.pack(side=tk.BOTTOM, fill=tk.X)
        
        self.cboCOM.bind("<Enter>", lambda x: self.statusBar.config(text="Seleccione el puerto"))
        self.cboCOM.bind("<Leave>", lambda x: self.statusBar.config(text=""))
        self.btnConn.bind("<Enter>", self.info)
        self.btnConn.bind("<Leave>", lambda x: self.statusBar.config(text=""))
          
        self.text.bind("<Enter>", lambda x: self.statusBar.config(text="Historial de mensajes"))
        self.text.bind("<Leave>", lambda x: self.statusBar.config(text=""))
        self.inText.bind("<Enter>", self.info3)
        self.inText.bind("<Leave>", lambda x: self.statusBar.config(text=""))
        self.btnEnviar.bind("<Enter>", self.info4)
        self.btnEnviar.bind("<Leave>", lambda x: self.statusBar.config(text=""))
        frm3_2.bind("<Enter>", self.info2)
        frm3_2.bind("<Leave>", lambda x: self.statusBar.config(text=""))
    
        self.cont = 0
    def info(self, event):
        if len(self.cboCOM.get())>0:
            if self.cont==1: self.statusBar.config(text="Click para desconectar")
            else: self.statusBar.config(text="Click para conectar")
    def info2(self, event):
        if len(self.cboCOM.get())>0: self.statusBar.config(text="Seleccione un emoji")
    def info3(self, event):
        if len(self.cboCOM.get())>0: self.statusBar.config(text="Escriba su mensaje")
    def info4(self, event):
        if len(self.cboCOM.get())>0: self.statusBar.config(text="Click para enviar")
            
    
    def select_puerto(self, event):
        self.btnConn.config(state="normal")
        self.cont = 0  

    def conectar1(self):
        
        self.cont = self.cont+1
                
        if self.cont==1:
            try:
                PORT = self.cboCOM.get()
                self.ser1 = serial.Serial(port=PORT, baudrate=9600, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)            
                
                print(f"Conexion establecida via {PORT}")
                self.statusBar.config(text=f"Conexion establecida via {PORT}")
                
                self.cboCOM.config(state="disable")
                self.btnConn.config(text="Desconectar")
                self.inText.config(state="normal")
                self.btnEnviar.config(state="normal")
                
                self.b1.config(state="normal")
                self.b2.config(state="normal")
                self.b3.config(state="normal")
                self.b4.config(state="normal")
                self.b5.config(state="normal")
                self.b6.config(state="normal")
                self.b7.config(state="normal")
                self.b8.config(state="normal")
                self.b9.config(state="normal")
                self.b10.config(state="normal")
                self.b11.config(state="normal")
                self.b12.config(state="normal")
                self.b13.config(state="normal")
                self.b14.config(state="normal")
                self.b15.config(state="normal")
                self.b16.config(state="normal")
                self.b17.config(state="normal")
                self.b18.config(state="normal")
                
                
                th1 = threading.Thread(target=self.recibir(), daemon=True)
                th1.start()
                
            except:
                self.cont = self.cont-1
                
                print(f"El puerto {PORT} no esta disponible")
                self.statusBar.config(text=f"El puerto {PORT} no esta disponible")

            
          
        if self.cont==2:
            self.cboCOM.config(state="normal")
            self.btnConn.config(text="Conectar", state="disable")
            self.inText.config(state="disable")
            self.btnEnviar.config(state="disable")
            
            self.b1.config(state="disable")
            self.b2.config(state="disable")
            self.b3.config(state="disable")
            self.b4.config(state="disable")
            self.b5.config(state="disable")
            self.b6.config(state="disable")
            self.b7.config(state="disable")
            self.b8.config(state="disable")
            self.b9.config(state="disable")
            self.b10.config(state="disable")
            self.b11.config(state="disable")
            self.b12.config(state="disable")
            self.b13.config(state="disable")
            self.b14.config(state="disable")
            self.b15.config(state="disable")
            self.b16.config(state="disable")
            self.b17.config(state="disable")
            self.b18.config(state="disable")
                
            self.ser1.close() #desconectar
            
            self.text.config(state="normal")
            self.text.delete("1.0", END) 
            self.text.config(state="disable")
            
            print("Conexion cerrada")
            self.statusBar.config(text="Conexion cerrada")

            self.cboCOM.delete(0, 'end')
     
    def publicar(self):
        
        if len(self.mensaje.get()) !=0: 
                    
            string = f"{self.cboCOM.get()}: " + self.mensaje.get().strip()   + "\n"   
            self.text.config(state="normal")
            self.text.insert(END, string, 'a')
            self.text.tag_config('a', foreground='blue')
            self.text.config(state="disable")
            
            data = string.encode('utf-8')
            self.ser1.write(data)
            
            self.inText.delete(0, 'end')        
            print(string)
            
            self.statusBar.config(text="Enviando mensaje...")
            time.sleep(1)
            self.statusBar.config(text="Mensaje enviado")
            
        self.recibir()
        
    def recibir(self):
        try:
            if self.ser1.in_waiting>0:   
                
                data = self.ser1.readline() 
                print(data)
                print(data.decode('utf-8'))  
                if len(data)>2:
                    
                    string = data.decode('utf-8')
                    
                    self.text.config(state="normal")
                    self.text.insert(END, string, 'b')
                    self.text.tag_config('b', foreground='green')
                    self.text.config(state="disable")
                    print(string)
                    
                    self.statusBar.config(text="Recibiendo mensaje...")
                    time.sleep(1)
                    self.statusBar.config(text="Recibio un mensaje")
        except:
            pass
            
        self.master.after(5000, self.recibir)
        
    
    def publicarE(self, event):
        self.publicar()
 
    
    def cerrar_puertos(self):
        try:
            self.ser1.close()
            print("Conexion cerrada ser1")
        except:
            pass
        self.master.destroy()
        
        
root = Tk()
app = ChatApp(root)
root.mainloop()