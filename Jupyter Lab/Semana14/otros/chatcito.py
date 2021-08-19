#%%
#Chat serial personal

from tkinter import Tk, Label, Entry, Button
from tkinter.ttk import Combobox, Labelframe
from tkinter.scrolledtext import ScrolledText
import serial.tools.list_ports
import serial
import threading
from tkinter import *
import time
import textwrap
import tkinter as tk

class Chat_personal:
    def __init__(self,master):
        
        
        self.master = master
        self.master.title("Serial chat")
        self.master.geometry("850x520+100+100")
        self.master.resizable(0, 0)
        self.cont = 0
        self.cont2 = 0        
        
        
        #objetos
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
        
        self.namemodificado.set("Nickname")
        self.nickname.set("Nickname")
        self.puertoconectado.set("Ninguno")
        self.status.set("Sin conexión")
        self.labelestado.set("Desconectado")
        
        
        ports = serial.tools.list_ports.comports()
        self.port_list = []
        for port in ports:
            self.port_list.append(port.device)
        
        
        
        
        self.frmperfil = Frame(self.master, bg = "#212D43",height=50,width=600)
        self.frmperfil.place(height=500, width=250, x=0, y=0)
        
        
        
        
        self.lblname = Label(self.frmperfil, textvariable = self.namemodificado, bg = "#212D43", fg = "white", font='Verdana 14', anchor=W)
        self.lblname.place(height=30, width=100, x=20, y=50)
        
        
        
        
        
        self.btntitulo = Button(self.frmperfil, text = "Cambiar", bg = "#212D43", fg = "white", font='Verdana 9', command=self.cambiarnickname)
        self.btntitulo.place(height=23, width=76, x=172, y=53)        
        
        
        
        
        self.lblmore = Label(self.frmperfil, text="Puerto conectado: ", bg = "#212D43", fg = "white", font='Verdana 8',height=1,width=5, anchor=W)
        self.lblmore.place(height=30, width=108, x=20, y=75)
        
        self.lblcom = Label(self.frmperfil, textvariable=self.puertoconectado, bg = "#212D43", fg = "white", font='Verdana 8',height=1,width=5)
        self.lblcom.place(height=30, width=50, x=120, y=75)        



        self.lbltitulo = Label(self.frmperfil, text = "Estado", bg = "#212D43", fg = "white", font='Verdana 14', anchor=W)
        self.lbltitulo.place(height=30, width=100, x=20, y=120)


        self.lblestado = Label(self.frmperfil, textvariable=self.labelestado, bg = "#212D43", fg = "white", font='Verdana 8',height=1,width=5, anchor=W)
        self.lblestado.place(height=30, width=200, x=21, y=150)           
        
        
        
        self.lblPort1 = Label(self.frmperfil, text="Puerto:", bg = "#212D43", fg = "white", font='Verdana 10')
        self.lblPort1.place(height=23, width=55, x=0, y=5)
        
        
        
        self.cboCOM1 = Combobox(self.frmperfil, values=self.port_list, textvariable=self.port_select1)
        self.cboCOM1.place(height=23, width=115, x=55, y=5)        
        self.cboCOM1.set("Ninguno")


        self.btnConn1 = Button(self.frmperfil, text="Conectado", width=12, command=self.conectar, bg = "#212D43", fg = "white", font='Verdana 10')
        self.btnConn1.place(height=23, width=76, x=172, y=5)


        self.frmchat = Frame(self.master, bg = "#F0F0EF")
        self.frmchat.place(height=450, width=600, x=250, y=0)
        
        
        self.text1 = ScrolledText(self.frmchat, width=70, height=20, state='disabled')
        self.text1.place(height=450, width=600, x=0, y=0)        


        
        
        self.frmescribe = Frame(self.master,  bg = "#C3CCD2")
        self.frmescribe.place(height=50, width=600, x=250, y=450)
        
        
        self.inText1 = Entry(self.frmescribe, width=40, textvariable=self.envia1)
        self.inText1.place(height=28, width=480, x=28, y=11)

        
        self.btnEnviar1 = Button(self.frmescribe, text="Send", width=12, command=self.envia_mensaje1, font='Verdana 8',  bg = "#4C7FBD",  fg = "white")
        self.btnEnviar1.place(height=28, width=70, x=508, y=11)
        

        
        self.text1.insert(tk.END, self.chat1)
        
        
        # Manejo del boton "X" de la ventana en Windows
        self.master.protocol("WM_DELETE_WINDOW", self.closing)
        
        
        
        
        
        self.status_bar = Label(self.master, textvariable=self.status,anchor=W, font='Verdana 8',  bg = "#172154",  fg = "white")
        self.status_bar.place(height=20, width=850, x=0, y=500)
        

