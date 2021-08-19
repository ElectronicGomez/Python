import pandas as pd
import numpy as np
import datetime
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import roc_curve
from keras.models import Sequential
from keras.layers import Dense
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn import preprocessing
from sklearn import metrics
from keras import optimizers
from tkinter import Tk,StringVar,Entry,Button,Label,Frame
from tkinter.ttk import Labelframe
from tkinter import Tk,StringVar,Entry,Button,Label,Frame,ttk
from tkinter import messagebox

np.random.seed(int(datetime.datetime.now().microsecond))

df = pd.read_csv("heartModified(thalDiv).csv")
dfgraf=pd.read_csv("heart.csv")
print(df.info())
print('')

print(df.describe())
print('')

print(df.head(10))
print('')

#Normalizando datos
X = df.loc[:,['age','sex','cp0','cp1','cp2','cp3','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope0','slope1','slope2','ca','thal1','thal2','thal3']]
X['age'] = (X['age'] - 25)/(80-25)
X['trestbps'] = (X['trestbps'] - 90)/(200-90)
X['chol'] = (X['chol'] - 125)/(570-125)
X['thalach'] = (X['thalach'] - 70)/(205-70)
X['oldpeak'] = (X['oldpeak'] - 0)/(6.2-0)
X['ca'] = (X['ca'] - 0)/(4-0)

#Vector de salida deseada
y = df.loc[:,'target']

# Se conforman los patrones de entrenamiento:
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

#Se crea el modelo
model = Sequential()
model.add(Dense(units=11, activation='sigmoid', input_dim=20))
model.add(Dense(units=11, activation='sigmoid'))
model.add(Dense(units=1, activation='sigmoid'))

#Se entrena el modelo
print("Training model...")
sgd = optimizers.SGD(lr=0.4)
model.compile(loss='mean_squared_error', optimizer=sgd)
model.fit(X, y, epochs=10000, verbose=False)

print("")
print("Training Done")

#Se preba el modelo con lo restante de la base de datos
y_pred = model.predict(X_test)
ac = metrics.accuracy_score(y_test, y_pred.round())
print("accuaracy:",ac)

