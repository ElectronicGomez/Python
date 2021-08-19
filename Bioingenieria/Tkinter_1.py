#%%
from tkinter import Tk,StringVar,Entry,Button,Label,Frame
from tkinter.ttk import Labelframe
import pandas as pd

class App:
    def __init__(self,master):
        self.master = master
        self.master.title('TKINTER')
        #self.master.resizable(0,0)
        
        
        
        
        
        
        self.edad = StringVar()
        self.sexo = StringVar()
        self.cp = StringVar()
#        self.cp0 = StringVar()
#        self.cp1 = StringVar()
#        self.cp2 = StringVar()
#        self.cp3 = StringVar()
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
        self.var=StringVar()
        
        self.var.set('cp')
        
        
        frm = Frame(master = self.master)
        frm.pack()
        
        self.lblFrame = Labelframe(frm,text='Datos a ingresar')
        self.lblFrame.pack(side='top')
        self.lblFrame2 = Labelframe(frm,text = 'Asignamos datos')
        self.lblFrame2.pack(side='top')
        
        self.combo = ttk.Combobox(self.lblFrame, values=['Angina','Angina Atípica','Asintomático'],textvariable=self.var)
        
        
        
        self.lbledad = Label(self.lblFrame,text = 'Edad',width=20)
        self.lblsexo = Label(self.lblFrame,text='Sexo',width=20)
        self.lblcpselec = Label(self.lblFrame,text = 'Seleccionar cp',width=20)
#        self.lblcp0 = Label(self.lblFrame,text = 'Cp0',width=20)
#        self.lblcp1 = Label(self.lblFrame,text = 'Cp1',width=20)
#        self.lblcp2 = Label(self.lblFrame,text = 'Cp2',width=20)
#        self.lblcp3 = Label(self.lblFrame,text = 'Cp3',width=20)
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
        
        self.lblcpselec = Label(self.lblFrame,text = 'Seleccionar cp',width=20)
        
        
        self.Entryedad = Entry(self.lblFrame,width=20,textvariable = self.edad)
        self.Entrysexo = Entry(self.lblFrame,width=20,textvariable = self.sexo)
        self.Entrycp = Entry(self.lblFrame,width=20,textvariable = self.cp)
#        self.Entrycp0 = Entry(self.lblFrame,width=20,textvariable = self.cp0)
#        self.Entrycp1 = Entry(self.lblFrame,width=20,textvariable = self.cp1)
#        self.Entrycp2 = Entry(self.lblFrame,width=20,textvariable = self.cp2)
#        self.Entrycp3 = Entry(self.lblFrame,width=20,textvariable = self.cp3)
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
        #self.target.get()
        
        #self.target.set(9)
        
        self.ButtonAsig = Button(self.lblFrame2,text = 'Asignamos Valores',command = self.Asignamos)
        self.ButtonAsig.grid()
        
        self.lbledad.grid(row=0,column = 0)
        self.lblsexo.grid(row=1,column = 0)
        self.lblcpselec.grid(row=2,column = 0)
#        self.lblcp0.grid(row=2,column = 0)
#        self.lblcp1.grid(row=3,column = 0)
#        self.lblcp2.grid(row=4,column = 0)
#        self.lblcp3.grid(row=5,column = 0)
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
        
        
        self.combo.grid(row=1,column=3)
        
        self.Entryedad.grid(row=0,column = 1,padx=10)
        self.Entrysexo.grid(row=1,column = 1)
        self.Entrycp.grid(row=2,column = 1)        
#        self.Entrycp0.grid(row=2,column = 1)
#        self.Entrycp1.grid(row=3,column = 1)
#        self.Entrycp2.grid(row=4,column = 1)
#        self.Entrycp3.grid(row=5,column = 1)
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

      
    def Asignamos(self):
        l_edad=[]
        l_sexo=[]
        l_cp=[]
#        l_cp0=[]
#        l_cp1=[]
#        l_cp2=[]
#        l_cp3=[]
        l_trestbps=[]
        l_chol=[]
        l_fbs=[]
        l_restecg=[]
        l_thalach=[]
        l_exang=[]
        l_oldpeak=[]
        l_slope0=[]
        l_slope1=[]
        l_slope2=[]
        l_ca=[]
        l_thal0=[]
        l_thal1=[]
        l_thal2=[]
        l_target=[]
        
        l_edad.append(self.edad.get())
        l_sexo.append(self.sexo.get())
        l_cp.append(self.cp.get())
#        l_cp0.append(self.cp0.get())
#        l_cp1.append(self.cp1.get())
#        l_cp2.append(self.cp2.get())
#        l_cp3.append(self.cp3.get())
        l_trestbps.append(self.trestbps.get())
        l_chol.append(self.chol.get())
        l_fbs.append(self.fbs.get())
        l_restecg.append(self.restecg.get())
        l_thalach.append(self.thalach.get())
        l_exang.append(self.exang.get())
        l_oldpeak.append(self.oldpeak.get())
        l_slope0.append(self.slope0.get())
        l_slope1.append(self.slope1.get())
        l_slope2.append(self.slope2.get())
        l_ca.append(self.ca.get())
        l_thal0.append(self.thal0.get())
        l_thal1.append(self.thal1.get())
        l_thal2.append(self.thal2.get())
        l_target.append(self.target.get())
                              
           
        
        self.bio ={'edad':l_edad,'sexo':l_sexo,'cp':l_cp,                   
                   'trestbps':l_trestbps,'chol':l_chol,'fbs':l_fbs,
                   'restecg':l_restecg,'thalach':l_thalach,'exang':l_exang,
                   'oldpeak':l_oldpeak,'slope0':l_slope0,'slope1':l_slope1,
                   'slope2':l_slope2,'ca':l_ca,'thal0':l_thal1,
                   'thal2':l_thal2,'target':l_target                  
                   
                   }
        
        
        
                
        
        
        print(self.bio)
        #df_nuevo = pd.DataFrame(self.dic)

        #y_test_pred = model.predict(df_nuevo)
        #Se imprime los resultados de la predicción
        #print(y_test_pred)
        #salida="Beningo - Maligno\n"
        #for n in range(len(y_test_pred)):            
        #    salida=salida+"{:.2f} - {:.2f}".format(y_test_pred[n][0],y_test_pred[n][1])+'\n'
        #self.text1.insert(END,salida)
        
        
        
      
                         
                                 
                                 
    

    
    
    
    
    
root = Tk()
app = App(root)
root.mainloop()
    
#%%%%
from tkinter import Tk,StringVar,Entry,Button,Label,Frame
from tkinter.ttk import Labelframe
import pandas as pd

root = Tk()


def presion(event):
    #print("back")
    if(var.get()=="hola"):
        a=1
    else:
        a=0
    print(a)
#    print(var.get())
    
    
frm=Frame(root)
frm.pack()
var = StringVar()

combo = ttk.Combobox(frm, values=['hola','chau'],textvariable=var)
combo.pack()

combo.bind("<<ComboboxSelected>>", presion)
root.mainloop()
