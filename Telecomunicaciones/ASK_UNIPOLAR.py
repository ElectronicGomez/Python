# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 10:46:41 2020

@author: ASUS
"""

#%% ASK UNIPOLAR (ON - OFF)
from sympy.combinatorics.graycode import GrayCode
import numpy as np
import matplotlib.pyplot as plt

cadena = '1011'

n = 1 #Numero de bits
M = 2**n 

cod_gray = list(GrayCode(n).generate_gray()) #Se genera una lista para tabla gray de n bits
print(cod_gray)

var = 0
ak = np.zeros(int(len(cadena)/n)) #Formato 0,1...(M-1) unipolar


for i in range(int(len(cadena)/n)):
    ak[i] = cod_gray.index(cadena[var:var+n])
    var = var + n

var = 0

Ts = 1 #Tiempo de simbolo
fs = 1 / Ts #Frecuencia de simbolo
Tb = Ts//n #Tiempo de bit redondeado al menor entero
Ac = 1
fc = 2
valores = 400
n_bit = 0

aux = np.linspace(0,2*np.pi*fc,valores)
Ac_cos = Ac*np.cos(aux) # Ac* cos(Wc*t)


xct = []
ondas = []
for i in ak:
    ondas.append(list(Ac_cos*i))
    xct = xct + list(Ac_cos*i) #Señal modulada

# ondas = [[],[],[],[]]
t = np.linspace(0, Tb*len(cadena),len(xct))

plt.close('all')
fig1 = plt.figure(1, figsize=(10,15))
fig1.tight_layout(pad=2)

ax1 = fig1.add_subplot(612)
ax1.set_xlim([0,5])
ax1.plot(t,xct,'g') #Señal modulada entrada al filtro adaptado
plt.title('Señal modulada entrada al filtro adaptado', {"color":"blue"}, fontweight="bold")
plt.xlabel('Tiempo', fontweight="bold")
plt.grid(True)

xct_ruido = xct + np.random.normal(scale=0.354,size=1600)
ax2 = fig1.add_subplot(613)
ax2.set_xlim([0,5])
ax2.plot(t,xct_ruido, 'r')
plt.title('Señal modulada entrada al filtro adaptado ASK(ON-OFF) - Con ruido', {"color":"blue"}, fontweight="bold")
plt.xlabel('Tiempo', fontweight="bold")
plt.grid(True)    

zt = []
k = 0
Eb = Ac**2*Tb/4
K = Ac/Eb

cont_a=0
val2= valores/len(cadena)
for i in range(len(cadena)):
    
    for j in range(n):
        fig1= plt.figure(1, figsize=(10,15))
        fig1.tight_layout(pad=2)
        
        
        plt.subplot(611) 
        aux1 = np.linspace(Tb*cont_a, Tb*(cont_a+1),val2)
        aux2 = int(cadena[cont_a])
        plt.plot(aux1, np.linspace(aux2, aux2, val2) )
        plt.title('Cadena de bits x(t)', {"color":"blue"}, fontweight="bold")
        plt.xlabel('Tiempo', fontweight="bold")
        plt.grid(True)
#     
        cont_a += 1


for i in ondas:
    for idx in range(len(i)):
        if i[idx] !=0: #Z11
            val_z = idx+(valores*n_bit)
            if t[val_z]>=k*Tb and t[val_z]<k+1:
                a = (Ac_cos[idx]/2)*(t[val_z]-k*Tb)
                zt.append(K*Ac**2*a)
            else:
                b = (Ac_cos[idx]/2)*((k+2)*Tb-t[val_z])
                zt.append(K*Ac**2*b)
        else: #Z01
            zt.append(0)
    k= k+1
    n_bit = n_bit+1

ax3 = fig1.add_subplot(614)
ax3.set_xlim([0,5])
ax3.plot(t,zt,'b')
plt.title('Salida del filtro adaptado: ASK(ON-OFF)', {"color":"blue"}, fontweight="bold")
plt.xlabel('Tiempo', fontweight="bold")
plt.grid(True)
            
Zm = []
for i in range(valores*Tb, len(zt)+1, valores*Tb):
    Zm = Zm + [zt[i-1] for j in range(valores*Tb)]

t = np.linspace(Tb, Tb*len(cadena)+1, len(Zm))

ax4 = fig1.add_subplot(615)
ax4.set_xlim([0,5])
ax4.plot(t,Zm,'b')
plt.title('Salida del S/H: ASK(ON-OFF)', {"color":"blue"}, fontweight="bold")
plt.xlabel('Tiempo', fontweight="bold")
plt.grid(True)
    
señal_dem = []

for i in range(len(Zm)):
    if Zm[i]>K*Eb:
        señal_dem.append(1)
    else:
        señal_dem.append(0)
    
ax5 = fig1.add_subplot(616)
ax5.plot(t,señal_dem,lw=5, c='c')
plt.title('Señal demodulada : ASK(ON-OFF)', {"color":"blue"}, fontweight="bold")
plt.xlabel('Tiempo', fontweight="bold")
plt.grid(True)
            
#FILTRO CORRELADOR
fig2 = plt.figure(2)

zt=[]
k=0
Eb=Ac**2*Tb/4
K=Ac/Eb
n_bit=0
t = np.linspace(0, Tb*len(cadena),len(xct))  
Ac_sen=Ac*np.sin(np.linspace(0,4*np.pi*fc, valores))

for i in ondas:
    for idx in range(len(i)): #Z11
        if i[idx]!=0:
            val_z = idx+(valores*n_bit)
            a = (t[val_z]-k*Tb)+(Ac_sen[idx]/(2*2*np.pi*fc))
            zt.append((K*Ac**2/2)*a)
        else:
            zt.append(0)
    k = k+1
    n_bit=n_bit+1

ax2_1 = fig2.add_subplot(311)
ax2_1.set_xlim([0,5])
plt.plot(t,zt, c='r')
plt.title('Salida  del filtor correlador : ASK(ON-OFF)', {"color":"blue"}, fontweight="bold")
plt.xlabel('Tiempo', fontweight="bold")
plt.grid(True)

Zm2 = []
for i in range(valores*Tb,len(zt)+1, valores*Tb):
    Zm2 = Zm2+[zt[i-1] for j in range(valores*Tb)]
    
t = np.linspace(Tb, Tb*len(cadena)+1, len(Zm2))

ax2_2 = fig2.add_subplot(312)
ax2_2.set_xlim([0,5])
ax2_2.plot(t,Zm2,'b')
plt.title('Salida del S/H: ASK(ON-OFF)', {"color":"blue"}, fontweight="bold")
plt.xlabel('Tiempo', fontweight="bold")
plt.grid(True)
                 
señal_dem2 = []

for i in range(len(Zm2)):
    if Zm2[i]>K*Eb:
        señal_dem2.append(1)
    else:
        señal_dem2.append(0)
    
ax2_3 =fig2.add_subplot(313)
ax2_3.plot(t,señal_dem,lw=5, c='c')
plt.title('Señal demodulada : ASK(ON-OFF)', {"color":"blue"}, fontweight="bold")
plt.xlabel('Tiempo', fontweight="bold")
plt.grid(True)    
    
    
    
    
    
    
    
    
    

