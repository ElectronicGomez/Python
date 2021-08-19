#%%
from tkinter import Tk,StringVar,Entry,Button,Label,Frame
from tkinter.ttk import Labelframe
import pandas as pd

class App:
    def __init__(self,master):
        self.master = master
        self.master.title('TKINTER')
        self.master.resizable(0,0)
        

        self.lista = []
        self.edad = StringVar()
        self.sexo = StringVar()
        self.cp0 = StringVar()
        self.cp1 = StringVar()
        self.cp2 = StringVar()
        self.cp3 = StringVar()
        self.trestbps = StringVar()
        self.chol = StringVar()
        self.fbs = StringVar()
        self.restecg = StringVar()
        self.thalach = StringVar()
        self.exang = StringVar()
        self.oldpeak = StringVar()
        self.slope0 = StringVar()
        self.slope1 = StringVar()
        self.slope2 = StringVar()
        self.ca = StringVar()
        self.thal0 = StringVar()
        self.thal1 = StringVar()
        self.thal2 = StringVar()
        self.target = StringVar()
        self.cp = StringVar()
        
        frm = Frame(master = self.master)
        frm.pack()
        
        self.lblFrame = Labelframe(frm,text='Datos a ingresar')
        self.lblFrame.pack(side='top')
        self.lblFrame2 = Labelframe(frm,text = 'Asignamos datos')
        self.lblFrame2.pack(side='top')
        
        self.lbledad = Label(self.lblFrame,text = 'Edad',width=20)
        self.lblsexo = Label(self.lblFrame,text='Sexo',width=20)
        self.lblcp0 = Label(self.lblFrame,text = 'Cp0',width=20)
        self.lblcp1 = Label(self.lblFrame,text = 'Cp1',width=20)
        self.lblcp2 = Label(self.lblFrame,text = 'Cp2',width=20)
        self.lblcp3 = Label(self.lblFrame,text = 'Cp3',width=20)
        self.lbltrestbps = Label(self.lblFrame,text = 'Trestbps',width=20)
        self.lblchol = Label(self.lblFrame,text = 'Chol',width=20)
        self.lblfbs = Label(self.lblFrame,text = 'Fbs',width=20)
        self.lblrestecg = Label(self.lblFrame,text = 'Restecg',width=20)
        self.lblthalach = Label(self.lblFrame,text = 'Thalach',width=20)
        self.lblexang = Label(self.lblFrame,text = 'Exang',width=20)
        self.lbloldpeak = Label(self.lblFrame,text = 'Oldpeak',width=20)
        self.lblslope0 = Label(self.lblFrame,text = 'Slope0',width=20)
        self.lblslope1 = Label(self.lblFrame,text = 'Slope1',width=20)
        self.lblslope2 =Label(self.lblFrame,text = 'Slope2',width=20)
        self.lblca = Label(self.lblFrame,text = 'Ca',width=20)
        self.lblthal0 = Label(self.lblFrame,text = 'Thal0',width=20)
        self.lblthal1 = Label(self.lblFrame,text = 'Thal1',width=20)
        self.lblthal2 = Label(self.lblFrame,text = 'Thal2',width=20)
        self.lbltarget = Label(self.lblFrame,text = 'Target',width=20)
        self.lblcp = Label(self.lblFrame,text = 'cp',width=20)
        
        self.Entryedad = Entry(self.lblFrame,width=20,textvariable = self.edad)
        self.Entrysexo = Entry(self.lblFrame,width=20,textvariable = self.sexo)
        self.Entrycp0 = Entry(self.lblFrame,width=20,textvariable = self.cp0)
        self.Entrycp1 = Entry(self.lblFrame,width=20,textvariable = self.cp1)
        self.Entrycp2 = Entry(self.lblFrame,width=20,textvariable = self.cp2)
        self.Entrycp3 = Entry(self.lblFrame,width=20,textvariable = self.cp3)
        self.Entrytrestbps = Entry(self.lblFrame,width=20,textvariable = self.trestbps)
        self.Entrychol = Entry(self.lblFrame,width=20,textvariable = self.chol)
        self.Entryfbs = Entry(self.lblFrame,width=20,textvariable = self.fbs)
        self.Entryrestecg = Entry(self.lblFrame,width=20,textvariable = self.restecg)
        self.Entrythalach = Entry(self.lblFrame,width=20,textvariable = self.thalach)
        self.Entryexang = Entry(self.lblFrame,width=20,textvariable = self.exang)
        self.Entryoldpeak = Entry(self.lblFrame,width=20,textvariable = self.oldpeak)
        self.Entryslope0 = Entry(self.lblFrame,width=20,textvariable = self.slope0)
        self.Entryslope1 = Entry(self.lblFrame,width=20,textvariable = self.slope1)
        self.Entryslope2 =Entry(self.lblFrame,width=20,textvariable = self.slope2)
        self.Entryca = Entry(self.lblFrame,width=20,textvariable = self.ca)
        self.Entrythal0 = Entry(self.lblFrame,width=20,textvariable = self.thal0)
        self.Entrythal1 = Entry(self.lblFrame,width=20,textvariable = self.thal1)
        self.Entrythal2 = Entry(self.lblFrame,width=20,textvariable = self.thal2)
        self.Entrytarget = Entry(self.lblFrame,width=20,textvariable = self.target)
        self.Entrycp = Entry(self.lblFrame,width=20,textvariable = self.cp)
        
        self.ButtonAsig = Button(self.lblFrame2,text = 'Asignamos Valores',command = self.Asignamos)
        self.ButtonAsig.grid()
        
        self.lbledad.grid(row=0,column = 0)
        self.lblsexo.grid(row=1,column = 0)
        self.lblcp0.grid(row=2,column = 0)
        self.lblcp1.grid(row=3,column = 0)
        self.lblcp2.grid(row=4,column = 0)
        self.lblcp3.grid(row=5,column = 0)
        self.lbltrestbps.grid(row=6,column = 0)
        self.lblchol.grid(row=7,column = 0)
        self.lblfbs.grid(row=8,column = 0)
        self.lblrestecg.grid(row=9,column = 0)
        self.lblthalach.grid(row=10,column = 0)
        self.lblexang.grid(row=11,column = 0)
        self.lbloldpeak.grid(row=12,column = 0)
        self.lblslope0.grid(row=13,column = 0)
        self.lblslope1.grid(row=14,column = 0)
        self.lblslope2.grid(row=15,column = 0)
        self.lblca.grid(row=16,column = 0)
        self.lblthal0.grid(row=17,column = 0)
        self.lblthal1.grid(row=18,column = 0)
        self.lblthal2.grid(row=19,column = 0)
        self.lbltarget.grid(row=20,column = 0)
        self.lblcp.grid(row=21,column = 0)
        
        self.Entryedad.grid(row=0,column = 1,padx=10)
        self.Entrysexo.grid(row=1,column = 1)
        self.Entrycp0.grid(row=2,column = 1)
        self.Entrycp1.grid(row=3,column = 1)
        self.Entrycp2.grid(row=4,column = 1)
        self.Entrycp3.grid(row=5,column = 1)
        self.Entrytrestbps.grid(row=6,column = 1)
        self.Entrychol.grid(row=7,column = 1)
        self.Entryfbs.grid(row=8,column = 1)
        self.Entryrestecg.grid(row=9,column = 1)
        self.Entrythalach.grid(row=10,column = 1)
        self.Entryexang.grid(row=11,column = 1)
        self.Entryoldpeak.grid(row=12,column = 1)
        self.Entryslope0.grid(row=13,column = 1)
        self.Entryslope1.grid(row=14,column = 1)
        self.Entryslope2.grid(row=15,column = 1)
        self.Entryca.grid(row=16,column = 1)
        self.Entrythal0.grid(row=17,column = 1)
        self.Entrythal1.grid(row=18,column = 1)
        self.Entrythal2.grid(row=19,column = 1)
        self.Entrytarget.grid(row=20,column = 1)
        self.Entrycp.grid(row=21,column = 1)
        
        
    def Asignamos(self):
        """
        self.lista.append(self.edad.get())
        self.lista.append(self.sexo.get())
        self.lista.append(self.cp0.get())
        self.lista.append(self.cp1.get())
        self.lista.append(self.cp2.get())
        self.lista.append(self.cp3.get())
        self.lista.append(self.trestbps.get())
        self.lista.append(self.chol.get())
        self.lista.append(self.fbs.get())
        self.lista.append(self.restecg.get())
        self.lista.append(self.thalach.get())
        self.lista.append(self.exang.get())
        self.lista.append(self.oldpeak.get())
        self.lista.append(self.slope0.get())
        self.lista.append(self.slope1.get())
        self.lista.append(self.slope2.get())
        self.lista.append(self.ca.get())
        self.lista.append(self.thal0.get())
        self.lista.append(self.thal1.get())
        self.lista.append(self.thal2.get())
        self.lista.append(self.target.get())
        """
        if (self.sexo.get() == "Masculino"): genero = 1
        else: genero = 0

        if (self.cp.get() == "Anginal"):
            c0 = 1; c1 = 0; c2 = 0; c3 = 0
        elif (self.cp.get() == "Anginal Atipico"):
            c0 = 0; c1 = 1; c2 = 0; c3 = 0
        elif (self.cp.get() == ""):
            c0 = 0; 

        dft = pd.DataFrame({"age":[(self.edad.get() - 25)/(80-25))],     
                                   
                                   
                                   
                   "sex":[genero],
                   "cp0":[c0],
                   "cp1":[c1],
                   "cp2":[c2],
                   "cp3":[c3],
                   "trestbps":[0],
                   "chol":[0],
                   "fbs":[0],
                   "restecg":[0],
                   "thalach":[0],
                   "exang":[0],
                   "oldpeak":[0],
                   "slope0":[0],
                   "slope1":[0],
                   "slope2":[0],
                   "ca":[0],
                   "thal1":[0],
                   "thal2":[0],
                   "thal3":[0]})
        
        print(self.edad.get())
    

    
    
    
    
    
root = Tk()
app = App(root)
root.mainloop()
    

