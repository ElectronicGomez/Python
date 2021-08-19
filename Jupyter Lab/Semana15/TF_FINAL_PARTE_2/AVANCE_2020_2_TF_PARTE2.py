
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
import socket
from tkinter.messagebox import showerror
import datetime

HEADER_SIZE = 10


class Client:
    def __init__(self, address, port, username):
        self.address = address
        self.port = port
        self.username = username
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.address, self.port))
    
    def envia(self, DATA):
        data_len = len(DATA + self.username + "> ")
        self.sock.send(f"{data_len:<{HEADER_SIZE}}{self.username}> {DATA}".encode('utf-8'))
        
        return None
    
    
    def recibe(self):
        data_header = self.sock.recv(HEADER_SIZE)
        
        if not data_header:
            return False
        data = self.sock.recv(int(data_header))
        
        return data.decode('utf-8')

class SerialChat:
    def __init__(self, master):
        self.master = master
        self.PORT = "COM1"
        
        self.master.title(f"Chat TCP/IP")
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
        self.namemodificado = StringVar()
        self.namemodificado.set("Nickname")
        
        self.address = StringVar(value=socket.gethostbyname(socket.gethostname()))
        self.puerto = IntVar(value=2000)
        self.id = StringVar()
        self.client = None
        self.var_enviar = False
        
        self.labelestado.set("Desconectado")
        self.puertoconectado.set("no se detecta IP")
        self.status.set("Sin conexión")
        # ---------------------- SERIAL PORT --------------------------
        ports = serial.tools.list_ports.comports()
        self.port_list = []
        for port in ports:
            self.port_list.append(port.device)
        #print(self.port_list)
        
        
        # ------------------------ FRAMES -----------------------------
        self.frm1 = tk.LabelFrame(self.master, text="Conexion")
        self.frm2 = tk.Frame(self.master)
        self.frm3 = tk.LabelFrame(self.master, text="Enviar mensaje")
        self.frm1.pack(padx=5, pady=5, anchor=tk.W)
        self.frm2.pack(padx=5, pady=5, fill='y', expand=True)
        self.frm3.pack(padx=5, pady=5)
        
        # ------------------------ FRAME 1 ----------------------------
    
        
        self.lblip = tk.Label(self.frm1, text="Dirección IP:") 
#        self.cboPort = ttk.Combobox(frm1, values=self.port_list, textvariable=self.port_select1,state="readonly")
        self.inip = tk.Entry(self.frm1, textvariable=self.address, width=15,state="readonly")
#        self.cboPort.set("Ninguno")
        
        self.lblpuerto = Label(self.frm1, text=" Host :")
        self.inpuerto = tk.Entry(self.frm1, textvariable=self.puerto, width=15,state="readonly")
        
        self.lblid = Label(self.frm1, text=" Id de Usuario:")
        self.lblname = Label(self.frm1, textvariable = self.namemodificado)
        
        
        self.lblmore = Label(self.frm1, text="IP conectado: ", font='Verdana 8')
        self.lblcom = Label(self.frm1, textvariable=self.puertoconectado)
        self.lblestado = Label(self.frm1, textvariable=self.labelestado)
        self.lbltitulo = Label(self.frm1, text = "Estado:")
        
        
        self.lblSpace = tk.Label(self.frm1, text="")
        self.btnConnect = ttk.Button(self.frm1, text="Conectar", width=16, command=self.conexion)
        self.btnid = ttk.Button(self.frm1, text = "Cambiar id", command=self.cambiarnickname)
        
        self.lblip.grid(row=0, column=0, padx=5, pady=5)
