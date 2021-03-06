# -*- coding: utf-8 -*-



#%%
import numpy as np
import matplotlib.pyplot as plt



#lectura del archivo .txt"
with open('Grupo07_d.txt', mode='r') as file:
    #cada valor se guarda en una lista (data)
    data=file.read().split('\n')

data.pop(len(data)-1)
total_muestra=len(data)
#Valor max y min de la lista (data)
muestra_max=int(max(data))
muestra_min=int(min(data))
#cálculo de umbral
umbral=(muestra_max - muestra_min)*0.85 + muestra_min

#Pico R
muestra_umbral=[]
posicion=[]
val=[]
cycles=0 

for i in range(len(data)):
    if int(data[i])>int(umbral):
        muestra_umbral.append(int(data[i]))
        if int(data[i])>int(data[i-1]) and int(data[i])>=int(data[i+1]):
            posicion.append(i+1)
            val.append(int(data[i]))
            cycles=cycles+1 
            
#Valores para el procesamiento de la señal ECG         
fs=450  #Frecuencia de muestreo
vrefh=3.3   
vrefl=0
ganancia=220
n_bits=10

rango = int(fs * (50*1e-3))
limite_min=[]
limite_max=[]
for i in range(0,len(posicion)):
    limite_min.append(posicion[i] - rango)
    limite_max.append(posicion[i] + rango)

valor_s=[]
posicion_s=[]
for i in range(0,len(posicion)):
    lista1=[]  
    lista2=[]
    for j in range(limite_min[i], limite_max[i]):
        lista1.append(int(data[j]))
        lista2.append(j)#AAAA
    valor_s.append(int(min(lista1)))  
    posicion_s.append(lista2[lista1.index(valor_s[i]) +1])    
    lista1.clear()

#pregunta 1
muestra_sub = posicion[cycles-1]-posicion[0]
t_promedio=muestra_sub/fs
fcp=((cycles-1)*60)/t_promedio  
fcp=round(fcp)
print("Pregunta 1")
print("La frecuencia cardiaca promedio es {} bpm\n".format(fcp))
#pregunta 2
sub=[]


for i in range(0,len(posicion)):
    if i<len(posicion)-1:
        x=posicion[i+1]-posicion[i]
        sub.append(x)
fi=[]   #fi: frecuencia instantánea
for i in range(len(sub)):
    t_aux=sub[i]/fs
    fi.append(round(((1)*60)/t_aux))

dic={}
for i in range(0,len(fi)):
    dic["Instante"+str(i+1)]=fi[i]
    
print("Pregunta 2")
print("Las frecuencia cardiacas instantaneas [bpm]: {}\n".format(fi))

#pregunta 3
arritmia0=[]  
arritmia=[]
for i in range(0,len(sub)):
    arritmia0.append(sub[i]/fs)  

for i in range(0,len(arritmia0)):  
    if i<len(arritmia0)-1:  
        x=arritmia0[i+1]-arritmia0[i]  
        arritmia.append(abs(x))
inst=[]
for i in range(0,cycles-1): 
    inst.append("Instante"+str(i+1))

ritmo={}
for i in range(0,len(fi)):
    if fi[i]<60:    
        ritmo["Instante"+str(i+1)]='Bradicardia'   
    elif fi[i]>100:
        ritmo["Instante"+str(i+1)]='Taquicardia'  
    elif fi[i]>59 and fi[i]<101:
        ritmo["Instante"+str(i+1)]='Normal'
#print(ritmo) ESTO SOLO ES PARA VERIFICAR QUE EL RITMO SALE NORMAL EN TODOS LOS INTANTES
#POR LO TANTO NO PRESENTA ARRITMIA
bradicardia={}
taquicardia={}
for i in range(0,len(fi)):
    if fi[i]<60:
        idx= 'Instante ' + str(i+1)
        bradicardia[idx]=fi[i]
    elif fi[i]>100:
        idx= 'Instante ' + str(i+1)
        taquicardia[idx]=fi[i]   
        
print("\nPregunta 3")

print("No presenta arritmia\n")

if fcp >100:
    print("\nPresenta taquicardia\n")
elif fcp <60:
    print("\nPresenta Bradicardia\n")
else:
    print("\n no presenta taquicardia ni bradicardia")
    


#pregunta 4
precision_ADC= (vrefh - vrefl)/ (2**10)
QRS=[]
for i in range(0,cycles):     
    QRS.append(val[i]-valor_s[i])      
A=[]    # A: amplitud
for i in range(0,cycles):   
    A.append(round(10**3 *((precision_ADC)*QRS[i])/200,3))
V={}
for i in range(0,len(A)):
    V["Instante"+str(i+1)]=A[i]    
print("\nPregunta 4")
print("Amplitudes QRS [mV]: {}".format(A))
print(posicion)
print(val)

import numpy as np
import matplotlib.pyplot as plt

t=np.arange(0,total_muestra,1)
new=[]
for i in range(0,len(data)):
    new.append(int(data[i]))
plt.plot(t,new)