class App:
    def __init__(self,master,model):
        self.model = model
        self.master = master
        self.master.title("RN para enf. cardiovasculares. Precision: "+str(round(ac,2)*100)+" %")
        #self.master.resizable(0,0)
        
        self.edad = StringVar()
        self.sexo = StringVar()
        self.cp = StringVar()
        self.trestbps = StringVar()
        self.chol = StringVar()
        self.fbs = StringVar()
        self.restecg = StringVar()
        self.thalach = StringVar()
        self.exang = StringVar()
        self.oldpeak = StringVar()
        self.slope = StringVar()
        self.ca = StringVar()
        self.thal = StringVar()

        frm = Frame(master = self.master)
        frm.pack()
        
        self.lblFrame = Labelframe(frm,text='Datos a ingresar')
        self.lblFrame.pack(side='top')
        self.lblFrame2 = Labelframe(frm,text = 'Asignamos datos')
        self.lblFrame2.pack(side='top')
        ##################### Histograma
        self.variable=StringVar()
        self.lblFrame3 = Labelframe(frm,text='Graficos')
        self.lblFrame3.pack(side='top')
        
        self.lblvariable = Label(self.lblFrame3,text = 'Variable: ',width=25)
        self.combovariable = ttk.Combobox(self.lblFrame3, values=['Edad','Sexo','Tipo de dolor de pecho','Presion sanguinea en reposo (mmHg)',
         'Colesterol (mg/dl)','Nivel de azucar en la sangre en ayuno',
         'Resultados electrocadriograficos', 'Frecuencia cardiaca maxima (bpm)', 
         'Angina inducido por ejericio','Depresion del segmento ST (mm)','Pendiente del segmento ST',
         'Numero de vasos principales coloreados por fluoroscopia','Talasemia','Enfermo del corazon'],textvariable=self.variable,width=17)
        
        self.ButtonHistograma = Button(self.lblFrame3,text = 'Histograma',command = self.Histograma)
       
        self.lblvariable.grid(row=0,column = 0)
        self.combovariable.grid(row=0,column=1)
        self.ButtonHistograma.grid(row=1,column=1)        
        
        #################### Relacion
        
        self.compo1=StringVar()
        self.compo2=StringVar()
        self.lblcompo1 = Label(self.lblFrame3,text = 'Componente 1: ',width=25)
        self.lblcompo2 = Label(self.lblFrame3,text = 'Componente 2: ',width=25)
        self.combocompo1 = ttk.Combobox(self.lblFrame3, values=['Edad','Sexo','Tipo de dolor de pecho','Presion sanguinea en reposo (mmHg)',
         'Colesterol (mg/dl)','Nivel de azucar en la sangre en ayuno',
         'Resultados electrocadriograficos', 'Frecuencia cardiaca maxima (bpm)', 
         'Angina inducido por ejericio','Depresion del segmento ST (mm)','Pendiente del segmento ST',
         'Numero de vasos principales coloreados por fluoroscopia','Talasemia'],textvariable=self.compo1,width=17)
        self.combocompo2 = ttk.Combobox(self.lblFrame3, values=['Edad','Sexo','Tipo de dolor de pecho','Presion sanguinea en reposo (mmHg)',
         'Colesterol (mg/dl)','Nivel de azucar en la sangre en ayuno',
         'Resultados electrocadriograficos', 'Frecuencia cardiaca maxima (bpm)', 
         'Angina inducido por ejericio','Depresion del segmento ST (mm)','Pendiente del segmento ST',
         'Numero de vasos principales coloreados por fluoroscopia','Talasemia'],textvariable=self.compo2,width=17)
        
        self.ButtonRelacion = Button(self.lblFrame3,text = 'Relacion',command = self.Relacion)
       
        self.lblcompo1.grid(row=3,column = 0)
        self.lblcompo2.grid(row=4,column = 0)
        self.combocompo1.grid(row=3,column=1)
        self.combocompo2.grid(row=4,column=1)
        self.ButtonRelacion.grid(row=5,column=1)   
        ########################
        self.lbledad = Label(self.lblFrame,text = 'Edad(25-80 años):',width=25)
        self.lblsexo = Label(self.lblFrame,text='Sexo:',width=25)
        self.lblcpselec = Label(self.lblFrame,text = 'Tipo dolor de pecho:',width=25)
        self.lbltrestbps = Label(self.lblFrame,text = 'Pres.sang.Reposo(90-200 mmHg):',width=25)
        self.lblchol = Label(self.lblFrame,text = 'Colesterol(125-570 mg/dl):',width=25)
        self.lblfbs = Label(self.lblFrame,text = 'Nivel Azucar en Ayuno:',width=25)
        self.lblrestecg = Label(self.lblFrame,text = 'ECG en reposo:',width=25)
        self.lblthalach = Label(self.lblFrame,text = 'Max.Ritmo.Card(70-205 bpm):',width=25)
        self.lblexang = Label(self.lblFrame,text = 'Dolor pecho x ejercicio:',width=25)
        self.lbloldpeak = Label(self.lblFrame,text = 'Depresion ST x ejerc.(0-6.2%):',width=25)
        self.lblslope = Label(self.lblFrame,text = 'Pendiente de depresion ST:',width=25)
        self.lblca = Label(self.lblFrame,text = '#Vasos col. x fluorosc.(0-4):',width=25)
        self.lblthal = Label(self.lblFrame,text = 'Talasemia:',width=25)
        self.lblaccu=Label(self.lblFrame2,text="Precision: "+str(round(ac,2)*100)+" %",width=25)

        self.Entryedad = Entry(self.lblFrame,width=20,textvariable = self.edad)
        self.combosexo = ttk.Combobox(self.lblFrame, values=['Masculino','Femenino'],textvariable=self.sexo,width=17)
        self.combocp = ttk.Combobox(self.lblFrame, values=['Angina','Angina Atípica','Dolor no anginoso','Asintomático'],textvariable=self.cp,width=17)
        self.Entrytrestbps = Entry(self.lblFrame,width=20,textvariable = self.trestbps)
        self.Entrychol = Entry(self.lblFrame,width=20,textvariable = self.chol)
        self.combofbs = ttk.Combobox(self.lblFrame, values=['< 120mg/dl','> 120mg/dl'],textvariable=self.fbs,width=17)
        self.comborestecg = ttk.Combobox(self.lblFrame, values=['Normal','Onda ST-T anormal'],textvariable=self.restecg,width=17)
        self.Entrythalach = Entry(self.lblFrame,width=20,textvariable = self.thalach)
        self.comboexang = ttk.Combobox(self.lblFrame, values=['No','Sí'],textvariable=self.exang,width=17)
        self.Entryoldpeak = Entry(self.lblFrame,width=20,textvariable = self.oldpeak)
        self.comboslope = ttk.Combobox(self.lblFrame, values=['Positiva','Plana','Negativa'],textvariable=self.slope,width=17)
        self.Entryca = Entry(self.lblFrame,width=20,textvariable = self.ca)
        self.combothal = ttk.Combobox(self.lblFrame, values=['Normal','Fixed defect','Reversable defect'],textvariable=self.thal,width=17)
        
        
        
        self.ButtonAsig = Button(self.lblFrame2,text = 'Asignamos Valores',command = self.Asignamos)
        self.ButtonAsig.grid(row=0,column=1)
        self.lblaccu.grid(row=0,column=0)
        self.lbledad.grid(row=0,column = 0)
        self.lblsexo.grid(row=1,column = 0)
        self.lblcpselec.grid(row=2,column = 0)
        self.lbltrestbps.grid(row=3,column = 0)
        self.lblchol.grid(row=4,column = 0)
        self.lblfbs.grid(row=5,column = 0)
        self.lblrestecg.grid(row=6,column = 0)
        self.lblthalach.grid(row=7,column = 0)
        self.lblexang.grid(row=8,column = 0)
        self.lbloldpeak.grid(row=9,column = 0)
        self.lblslope.grid(row=10,column = 0)
        self.lblca.grid(row=11,column = 0)
        self.lblthal.grid(row=12,column = 0)
        
        self.Entryedad.grid(row=0,column = 1,padx=10)
        self.combosexo.grid(row=1,column=1)
        self.combocp.grid(row=2,column=1) 
        self.Entrytrestbps.grid(row=3,column = 1)
        self.Entrychol.grid(row=4,column = 1)
        self.combofbs.grid(row=5,column=1)
        self.comborestecg.grid(row=6,column=1)
        self.Entrythalach.grid(row=7,column = 1)
        self.comboexang.grid(row=8,column=1) 
        self.Entryoldpeak.grid(row=9,column = 1)
        self.comboslope.grid(row=10,column=1)
        self.Entryca.grid(row=11,column = 1)
        self.combothal.grid(row=12,column=1)
        
    def Relacion(self):
        if(self.compo1.get()=="Edad"): variable_2="age";
        elif(self.compo1.get()=="Sexo"): variable_2="sex";
        elif(self.compo1.get()=="Tipo de dolor de pecho"): variable_2="cp";
        elif(self.compo1.get()=="Presion sanguinea en reposo (mmHg)"): variable_2="trestbps";
        elif(self.compo1.get()=="Colesterol (mg/dl)"): variable_2="chol";
        elif(self.compo1.get()=="Nivel de azucar en la sangre en ayuno"): variable_2="fbs";
        elif(self.compo1.get()=="Resultados electrocadriograficos"): variable_2="restecg";
        elif(self.compo1.get()=="Frecuencia cardiaca maxima (bpm)"): variable_2="thalach";
        elif(self.compo1.get()=="Angina inducido por ejericio"): variable_2="exang";
        elif(self.compo1.get()=="Depresion del segmento ST (mm)"): variable_2="oldpeak";
        elif(self.compo1.get()=="Pendiente del segmento ST"): variable_2="slope";
        elif(self.compo1.get()=="Numero de vasos principales coloreados por fluoroscopia"): variable_2="ca";
        elif(self.compo1.get()=="Talasemia"): variable_2="thal";
        
        if(self.compo2.get()=="Edad"): variable_3="age";
        elif(self.compo2.get()=="Sexo"): variable_3="sex";
        elif(self.compo2.get()=="Tipo de dolor de pecho"): variable_3="cp";
        elif(self.compo2.get()=="Presion sanguinea en reposo (mmHg)"): variable_3="trestbps";
        elif(self.compo2.get()=="Colesterol (mg/dl)"): variable_3="chol";
        elif(self.compo2.get()=="Nivel de azucar en la sangre en ayuno"): variable_3="fbs";
        elif(self.compo2.get()=="Resultados electrocadriograficos"): variable_3="restecg";
        elif(self.compo2.get()=="Frecuencia cardiaca maxima (bpm)"): variable_3="thalach";
        elif(self.compo2.get()=="Angina inducido por ejericio"): variable_3="exang";
        elif(self.compo2.get()=="Depresion del segmento ST (mm)"): variable_3="oldpeak";
        elif(self.compo2.get()=="Pendiente del segmento ST"): variable_3="slope";
        elif(self.compo2.get()=="Numero de vasos principales coloreados por fluoroscopia"): variable_3="ca";
        elif(self.compo2.get()=="Talasemia"): variable_3="thal";
        
        plt.figure()
        plt.scatter(x=dfgraf[variable_2][dfgraf.target==1],y=dfgraf[variable_3][dfgraf.target==1],c='green')
        plt.scatter(x=dfgraf[variable_2][dfgraf.target==0],y=dfgraf[variable_3][dfgraf.target==0],c='red')
        plt.xlabel(self.compo1.get())
        plt.ylabel(self.compo2.get())
        plt.legend(['Enfermo','No Enfermo'])
        plt.show()
        
        
        
    def Histograma(self):
        if(self.variable.get()=="Edad"): variable_1="age";
        elif(self.variable.get()=="Sexo"): variable_1="sex";
        elif(self.variable.get()=="Tipo de dolor de pecho"): variable_1="cp";
        elif(self.variable.get()=="Presion sanguinea en reposo (mmHg)"): variable_1="trestbps";
        elif(self.variable.get()=="Colesterol (mg/dl)"): variable_1="chol";
        elif(self.variable.get()=="Nivel de azucar en la sangre en ayuno"): variable_1="fbs";
        elif(self.variable.get()=="Resultados electrocadriograficos"): variable_1="restecg";
        elif(self.variable.get()=="Frecuencia cardiaca maxima (bpm)"): variable_1="thalach";
        elif(self.variable.get()=="Angina inducido por ejericio"): variable_1="exang";
        elif(self.variable.get()=="Depresion del segmento ST (mm)"): variable_1="oldpeak";
        elif(self.variable.get()=="Pendiente del segmento ST"): variable_1="slope";
        elif(self.variable.get()=="Numero de vasos principales coloreados por fluoroscopia"): variable_1="ca";
        elif(self.variable.get()=="Talasemia"): variable_1="thal";
        
        pd.crosstab(dfgraf[variable_1],dfgraf["target"]).plot(kind="bar",figsize=(10,5),color=['#11A5AA','#AA1190' ])
        plt.xlabel(self.variable.get())
        plt.xticks(rotation = 0)
        plt.ylabel("Frecuencia")
        plt.legend(['No enfermo','Enfermo'])
        plt.show()