#        self.inText1.bind("<Return>", self.envia_mensaje1)
        
        
    def cambiarnickname(self):
        
        
        if (self.cont2==0):
            self.cont2 = 1
            self.btntitulo.config(text="Aceptar")
            
            self.lblname.destroy()
            
            
            self.entname = Entry(self.frmperfil)
            self.entname.place(height=25, width=130, x=23, y=50)            
            
            
            
        elif (self.cont2==1):
            self.cont2 = 0
            self.btntitulo.config(text="Cambiar")
            
            
            self.namemodificado.set(self.entname.get())
            self.entname.destroy()
            
            
            self.lblname = Label(self.frmperfil, textvariable = self.namemodificado, bg = "#212D43", fg = "white", font='Verdana 14', anchor=W)
            self.lblname.place(height=30, width=100, x=20, y=50)
            
        
        
    def conectar(self):
        
        self.puertoconectado.set(self.cboCOM1.get())
        self.namemodificado.set("Nickname")  
        
        
        if self.cont==0:
            self.cont=1
            self.btnConn1.config(text="Disconnect", width=12, bg = "#CF0303", fg = "white", font='Verdana 9')
            self.namemodificado.set(self.cboCOM1.get())  
            try:
                self.ser1 = serial.Serial(port=self.port_select1.get(), timeout=2)
#                self.text1.insert(END, "Conexion establecida"+ '\n')
                
                self.labelestado.set("Conexion establecida")
                
                self.status.set("Conectado")
                self.text1.config(state='normal')  
            except:
                self.labelestado.set("No se pudo realizar la conexion")
                self.text1.config(state='disabled')                
#                self.text1.insert(END, "No se pudo realizar la conexion"+ '\n')


                
                self.namemodificado.set("Nickname")
                self.status.set("Desconectado")
                
            th = threading.Thread(target=self.Response_loop, daemon=True)
            th.start()
            
            
            
        elif self.cont==1:
            self.btnConn1.config(text="Connect", width=12, bg = "#212D43", fg = "white", font='Verdana 10')
            self.cont=0
            self.ser1.close()
#            self.text1.insert(END, "Conexion cerrada"+ '\n')
            self.labelestado.set("Conexion cerrada")
            
            
            self.puertoconectado.set("Ninguno")
            self.namemodificado.set("Nickname") 
            self.status.set("Desconectado")
            self.text1.config(state='disabled')
            
            
                
    def envia_mensaje1(self):
        
        try:

            #Port 1 envia y port2 recibe
            data = ("  "+ self.namemodificado.get() +": "+self.envia1.get()).encode('utf-8')
            
            #se envia la data por el puerto
            
            self.ser1.write(data)
            
            
            
            
            self.status.set("Enviado")
            
            
            
            

#            self.status.set("Connected")
            
            
            
            self.text1.insert(tk.END, str(self.fecha.get())+" - "+str(self.hora.get())+ "\n"+ "  "+ self.namemodificado.get() +": "+self.chat1 + self.envia1.get() + '\n'+ '\n')
            
            
            
            
            #   Recibir
           
            self.envia1.set('')
        except:
            #self.text1.insert(END, "No hay conexion a puertos"+ '\n')
            self.labelestado.set("No hay conexion a puertos")
            

    
    def Response_loop(self):
        self.Recibe_dato()
    
    
    def Recibe_dato(self):
        
        
        self.hora.set(time.strftime("%H:%M:%S") )
        self.fecha.set(time.strftime("%d/%m/%y"))

        
        
        
        if self.ser1.in_waiting > 0:
            self.status.set("Recibido")
            data2 = self.ser1.readline()
            
            strSerial = data2.decode('utf-8')
            
            
            self.text1.insert(str(self.fecha.get())+" - "+str(self.hora.get()) + "\n"+ self.chat1 + strSerial + '\n'+ '\n')
            
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



