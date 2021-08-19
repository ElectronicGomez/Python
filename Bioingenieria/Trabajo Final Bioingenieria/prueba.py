import pandas as pd
import numpy as np
import datetime
import matplotlib
#matplotlib.use("TKAgg")
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import roc_curve
from keras.models import Sequential
from keras.layers import Dense
from sklearn.preprocessing import StandardScaler
from sklearn import preprocessing
from sklearn import metrics
from keras import optimizers
from tkinter import *
def entrenar():
    np.random.seed(int(datetime.datetime.now().microsecond))
    global model
    df = pd.read_csv("heartModified(thalDiv).csv")
    print(df.info())
    print('')

    print(df.describe())
    print('')

    print(df.head(10))
    print('')
#    plt.ion()
#    marker_shapes = ['.', '^', '*']
#    for i, resultados in enumerate(df['target'].unique()):
#        if i == 0:
#            ax = df[df['target'] == resultados].plot.scatter(x='trestbps', y='age', marker=marker_shapes[i], s=100,title="Aprobados vs jalados por carreras", label=resultados, figsize=(10,7))
#        else:
#            df[df['target'] == resultados].plot.scatter(x='trestbps', y='age', marker=marker_shapes[i], s=100, title="Aprobados vs jalados por carreras", label=resultados, ax=ax)
#    plt.show()

#df['sex'].plot.hist(title='Histograma de las notas de la PC1')
#matplotlib.pyplot.show()

#Normalizando datos
    X = df.loc[:,['age','sex','cp0','cp1','cp2','cp3',
                  'trestbps','chol','fbs','restecg','thalach',
                  'exang','oldpeak','slope0','slope1','slope2','ca',
                  'thal1','thal2','thal3']]
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
    sgd = optimizers.SGD(lr=0.4)
    model.compile(loss='mean_squared_error', optimizer=sgd)
    model.fit(X, y, epochs=3000, verbose=False)

    print("")
    print("Training Done")
    y_pred = model.predict(X_test)

    ac = metrics.accuracy_score(y_test, y_pred.round())
    print("accuaracy:",ac)
   # ventana.title("Precision de : "+ str(round(ac,2)*100)+"%")
#############################33
entrenar()

edad = (35 - 25)/(80-25)
sex=1
cp0=1
cp1=0
cp2=0
cp3=0
trest = (126- 90)/(200-90)
chol = (282 - 125)/(570-125)
fbs=0
restecg=0
thalach= (156 - 70)/(205-70)
exang=1
olpeak = (0 - 0)/(6.2-0)
slope0=0
slope1=0
slope2=1
ca = (0 - 0)/(4-0)
thal1=0
thal2=0
thal3=1
dft1=pd.DataFrame({"age":[edad],"sex":[sex],"cp0":[cp0],"cp1":[cp1],"cp2":[cp2],"cp3":[cp3],
                   "trestbps":[trest],"chol":[chol],"fbs":[fbs],"restecg":[restecg],"thalach":[thalach],
                   "exang":[exang],"oldpeak":[olpeak],"slope0":[slope0],"slope1":[slope1],"slope2":[slope2],"ca":[ca],
                   "thal1":[thal1],"thal2":[thal2],"thal3":[thal3]})
ysal=model.predict(dft1)
print(ysal)

############################################33333
ab=4
def predi ():
    global ab
    global valor
    b=ab+3
    print("Hola"+str(b))
    print(valor.get())
    
    
    
    
    
ventana = Tk()
ventana.geometry("500x500+0+0")
ventana.resizable(width=FALSE,height=FALSE)


etiqueta2=Label(ventana,text="respuesta").place(x=20,y=50)
#Establecimiento de entradas
edad=IntVar(value="25")
sexo=IntVar()
valor=IntVar()
#Botones
Spinbox(ventana,value=["Angina","Angina atipica","etc"],textvariable=valor).place(x=20,y=110)


#Boton para ejecutar ingreso
boton=Button(ventana,text="Ejecutar Operacion",command=predi).place(x=20,y=140)
#Boton para entrenar
boton=Button(ventana,text="Entrenar",command=entrenar).place(x=20,y=180)
#Cerrar Tkinter
ventana.mainloop()




