#        plt.figure()
#        plt.hist([dfgraf["target"],dfgraf[variable_1]],color=['red','green'])
#        plt.show()

    def Asignamos(self):
        if(self.sexo.get() == "Masculino"): l_sexo = 1
        else: l_sexo = 0

        if(self.cp.get() == "Angina"): l_cp0 = 1; l_cp1 = 0; l_cp2 = 0; l_cp3 = 0
        elif(self.cp.get() == "Angina Atípica"): l_cp0 = 0; l_cp1 = 1; l_cp2 = 0; l_cp3 = 0
        elif(self.cp.get() == "Dolor no anginoso"): l_cp0 = 0; l_cp1 = 0; l_cp2 = 1; l_cp3 = 0
        elif(self.cp.get() == "Asintomático"): l_cp0 = 0; l_cp1 = 0; l_cp2 = 0; l_cp3 = 1

        if(self.fbs.get() == "> 120mg/dl"): l_fbs = 1
        else: l_fbs = 0
        
        if(self.restecg.get() == "Normal"): l_restecg = 0
        else: l_restecg = 1
        
        if(self.exang.get() == "Sí"): l_exang = 1
        else: l_exang = 0
        
        if(self.slope.get() == "Positiva"): l_slope0 = 1; l_slope1 = 0; l_slope2 = 0
        elif(self.slope.get() == "Plana"): l_slope0 = 0; l_slope1 = 1; l_slope2 = 0
        elif(self.slope.get() == "Negativa"): l_slope0 = 0; l_slope1 = 0; l_slope2 = 1

        if(self.thal.get() == "Normal"): l_thal0 = 1; l_thal1 = 0; l_thal2 = 0
        elif(self.thal.get() == "Fixed defect"): l_thal0 = 0; l_thal1 = 1; l_thal2 = 0
        elif(self.thal.get() == "Reversable defect"): l_thal0 = 0; l_thal1 = 0; l_thal2 = 1

        dft = pd.DataFrame({"age":[(int(self.edad.get())-25)/(80-25)],
                   "sex":[l_sexo],
                   "cp0":[l_cp0],
                   "cp1":[l_cp1],
                   "cp2":[l_cp2],
                   "cp3":[l_cp3],
                   "trestbps":[(int(self.trestbps.get()) - 90)/(200-90)],
                   "chol":[(int(self.chol.get()) - 125)/(570-125)],
                   "fbs":[l_fbs],
                   "restecg":[l_restecg],
                   "thalach":[(int(self.thalach.get()) - 70)/(205-70)],
                   "exang":[l_exang],
                   "oldpeak":[(float(self.oldpeak.get()) - 0)/(6.2-0)],
                   "slope0":[l_slope0],
                   "slope1":[l_slope1],
                   "slope2":[l_slope2],
                   "ca":[(int(self.ca.get()) - 0)/(4-0)],
                   "thal1":[l_thal0],
                   "thal2":[l_thal1],
                   "thal3":[l_thal2]})
        print("")
        print("Datos Ingresados:")
        print(dft)
        y_test_pred = self.model.predict(dft)
        if (round(y_test_pred[0][0]) == 1): res = "Enfermedad Cardiovascular"
        else: res = "Paciente Sano"
        messagebox.showinfo("Predicción", res)
        print("Output:",y_test_pred[0][0])

root = Tk()
app = App(root,model)
root.mainloop()