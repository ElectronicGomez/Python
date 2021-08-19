# -*- coding: utf-8 -*-
#%%
from tkinter import Tk, Frame, END, StringVar, IntVar
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import Button, Entry, Label, LabelFrame
from tkinter.messagebox import showerror
import socket
import threading

HEADER_SIZE = 10

class Client:
    def __init__(self, direccion_ip, puerto_TCP, usuario_cliente):
        self.direccion_ip = direccion_ip
        self.puerto_TCP = puerto_TCP
        self.usuario_cliente = usuario_cliente
        
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.direccion_ip, self.puerto_TCP))
    
    
    def cliente_recibir_mensaje(self):
        data_header = self.sock.recv(HEADER_SIZE)
        
        if not data_header:
            return False
        
        data = self.sock.recv(int(data_header))
        return data.decode('utf-8')
    
    
    def cliente_enviar_mensaje(self, strData):
        data_len = len(strData + self.usuario_cliente + "> ")
        self.sock.send(f"{data_len:<{HEADER_SIZE}}{self.usuario_cliente}> {strData}".encode('utf-8'))
        return None
    
    
class Chat_servidor_cliente:
    def __init__(self, master):
        self.master = master
        self.master.title("Chat Serial")
        self.master.resizable(0, 0)
        self.master.protocol("WM_DELETE_WINDOW", self.close_app)
        
        self.client = None
        self.connected = False
        
        self.IP = StringVar(value=socket.gethostbyname(socket.gethostname()))
        self.puerto_cliente = IntVar(value=2000)
        self.name_cliente = StringVar()
        self.msj = StringVar()
        self.status = StringVar()
        self.status.set("Sin conexión")
        
        frm1 = LabelFrame(self.master, text="LOGIN")
        frm2 = Frame(self.master)
        frm1.pack(padx=10, pady=10)
        frm2.pack(padx=10, pady=10)
        
        # -------------------------- frm1 -------------------------
        self.lblIP = Label(frm1, text="Server IP")
        self.inServer_ip = Entry(frm1, textvariable=self.IP, width=16)
        self.labelPuerto = Label(frm1, text="puerto_cliente")
        self.inPuerto_server = Entry(frm1, textvariable=self.puerto_cliente, width=12)
        self.labelCliente = Label(frm1, text="name_cliente")
        self.EntryUser = Entry(frm1, textvariable=self.name_cliente, width=16)
        self.btnConnect = Button(frm1, text="Conectar",command=self.connect)
        
        self.lblIP.grid(row=0, column=0, padx=5, pady=5)
        self.inServer_ip.grid(row=0, column=1, padx=5, pady=5)
        self.labelPuerto.grid(row=0, column=2, padx=5, pady=5)
        self.inPuerto_server.grid(row=0, column=3, padx=5, pady=5)
        self.labelCliente.grid(row=0, column=4, padx=5, pady=5)
        self.EntryUser.grid(row=0, column=5, padx=5, pady=5)
        self.btnConnect.grid(row=0, column=6, padx=5, pady=5)
                
        # -------------------------- frm2 -------------------------
        self.Chat = ScrolledText(frm2, width=70)
        self.inText = Entry(frm2, textvariable=self.msj, width=70)
        self.btnSend = Button(frm2, text="Enviar", command=lambda: self.Mensaje_sending(None))
        
        self.Chat.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
        self.inText.grid(row=1, column=0, padx=5, pady=5)
        self.btnSend.grid(row=1, column=1, padx=5, pady=5)
    
        self.Chat.config(state='disable')
        
        self.inText.bind("<Return>", self.Mensaje_sending)
        
        # --------------------------- StatusBar -----------------------
        self.statusBar = tk.Label(self.master,textvariable=self.status, bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.statusBar.pack(side=tk.BOTTOM, fill=tk.X)
        
    
    def connect(self):
        if self.connected == False:
            if self.IP.get() and self.puerto_cliente.get() and self.name_cliente.get():
                try:
                    self.client = Client(self.IP.get(), self.puerto_cliente.get(), self.name_cliente.get())
                    self.inServer_ip.config(state='disable')
                    self.inPuerto_server.config(state='disable')
                    self.EntryUser.config(state='disable')
                    self.btnConnect.config(text='Desconectar')
                    self.Chat.config(state='normal')
                    self.status.set("Conexión establecida")
                    self.Chat.insert(END, "---- Mensaje del sistema: Conectado al Servidor ----\n", "aa")
                    self.Chat.tag_config("aa", foreground='blue')
                    self.Chat.see(END)
                    self.Chat.config(state='disable')
                    self.inText.config(state="normal")
                    self.btnSend.config(state="normal")
                    self.connected = True
                    
                    th = threading.Thread(target=self.Recibir_msje, daemon=True)
                    th.start()
                    
                except:
                    showerror("Error de conexion", "El servicio de Chat no esta disponible")
            else:
                showerror("Error de parametros", "Debe completar los parametros de Server IP, puerto_cliente y name_cliente")
        
        else:
            
            
            self.client.sock.close()
            self.inServer_ip.config(state='active')
            self.inPuerto_server.config(state='active')
            self.EntryUser.config(state='active')
            self.btnConnect.config(text='Conectar')
            self.Chat.config(state='normal')
            
            self.Chat.insert(END, "---- Mensaje del sistema: Desconectado al Servidor ----\n", "sys_msg")
            self.Chat.see(END)
            self.Chat.tag_config("sys_msg", foreground='red')
            self.Chat.config(state='disable')
            self.inText.config(state='disabled')
            self.btnSend.config(state='disabled')
            self.status.set("Se cerró la conexión")
            self.connected = False
    

    def Recibir_msje(self):
        while self.connected:
            try:
                message_in = self.client.cliente_recibir_mensaje()
                if message_in == False:
                    self.client.sock.close()
                    self.inServer_ip.config(state='active')
                    self.inPuerto_server.config(state='active')
                    self.EntryUser.config(state='active')
                    self.btnConnect.config(text='Conectar')
                    self.Chat.config(state='normal')
                    self.Chat.insert(END, "---- Mensaje del sistema: Desconectado al Servidor ----\n", "sys_msg")
                    self.Chat.see(END)
                    self.Chat.tag_config("sys_msg", foreground='red')
#                    self.Chat.config(state='readonly')
                    self.connected = False
                else:
                    self.Chat.config(state='normal')
                    self.Chat.insert(END, message_in + "\n")
                    self.Chat.see(END)
                    self.Chat.config(state='disable')
            except:
                break
    
    
    def Mensaje_sending(self, handle):
        if self.connected and self.msj.get():
            self.client.cliente_enviar_mensaje(self.msj.get())
            self.msj.set("")
            self.Chat.see(END)
            
    def close_app(self):
            try: self.client.sock.close()
            except:pass
            self.master.destroy()   


    
root = Tk()
app = Chat_servidor_cliente(root)
root.mainloop()
        
        
        
    