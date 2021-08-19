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
    def __init__(self, ip_address, tcp_port, username):
        self.ip_address = ip_address
        self.tcp_port = tcp_port
        self.username = username
        
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.ip_address, self.tcp_port))
    
    
    def recvMsg(self):
        data_header = self.sock.recv(HEADER_SIZE)
        
        if not data_header:
            return False
        
        data = self.sock.recv(int(data_header))
        return data.decode('utf-8')
    
    
    def sendMsg(self, strData):
        data_len = len(strData + self.username + "> ")
        self.sock.send(f"{data_len:<{HEADER_SIZE}}{self.username}> {strData}".encode('utf-8'))
        return None
    
    
class ChatClientApp:
    def __init__(self, master):
        self.master = master
        self.master.title("FACEBOOK")
        self.master.resizable(0, 0)
        self.master.protocol("WM_DELETE_WINDOW", self.close_app)
        
        self.client = None
        self.connected = False
        
        self.IP = StringVar(value=socket.gethostbyname(socket.gethostname()))
        self.Port = IntVar(value=5000)
        self.Username = StringVar()
        self.Message = StringVar()
        self.status = StringVar()
        self.status.set("Sin conexión")
        
        frm1 = LabelFrame(self.master, text="LOGIN")
        frm2 = Frame(self.master)
        frm1.pack(padx=10, pady=10)
        frm2.pack(padx=10, pady=10)
        
        # -------------------------- frm1 -------------------------
        self.lblServerIP = Label(frm1, text="Server IP")
        self.inServerIP = Entry(frm1, textvariable=self.IP, width=16)
        self.lblServerPort = Label(frm1, text="Port")
        self.inServerPort = Entry(frm1, textvariable=self.Port, width=12)
        self.lblUsername = Label(frm1, text="Username")
        self.inUsername = Entry(frm1, textvariable=self.Username, width=16)
        self.btnConnect = Button(frm1, text="Conectar",command=self.connect)
        
        self.lblServerIP.grid(row=0, column=0, padx=5, pady=5)
        self.inServerIP.grid(row=0, column=1, padx=5, pady=5)
        self.lblServerPort.grid(row=0, column=2, padx=5, pady=5)
        self.inServerPort.grid(row=0, column=3, padx=5, pady=5)
        self.lblUsername.grid(row=0, column=4, padx=5, pady=5)
        self.inUsername.grid(row=0, column=5, padx=5, pady=5)
        self.btnConnect.grid(row=0, column=6, padx=5, pady=5)
                
        # -------------------------- frm2 -------------------------
        self.Chat = ScrolledText(frm2, width=70)
        self.inText = Entry(frm2, textvariable=self.Message, width=70)
        self.btnSend = Button(frm2, text="Enviar", command=lambda: self.send_message(None))
        
        self.Chat.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
        self.inText.grid(row=1, column=0, padx=5, pady=5)
        self.btnSend.grid(row=1, column=1, padx=5, pady=5)
    
        self.Chat.config(state='disable')
        
        self.inText.bind("<Return>", self.send_message)
        
        # --------------------------- StatusBar -----------------------
        self.statusBar = tk.Label(self.master,textvariable=self.status, bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.statusBar.pack(side=tk.BOTTOM, fill=tk.X)
        
    
    def connect(self):
        if self.connected == False:
            if self.IP.get() and self.Port.get() and self.Username.get():
                try:
                    self.client = Client(self.IP.get(), self.Port.get(), self.Username.get())
                    self.inServerIP.config(state='disable')
                    self.inServerPort.config(state='disable')
                    self.inUsername.config(state='disable')
                    self.btnConnect.config(text='Desconectar')
                    self.Chat.config(state='normal')
                    self.status.set("Conexión establecida")
                    self.Chat.insert(END, "---- Mensaje del sistema: Conectado al Servidor ----\n", "aa")
                    
                    self.Chat.tag_config("aa", foreground='blue')
                    self.Chat.see(END)
                    self.Chat.config(state='disable')
                    self.connected = True
                    
                    th = threading.Thread(target=self.recv_message, daemon=True)
                    th.start()
                    
                except:
                    showerror("Error de conexion", "El servicio de Chat no esta disponible")
            else:
                showerror("Error de parametros", "Debe completar los parametros de Server IP, Port y Username")
        
        else:
            self.client.sock.close()
            self.inServerIP.config(state='active')
            self.inServerPort.config(state='active')
            self.inUsername.config(state='active')
            self.btnConnect.config(text='Conectar')
            self.Chat.config(state='normal')
            
            self.Chat.insert(END, "---- Mensaje del sistema: Desconectado al Servidor ----\n", "sys_msg")
            self.Chat.see(END)
            self.Chat.tag_config("sys_msg", foreground='red')
            self.Chat.config(state='disable')
            self.connected = False
    

    def recv_message(self):
        while self.connected:
            try:
                message_in = self.client.recvMsg()
                if message_in == False:
                    self.client.sock.close()
                    self.inServerIP.config(state='active')
                    self.inServerPort.config(state='active')
                    self.inUsername.config(state='active')
                    self.btnConnect.config(text='Conectar')
                    self.Chat.config(state='normal')
                    self.Chat.insert(END, "---- Mensaje del sistema: Desconectado al Servidor ----\n", "sys_msg")
                    self.Chat.see(END)
                    self.Chat.tag_config("sys_msg", foreground='red')
                    self.Chat.config(state='disable')
                    self.connected = False
                else:
                    self.Chat.config(state='normal')
                    self.Chat.insert(END, message_in + "\n")
                    self.Chat.see(END)
                    self.Chat.config(state='disable')
            except:
                break
    
    
    def send_message(self, handle):
        if self.connected and self.Message.get():
            self.client.sendMsg(self.Message.get())
            self.Message.set("")
            self.Chat.see(END)
            
    def close_app(self):
            try: self.client.sock.close()
            except:pass
            self.master.destroy()   


    
root = Tk()
app = ChatClientApp(root)
root.mainloop()
        
        
        
    