#        self.cboPort.grid(row=0, column=1, padx=5, pady=5)
        self.inip.grid(row=0, column=1, padx=5, pady=5)
        self.lblSpace.grid(row=0,column=2, padx=30, pady=5)
        self.btnConnect.grid(row=0, column=3, padx=5, pady=5)
        
        self.lblpuerto.grid(row=1, column=0, padx=5, pady=5)
        self.inpuerto.grid(row=1, column=1, padx=5, pady=5)
        
        self.lblid.grid(row=2, column=0, padx=5, pady=5)
        self.lblname.grid(row=2, column=1, padx=5, pady=5)
        self.btnid.grid(row=2, column=2, padx=5, pady=5)
        
        
        self.lblmore.grid(row=3, column=0, padx=5, pady=5)
        self.lblcom.grid(row=3, column=1, padx=5, pady=5)
        self.lbltitulo.grid(row=3, column=2, padx=5, pady=5)
        self.lblestado.grid(row=3, column=3, padx=5, pady=5)
        # ------------------------ FRAME 2 ---------------------------
        self.txtChat = ScrolledText(self.frm2, height=20, width=50, wrap=tk.WORD, state='disable', bg='#A3E4D7',font="bold")
        
        self.txtChat.grid(row=0, column=0, columnspan=3, padx=5, pady=5)
        
                
        # ------------------------ FRAME 3 --------------------------
        self.lblText = tk.Label(self.frm3, text="Texto:")
        self.inText = tk.Entry(self.frm3, width=45,textvariable=self.envia1,state='disable')
       
        
        self.btnSend = ttk.Button(self.frm3, text="Enviar", width=12, command=lambda: self.tiempo_enviar(None), state='disable')
        
        
        
        self.lblText.grid(row=0, column=0, padx=5, pady=5)
        self.inText.grid(row=0, column=1, padx=5, pady=5)
        self.btnSend.grid(row=0, column=2, padx=5, pady=5)
        
        
        #----------------------------binds--------------------------
        self.inText.bind("<Return>", self.tiempo_enviar)
        
        
        # --------------------------- StatusBar -----------------------
        self.statusBar = tk.Label(self.master,textvariable=self.status, bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.statusBar.pack(side=tk.BOTTOM, fill=tk.X)
        
        
        
        
            
        # ------------- Control del boton "X" de la ventana -----------
        
        self.master.protocol("WM_DELETE_WINDOW", self.cerrar_conexion)
    def cambiarnickname(self):
        
        
                    
        if (self.cont2==0):
            self.cont2 = 1
            self.btnid.config(text="Aceptar")
            
            self.lblname.destroy()
            
            
            self.inid = tk.Entry(self.frm1, textvariable=self.id, width=15,state="normal")
            self.inid.grid(row=2, column=1, padx=5, pady=5)            
            self.inid.bind("<Return>",lambda event:self.cambiarnickname())
            
            
        elif (self.cont2==1):
            self.cont2 = 0
            if self.inid.get()=='':
                self.cont2=1
                showerror("Error de usuario","Ingrese un id de usuario")
            else:
                
                
                self.btnid.config(text="Cambiar")
                
                
                self.namemodificado.set(self.inid.get())
                self.inid.destroy()
                
                
                
                self.lblname = Label(self.frm1, textvariable = self.namemodificado)
                self.lblname.grid(row=2, column=1, padx=5, pady=5)
                self.th2 = threading.Thread(target=self.hilito2, daemon=True)
                self.th2.start()
           
#        self.master.after(10,self.hilito2)
#        self.cliente = Client(self.address.get(), self.puerto.get(), self.namemodificado.get())
#                    
    
    def cerrar_conexion(self):
        # Se cierran los puertos COM y la ventana de tkinter
        try: 
            self.cliente.sock.close()
            
        except:pass
        
        self.master.destroy()

    
    def conexion(self):
        print("cont= ",self.cont)
        if self.cont==0:
#            print(self.cont2)
            print(self.address.get())
            print(self.puerto.get())
            print(self.namemodificado.get())
            self.cont=1
                    
            if self.address.get() and self.puerto.get() and self.namemodificado.get() and self.cont2==0 :
                
                try:
                    
                    print("hola\n")
                    self.cliente = Client(self.address.get(), self.puerto.get(), self.namemodificado.get())
                    
                    self.inText.config(state='normal')
                    self.btnSend.config(state='normal')
                    self.btnConnect.config(text='Desconectar')
                    self.txtChat.insert(tk.INSERT,self.envia1.get() + "\n",'color')
                    self.txtChat.tag_config('color', foreground="green")
                    self.txtChat.config(state='disable')
                    self.status.set("Conexión establecida")
                    self.puertoconectado.set(self.address.get())
                    self.labelestado.set("Conectado")
                    
                    
                    
                    
                except:
                    showerror("Error de conexion", "El servicio de Chat no esta disponible")
                    
            else:
                self.cont=0
                showerror("Error de user", "Ingrese un id de usuario y luego click en Aceptar")
                
                

                
                
            
            self.th = threading.Thread(target=self.hilito, daemon=True)
            self.th.start()
            
            
            
            
            
        elif self.cont==1:
            print("Desconectar: cont= ",self.cont)
#            self.inip.config(state='readonly')
#            self.inpuerto.config(state='readonly')
           
            self.inText.config(state='disable')
            self.btnSend.config(state='disable')
            self.btnConnect.config(text='Conectar')
            self.txtChat.config(state='disable')
            self.status.set("Sin conexión")
            self.status.set("Conexión Cerrada")
            self.labelestado.set("Desconectado")
            self.cont = 0
            self.cliente.sock.close()
    
    def tiempo_enviar(self,handle):
        self.status.set("Enviando mensaje...")
        self.master.after(1000,self.send_mensaje) 
        
    def mensaje_enviado(self):
#        self.status.set("Mensaje enviado")
        self.master.after(10,self.mensaje_enviado) 
       
    def enviado(self):
        horita = datetime.datetime.now()
        self.status.set(f"Mensaje enviado a los demas usuarios a las {horita.hour}:{horita.minute}:{horita.second}")
#        return None
    def send_mensaje(self):
        print(self.namemodificado.get())

        
#        self.status.set("Mensaje enviado")
        
#        self.txtChat.insert(tk.INSERT, self.envia1.get() + "\n",'verde')
#        self.txtChat.tag_config('verde', foreground="green")
        
        if self.cont==1 and self.envia1.get() and not self.var_enviar:
            self.cliente = Client(self.address.get(), self.puerto.get(), self.namemodificado.get())
            self.var_enviar = True
            
            self.cliente.envia(self.envia1.get())
#            self.txtChat.insert(tk.END)
#            self.status.set("Enviando mensaje...")
            print("====")
#            time.sleep(1)
            self.master.after(1000,self.enviado)
            
            self.envia1.set("")
#        self.inText.delete(0,'end')
    def hilito(self):
        self.recepcion()
        
    def hilito2(self):
        self.send_mensaje()
    
    def mensaje_recibido(self):
#        self.status.set("Recibiendo mensaje...")
        print("espera")
#        time.sleep(1)
        self.status.set("Mensaje recibido")
#        self.master.after(10,self.recepcion)
        
    def recibiendo(self):
#        self.status.set("Recibiendo mensaje...")
#        time.sleep(1)
        horita2 = datetime.datetime.now()
        self.status.set(f"Ha recibido un mensaje a las {horita2.hour}:{horita2.minute}:{horita2.second}")
        
    def recepcion(self):
        self.hora.set(time.strftime("%H:%M:%S"))
        self.fecha.set(time.strftime("%d/%m/%y"))
        while self.cont==1:
            try:
                MENSAJEENTRANTE = self.cliente.recibe()
                
                if MENSAJEENTRANTE == False:
                    self.cliente.sock.close()
                    self.inip.config(state='normal')
                    self.inpuerto.config(state='normal')
                    self.inid.config(state='normal')
                    self.btnConectar.config(text='Conectar')
                    self.txtChat.config(state='normal')
                    
                    self.txtChat.config(state='disable')
                    self.cont = 0
                else:
                    self.txtChat.config(state='normal')
                    
                    self.txtChat.insert(tk.INSERT, str(self.fecha.get())+" - "+str(self.hora.get())+ "\n",'rojo')
                    
                    self.txtChat.insert(tk.INSERT, MENSAJEENTRANTE + "\n\n",'color2')
                    self.txtChat.tag_config('color2', foreground="#2B9346")
#                    self.status.set("Mensaje enviado y/o recibido")
                    
#                    self.mensaje_enviado()
                    self.txtChat.see(tk.END)
                    self.txtChat.config(state='disable')
                    
                    if self.var_enviar == False:
                        
                        print("aaaaaaa")
                        self.status.set("Recibiendo mensaje...")
#                        time.sleep(1)
#                        self.status.set(f"Ha recibido un mensaje a las {horita2.hour}:{horita2.minute}:{horita2.second}")

                        self.master.after(1000, self.recibiendo)
                    else:
                        self.statusBar.config(text="Recibiendo mensaje...")
                        
                    self.var_enviar=False
#                    self.master.after(10,self.hilito2)
#                    self.cliente = Client(self.address.get(), self.puerto.get(), self.namemodificado.get())
               
                    
                    
            except:
                break
    
            
        
        self.master.after(10,self.hilito2)
        
            
root = tk.Tk()
app = SerialChat(root)
root.mainloop()


