# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 21:04:26 2020

@author: ASUS
"""

#%%
from sympy.combinatorics.graycode import GrayCode
import numpy as np
import matplotlib.pyplot as plt

bits = '1011100001011111'
n = 4 #  16 (4^2) QAM entonces numero de bits es 4 
M = 2**n
cod_gray = list(GrayCode(n/2).generate_gray())
print(cod_gray)
indi = 0
Ik_bits = ''
Qk_bits = ''

for i in bits:
    if(indi == 0):
        Ik_bits = Ik_bits + i
        indi = 1
    elif(indi == 1):
        Qk_bits = Qk_bits + i
        indi = 0
        
print(Ik_bits)
print('=====')
print(Qk_bits)

val1 = int(len(Ik_bits)/(n/2))
bk_Ik = np.zeros(val1)
#print(bk_Xi)
val2 = int(len(Qk_bits)/(n/2))
bk_Qk = np.zeros(val2)
#print(bk_Xq)

k = 0

for i in range(val1):
    bk_Ik[i] = cod_gray.index(Ik_bits[k:int(k + (n/2))])
    bk_Qk[i] = cod_gray.index(Qk_bits[k:int(k + (n/2))])
#    print(bk_Xi)
#    print(bk_Xq)
    k = int(k+ (n/2))
u = np.log2(M)
#print(u)

correspondencia = np.arange(-u+1,u,2)
#print(correspondencia)

Ik = bk_Ik
Qk = bk_Qk

for i in range(len(bk_Ik)):
    Ik[i] = correspondencia[int(bk_Ik[i])]
    Qk[i] = correspondencia[int(bk_Qk[i])]
print(Ik) 
print(Qk)

#Valores
Ts = 2
Fs = 1/Ts
Fc = 2
Ac = 1

Tb = Ts /(2*n)
Tb_conv = Ts/n
valores = 200
#Portadoras
aux = np.linspace(0,2*np.pi*Fc,valores)
Ac_cos = Ac*np.cos(aux) # Ac* cos(Wc*t)
Ac_sen = -Ac*np.sin(aux) #Ac*sen(Wc*t)

n_bit = 0
cont_a = 0
cont_b = 0
cont_c = 0
val2 = valores/n

fig1= plt.figure(1, figsize=(10,20))

for i in range(len(Ik)):
    fig1.tight_layout(pad=2)
    
    for j in range(n):
        plt.subplot(5,1,1) 
        aux1 = np.linspace(Tb*cont_a, Tb*(cont_a+1),val2)
        aux2 = int(bits[cont_a])
        plt.plot(aux1, np.linspace(aux2, aux2, val2) )
        plt.title('Cadena de bits x(t)', {"color":"blue"}, fontweight="bold")
        cont_a += 1
for i in range(len(Ik)):
    fig1.tight_layout(pad=2)   
    for k in range(int(n/2)):
        plt.subplot(5,1,2)
        var1 = np.linspace(Tb_conv*cont_b, Tb_conv*(cont_b+1),val2)
        var2 = int(Ik_bits[cont_b])
        plt.plot(var1, np.linspace(var2,var2,val2))
        plt.title('Convertidor S/P Xi(t)', {"color":"blue"}, fontweight="bold")
        plt.xlabel('Tiempo', fontweight="bold")
        cont_b+=1
        
for i in range(len(Ik)):
    fig1.tight_layout(pad=2)
    plt.subplot(5,1,3)
    aux_Xi = np.linspace(Ts/2*n_bit, Ts/2*(n_bit+1),valores)
    plt.plot(aux_Xi, np.linspace(Ik[i], Ik[i],valores))
    plt.title('Xi(t)', {"color":"blue"}, fontweight="bold")
    plt.xlabel('Tiempo', fontweight="bold")
    
    plt.subplot(5,1,4)
    #aux2_Xi = np.linspace(Ts/2*n_bit, Ts/2*(n_bit+1),valores)
    plt.plot(aux_Xi, Ac_cos)
    plt.ylabel('Portadora')
    plt.title('Cos(Wc*t)', {"color":"blue"}, fontweight="bold")
    plt.xlabel('Tiempo', fontweight="bold")
    
    #plt.figure(3, figsize=(11,6.5))
    plt.subplot(5,1,5)
    plt.plot(aux_Xi, Ik[i]*Ac_cos)
    plt.title('Xi(t)*Cos(Wc*t)', {"color":"blue"}, fontweight="bold")
    
    n_bit += 1

         
        
        
        
        
        
        