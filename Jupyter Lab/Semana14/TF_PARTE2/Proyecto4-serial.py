# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 23:29:53 2020

"""


#%%
from tkinter import *
from tkinter import ttk
import serial
import serial.tools.list_ports
import threading
import datetime
from tkinter.messagebox import askyesno

class Chat:
    def __init__(self,master):
        #------------MASTER AND THE BOYS
        self.master=master
        self.master.title("Serial Chat")
        self.master.resizable(0,0)
        self.master.protocol("WM_DELETE_WINDOW", self.closing)
        
        #------------VARIABLES
        self.lista_COMS=self.COMS_search()
        self.togle_con=False
        self.togle_enviar=False
        self.ton=False
        
        self.puerto=""
        
        #------------OBJTOVARIABLE
        self.mensaje=StringVar(value="")
        
        #------------frames
        self.frm1=LabelFrame(self.master,text="Conexion")
        self.frm2=Frame(self.master)
        self.frm3=LabelFrame(self.master,text="Enviar mensaje")
        
        self.frm1.pack(fill=X,padx=5)
        self.frm2.pack(fill=X,padx=5)
        self.frm3.pack(fill=X,padx=5)
        
        #------------Statusbar
        self.status_bar = Label(self.master,text="Elija un puerto Serial",relief=SUNKEN, anchor=W)
        self.status_bar.pack(side=BOTTOM, expand=True, fill=X,pady=5)
        
        
        #------------widgets
        #------------frm1
        self.btnConectar=Button(self.frm1,text="Conectar",width=10,command=self.cuandoconecto,state=DISABLED)
        self.cmbCOMS=ttk.Combobox(self.frm1,values=self.lista_COMS)
        self.lbl=Label(self.frm1,text="Puerto COM:")
        
        self.btnConectar.grid(row=0,column=2,padx=5, pady=5)
        self.cmbCOMS.grid(row=0,column=1,padx=5, pady=5)
        self.lbl.grid(row=0,column=0,padx=5, pady=5)
        #------------frm2
        self.scroll_Y = ttk.Scrollbar(self.frm2, orient='vertical')
        self.txtChat = Text(self.frm2,width=50, height=25, font="Times 10",state=DISABLED, yscrollcommand=self.scroll_Y.set)
        self.scroll_Y.config(command=self.txtChat.yview)
        
        self.txtChat.grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.scroll_Y.grid(row=0, column=1, sticky='ns')
        
        #------------frm3
        self.entmensaje=Entry(self.frm3,width=40,textvariable=self.mensaje,state=DISABLED)
        self.btnEnviar=Button(self.frm3,text="Enviar",width=10,state=DISABLED,command=self.enviador)
        
        self.entmensaje.grid(row=0,column=0,padx=5, pady=5)
        self.btnEnviar.grid(row=0,column=1,padx=5, pady=5)
        
        #------------Hilos y bucles
        th=threading.Thread(target=self.conectador1,daemon=True)
        th.start()
        
        #------------BINDS
        self.cmbCOMS.bind("<<ComboboxSelected>>",self.activabtncon)
        self.entmensaje.bind("<Return>", lambda event: self.enviador())
        
        #------------Activo el Boton Conectar 
    def activabtncon(self,algo):
        self.btnConectar.config(state=NORMAL)
        
        
        #------------habilito la secuencia de enviar
    def enviador(self):
        self.togle_enviar=True    
        
        #------------conectar el puerto elegido
    def cuandoconecto(self):
        self.puerto=str(self.cmbCOMS.get())
        if self.ton==False:
            try:
                #------------establezco la connecion
                self.ser = serial.Serial(port=self.puerto, timeout=0, baudrate=9600,
                                bytesize=8, stopbits=serial.STOPBITS_ONE)
                
                self.status_bar.config(text="Conexion establecida")
                self.togle_con=True
                self.btnConectar.config(text="Desconectar")
                self.btnEnviar.config(state=NORMAL)
                self.entmensaje.config(state=NORMAL)
                self.ton=True
            except:
                #------------secuencia por si sale mal
                try:
                    if self.ser.is_open:
                        self.ser.close()
                except:pass
                self.btnConectar.config(state=NORMAL)
                self.btnEnviar.config(state=DISABLED)
                self.entmensaje.config(state=DISABLED)
                self.status_bar.config(text="Hubo un error")
        else:
            try:
                if self.ser.is_open:
                    self.ser.close()
                    self.cmbCOMS.set("")
                    self.btnConectar.config(state=DISABLED,text="Conectar")
                    self.txtChat.delete('1.0', END)
                    self.btnEnviar.config(state=DISABLED)
                    self.entmensaje.config(state=DISABLED)
                    self.mensaje.set("")
                    self.ton=False
            except:pass
            
    #------------BUCLE
    def conectador1(self):
        self.lbl.after(10,self.conectador2)
        
    def conectador2(self):
        try:
            #------------verifico si puedo conectarme
            if self.togle_con:
                #------------prioridad a la recepcion de mensajes
                if self.ser.in_waiting > 0:         
                    self.status_bar.config(text="Mensaje recibido")
                    
                    
                    general=""
                    while True:
                        data = self.ser.readline()    
                        string = data.decode('utf-8')
                        general=general+string
                        
                        if general[-1] == "|":   
                            break
                        
                    com,mensa=general.split(sep=": ")
                    if mensa[:-1]!="":
                        self.txtChat.config(state=NORMAL)
                        self.txtChat.insert(END,general[:-1]+"\n","azul")
                        self.txtChat.see(END)
                        self.txtChat.config(state=DISABLED)
                        

                #------------luego veo si puedo enviar mensajes
                elif self.togle_enviar:
                    self.togle_enviar=False
                    string = self.mensaje.get() 
                    #------------solo envio un mensaje si no esta vacio
                    if string.strip() != "" :
                        string = str(self.puerto)+": "+string +"|"
                        self.status_bar.config(text="Mensaje enviado")
                        
                        data = string.encode('utf-8')
                        self.ser.write(data)
                        self.txtChat.config(state=NORMAL)
                        self.txtChat.insert(END,string[:-1]+"\n","verde")
                        self.txtChat.see(END)
                        self.txtChat.config(state=DISABLED)
                        self.mensaje.set("")
                              
        except:
            #------------por si sale mal
            try:
                if self.ser.is_open:
                    self.ser.close()
            except:pass
        self.txtChat.tag_config('verde', foreground='green')
        self.txtChat.tag_config('azul', foreground='blue') 
        self.conectador1()
        
    def closing(self):  
        #------------secuencia de cerrado del serial
        try:
            if self.ser.is_open:
                self.ser.close()
        except: pass
        #------------solo guardo si el texto no esta vacio
        if self.txtChat.get(1.0, END).strip() != "":
            preguntar=askyesno("Guardado","¿Desea guardar su conversación?")
            #------------pregunto si quieren guardar su conversacion
            if preguntar:
                fecha = datetime.datetime.now()
                #------------lo guardo con su fecha y con el nombre de Chat
                fecha="Chat_"+fecha.strftime("%H%m%S%d%m%Y")+".txt"
                with open(fecha, mode='w') as f: 
                    f.write(self.txtChat.get(1.0, END))
        #------------cierro la ventana
        self.master.destroy()
        
    #------------funcion para tener los COMS
    def COMS_search(self):
        arrojador=[]
        ports = serial.tools.list_ports.comports()

        for port in ports:
            a=str(port).split(" ")
            arrojador.append(a[0])
        return arrojador
        
    
        
        
root=Tk()
app=Chat(root)
root.mainloop()

