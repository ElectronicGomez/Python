# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 16:08:56 2020

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

for i in range(len(Ik)):
    
    for j in range(n):
        fig1= plt.figure(1, figsize=(10,15))
        fig1.tight_layout(pad=2)
        
        
        plt.subplot(5,1,1) 
        aux1 = np.linspace(Tb*cont_a, Tb*(cont_a+1),val2)
        aux2 = int(bits[cont_a])
        plt.plot(aux1, np.linspace(aux2, aux2, val2) )
        plt.title('Cadena de bits x(t)', {"color":"blue"}, fontweight="bold")
        plt.xlabel('Tiempo', fontweight="bold")
        plt.grid(True)
#        ax =plt.gca()
#        ax.set_ylim(-2,2)
       
        cont_a += 1
        
    for k in range(int(n/2)):
        plt.subplot(5,1,2)
        var1 = np.linspace(Tb_conv*cont_b, Tb_conv*(cont_b+1),val2)
        var2 = int(Ik_bits[cont_b])
        plt.plot(var1, np.linspace(var2,var2,val2))
        plt.title('Convertidor S/P Xi(t)', {"color":"blue"}, fontweight="bold")
        plt.xlabel('Tiempo', fontweight="bold")
        plt.grid(True)
        cont_b+=1
    #plt.figure(2, figsize=(11,5.5))
    plt.subplot(5,1,3)
    aux_Xi = np.linspace(Ts/2*n_bit, Ts/2*(n_bit+1),valores)
    plt.plot(aux_Xi, np.linspace(Ik[i], Ik[i],valores))
    plt.title('Xi(t)', {"color":"blue"}, fontweight="bold")
    plt.xlabel('Tiempo', fontweight="bold")
    plt.grid(True)
    
    plt.subplot(5,1,4)
    #aux2_Xi = np.linspace(Ts/2*n_bit, Ts/2*(n_bit+1),valores)
    plt.plot(aux_Xi, Ac_cos)
    plt.ylabel('Portadora')
    plt.title('Cos(Wc*t)', {"color":"blue"}, fontweight="bold")
    plt.xlabel('Tiempo', fontweight="bold")
    plt.grid(True)
    
    #plt.figure(3, figsize=(11,6.5))
    plt.subplot(5,1,5)
    plt.plot(aux_Xi, Ik[i]*Ac_cos)
    plt.title('Xi(t)*Cos(Wc*t)', {"color":"blue"}, fontweight="bold")
    plt.grid(True)
    
    fig2 = plt.figure(2, figsize=(10,15))
    fig2.tight_layout(pad=2)
    
    for m in range(int(n/2)):
        plt.subplot(511)
        var3 = np.linspace(Tb_conv*cont_c, Tb_conv*(cont_c+1), val2)
        var4 = int(Qk_bits[cont_c])
        plt.plot(var3, np.linspace(var4, var4, val2))
        plt.title('Convertidor S/P Xq(t)', {"color":"blue"}, fontweight="bold")
        plt.grid(True)
        cont_c +=1
    
    plt.subplot(512)
    a = np.linspace(Ts/2*n_bit, Ts/2*(n_bit+1), valores)
    plt.plot(a, np.linspace(Qk[i], Qk[i], valores))
    plt.title('Xq(t)', {"color":"blue"}, fontweight="bold")
    plt.grid(True)
    
    plt.subplot(513)
    plt.plot(a, Ac_sen)
    plt.ylabel('Portadora', fontweight="bold")
    plt.title('-Sen(Wc*t)', {"color":"blue"}, fontweight="bold")
    plt.grid(True)
    
#    plt.figure(5, figsize=(11,6.5))
    plt.subplot(514)
    plt.plot(a, Qk[i]*Ac_sen)
    plt.title('-Xq(t)*Sen(Wc*t)', {"color":"blue"}, fontweight="bold")
    plt.grid(True)
    
    plt.subplot(515)
#    plt.figure(6, figsize=(12,8))
    plt.plot(a, Ik[i]*Ac_cos + Qk[i]*Ac_sen)
    plt.title('Xi(t)*Cos(Wc*t) - Xq(t)*Sen(Wc*t)', {"color":"blue"}, fontweight="bold")
    plt.ylabel('Señal modulada Xc(t)', fontweight="bold")
    plt.xlabel('Tiempo', fontweight="bold")
    plt.grid(True)
    
    n_bit += 1
    
    # HALLAMOS  LAS DEP
    
    valor = 2
    F = np.linspace((-Fc-Fs)*valor, (Fc+Fs)*valor, valores*5)
    
    num1 = ((u**2)-1)/(3*Fs)
    
    Gi = num1*(np.sinc(F/Fs)**2)
    Gq = num1*(np.sinc(F/Fs)**2)
    Glp = Gi + Gq
    
    zinc1 = np.sinc((F+Fc)/Fs)**2
    zinc2 = np.sinc((F-Fc)/Fs)**2
    amplitud = ((Ac**2)/4)*(2*num1)
    
    Gc1 = amplitud*zinc1
    Gc2 = amplitud*zinc2
    
    Gc = Gc1 + Gc2
    
    fig3 = plt.figure(3, figsize=(10,15))
    fig3.tight_layout(pad=2)
    
    plt.subplot(411)
    plt.plot(F,Gi)
    plt.title('DEP de Gi(f)', {"color":"blue"}, fontweight="bold")
    plt.ylabel('Potencia', fontweight="bold")
    plt.xlabel('Frecuencia', fontweight="bold")
    plt.grid(True)
    
    plt.subplot(412)
    plt.plot(F,Gq)
    plt.title('DEP de Gq(f)', {"color":"blue"}, fontweight="bold")
    plt.ylabel('Potencia', fontweight="bold")
    plt.xlabel('Frecuencia', fontweight="bold")
    plt.grid(True)

    plt.subplot(413)
    plt.plot(F,Glp)
    plt.title('DEP de Glp(f)', {"color":"blue"}, fontweight="bold")
    plt.ylabel('Potencia', fontweight="bold")
    plt.xlabel('Frecuencia', fontweight="bold")
    plt.grid(True)
    
    plt.subplot(414)
    plt.plot(F,Gc)
    plt.title('DEP de Gc(f)' , {"color":"blue"}, fontweight="bold")
    plt.ylabel('Potencia', fontweight="bold")
    plt.xlabel('Frecuencia', fontweight="bold")
    plt.grid(True)





    
    
        
            
    
    
    
    
    
    
    










