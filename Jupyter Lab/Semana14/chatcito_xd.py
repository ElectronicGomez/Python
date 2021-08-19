
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

class SerialChat:
    def __init__(self, master):
        self.master = master
        self.PORT = "COM1"
        
        self.master.title(f"Serial Chat")
        self.master.geometry("+50+50")
        self.master.resizable(0, 0)
        
        self.cont = 0
        self.cont2 = 0
        #-------------------------- objetos --------------------
        self.chat1 = ''
        self.port_select1 = StringVar()
        self.envia1 = StringVar()
        self.puertoconectado = StringVar()
        self.nickname = StringVar()
        self.namemodificado = StringVar()
        self.status = StringVar()
        self.labelestado = StringVar()
        self.hora = StringVar()        
        self.fecha = StringVar()
        
        self.labelestado.set("Desconectado")
        self.puertoconectado.set("Sin puerto")
        self.status.set("Sin conexión")
        # ---------------------- SERIAL PORT --------------------------
        ports = serial.tools.list_ports.comports()
        self.port_list = []
        for port in ports:
            self.port_list.append(port.device)
        #print(self.port_list)
        
        
        # ------------------------ FRAMES -----------------------------
        frm1 = tk.LabelFrame(self.master, text="Conexion")
        frm2 = tk.Frame(self.master)
        frm3 = tk.LabelFrame(self.master, text="Enviar mensaje")
        frm1.pack(padx=5, pady=5, anchor=tk.W)
        frm2.pack(padx=5, pady=5, fill='y', expand=True)
        frm3.pack(padx=5, pady=5)
        
        # ------------------------ FRAME 1 ----------------------------
    
        
        self.lblCOM = tk.Label(frm1, text="Puerto COM:") 
        self.cboPort = ttk.Combobox(frm1, values=self.port_list, textvariable=self.port_select1)
        self.cboPort.set("Ninguno")
        
        self.lblmore = Label(frm1, text="Puerto conectado: ", font='Verdana 8')
        self.lblcom = Label(frm1, textvariable=self.puertoconectado)
        self.lblestado = Label(frm1, textvariable=self.labelestado)
        self.lbltitulo = Label(frm1, text = "Estado:")
        
        
        self.lblSpace = tk.Label(frm1, text="")
        self.btnConnect = ttk.Button(frm1, text="Conectar", width=16, command=self.conectar)
        self.lblCOM.grid(row=0, column=0, padx=5, pady=5)
        self.cboPort.grid(row=0, column=1, padx=5, pady=5)
        self.lblSpace.grid(row=0,column=2, padx=30, pady=5)
        self.btnConnect.grid(row=0, column=3, padx=5, pady=5)
        
        self.lblmore.grid(row=1, column=0, padx=5, pady=5)
        self.lblcom.grid(row=1, column=1, padx=5, pady=5)
        self.lbltitulo.grid(row=1, column=2, padx=5, pady=5)
        self.lblestado.grid(row=1, column=3, padx=5, pady=5)
        # ------------------------ FRAME 2 ---------------------------
        self.txtChat = ScrolledText(frm2, height=25, width=50, wrap=tk.WORD, state='disable')
        self.txtChat.grid(row=0, column=0, columnspan=3, padx=5, pady=5)
        
                
        # ------------------------ FRAME 3 --------------------------
        self.lblText = tk.Label(frm3, text="Texto:")
        self.inText = tk.Entry(frm3, width=45,textvariable=self.envia1,state='disable')
       
        
        self.btnSend = ttk.Button(frm3, text="Enviar", width=12,command=self.envia_mensaje1, state='disable')
        
        
        
        self.lblText.grid(row=0, column=0, padx=5, pady=5)
        self.inText.grid(row=0, column=1, padx=5, pady=5)
        self.btnSend.grid(row=0, column=2, padx=5, pady=5)
        
        
        
        # --------------------------- StatusBar -----------------------
        self.statusBar = tk.Label(self.master,textvariable=self.status, bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.statusBar.pack(side=tk.BOTTOM, fill=tk.X)
        
        
            
        # ------------- Control del boton "X" de la ventana -----------
        self.master.protocol("WM_DELETE_WINDOW", self.cerrar_puertos)
    
    
    def cerrar_puertos(self):
        # Se cierran los puertos COM y la ventana de tkinter
        try:
            if self.ser1.is_open==True:
                self.ser1.close()
            else:
                pass
            self.master.destroy()
        except:
            self.master.destroy()

    
    def conectar(self):
        self.puertoconectado.set(self.cboPort.get())
        PORT = self.cboPort.get()
        print(self.cont)
        self.inText.config(state='normal')
        self.btnSend.config(state='normal')
        if self.cont==0:
            self.cont=1
            self.btnConnect.config(text="Desconectar")
             
            try:
                self.ser1 = serial.Serial(port = PORT,
                        baudrate=9600,
                        bytesize=8,
                        timeout=2,
                        stopbits=serial.STOPBITS_ONE)
                self.labelestado.set("Conectado")
                self.status.set("Conexión establecida")
                self.txtChat.config(state='normal')
 
            except:
                print(f"puerto {PORT} no disponible")

                
                
                
            th = threading.Thread(target=self.Response_loop, daemon=True)
            th.start()
            
        elif self.cont==1:
            self.btnConnect.config(text="Conectar")
            self.cont=0
            self.ser1.close()
#            self.text1.insert(END, "Conexion cerrada"+ '\n')
            self.labelestado.set("Desconectado")
            
            self.puertoconectado.set("Sin puerto")
           
            self.status.set("Sin conexión")
            self.inText.config(state='disabled')
            self.btnSend.config(state='disabled')
            self.txtChat.config(state='disabled')
           
    def envia_mensaje1(self):
        
        try:
            
           

            #Port 1 envia y port2 recibe
            data = ("  "+ self.cboPort.get() +": "+self.envia1.get()).encode('utf-8')
            
            #se envia la data por el puerto
            self.ser1.write(data)
            self.status.set("Mensaje enviado")
#            self.status.set("Connected")
           
            self.txtChat.insert('end', str(self.fecha.get())+" - "+str(self.hora.get())+ "\n")
            
            self.txtChat.insert('end',"  "+ self.cboPort.get() +": "+self.chat1 + self.envia1.get() + '\n'+ '\n')

            
            
            
            #   Recibir
           
            self.envia1.set('')
        except:
            #self.text1.insert(END, "No hay conexion a puertos"+ '\n')
            self.labelestado.set("No hay conexion a puertos")
            
    def Response_loop(self):
        self.Recibe_dato()
    
    
    def Recibe_dato(self):
        self.hora.set(time.strftime("%H:%M:%S"))
        self.fecha.set(time.strftime("%d/%m/%y"))
          
        if self.ser1.in_waiting > 0:
            self.status.set("Recibido")
            
            
            #Se leen los datos y se espera el caracter en offline
            #readline: lee una trama y espera un back slash n (\n)
            data2 = self.ser1.readline()
            #La data es binaria (en str). Se tiene qu decodificar
            extr = data2.decode('utf-8') #decode: cambia la codificacion de lo que haya llgado: Convertir esos bytes de string a string literales
            print(f"Rx: {extr}")
            self.txtChat.insert(tK.END, str(self.fecha.get())+" - "+str(self.hora.get())+ "\n")
            
            self.txtChat.insert(tk.END, extr + '\n'+ '\n')
            
        self.master.after(10, self.Response_loop)
            
root = tk.Tk()
app = SerialChat(root)
root.mainloop()


