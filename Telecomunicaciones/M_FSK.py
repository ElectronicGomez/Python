# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 21:15:19 2020

@author: ASUS
"""
#%%
#%%
#%%
from sympy.combinatorics.graycode import GrayCode
import numpy as np
import matplotlib.pyplot as plt


fb=1
factor_c=2
Ts=1
fs=1/Ts
n=1
Tb=Ts/n
Ac=2
fc=factor_c
num_bit=0
puntos_c=200
dirac=0.000015
cadena_bits = '1011'
M = 2**n
lista_gray = list(GrayCode(n).generate_gray())
print(lista_gray)
corri=0
dec=np.zeros(int(len(cadena_bits)/n))
for x in range(int(len(cadena_bits)/n)):
    dec[x]=lista_gray.index(cadena_bits[corri:corri+n])
    corri=corri+n
tabla=np.arange(-M+1,M,2)
bk=np.zeros(len(dec))
Qk=np.zeros(len(dec))
for x in range(len(dec)):
        bk[x]=tabla[int(dec[x])]
        Qk[x]=(-1)**x*bk[x]
cos_por=Ac*np.cos(np.linspace(0,2*np.pi*fb*factor_c,puntos_c))
sen_ele=np.sin(np.linspace(0,np.pi*fb,puntos_c))
sen_por = -Ac*np.sin(np.linspace(0,2*np.pi*fb*factor_c, puntos_c))
corri_b=0
alter=0

for x in range(len(bk)):
    
        fig1= plt.figure(1, figsize=(10,15))
        fig1.tight_layout(pad=2)
        cos_xi=np.cos(np.linspace(0,np.pi*fb*bk[x],puntos_c))
        cos_xi_2=np.cos(np.linspace(np.pi*fb*bk[x],2*np.pi*fb*bk[x],puntos_c))
        
        for y in range(n):
            plt.subplot(411)
            plt.plot(np.linspace(int(Tb*corri_b),int(Tb*(corri_b+1)),int((puntos_c)/n)),np.linspace(int(cadena_bits[corri_b]),int(cadena_bits[corri_b]),int(puntos_c/n)))
            plt.title('cadena bits x(t)')#grafico cadena d e bits
            corri_b=corri_b+1
        #grafica de xi(t)
            if(alter==0):
                plt.subplot(412)
                plt.plot(np.linspace(Ts*num_bit,Ts*(num_bit+1),puntos_c),cos_xi)
                plt.title('xi(t)')
            elif(alter==1):
                plt.subplot(412)
                plt.plot(np.linspace(Ts*num_bit,Ts*(num_bit+1),puntos_c),cos_xi_2)
                plt.title('xi(t)')
            #grafica de portadora
            plt.subplot(413)
            plt.plot(np.linspace(Ts*num_bit,Ts*(num_bit+1),puntos_c),cos_por)
            plt.title('Cos(wct)')
            #grafica xi*portadora
            if(alter==0):
                plt.subplot(414)
                plt.plot(np.linspace(Ts*num_bit,Ts*(num_bit+1),puntos_c),cos_por*cos_xi)
                plt.title('xi(t)*Cos(wct)')
            elif(alter==1):
                plt.subplot(414)
                plt.plot(np.linspace(Ts*num_bit,Ts*(num_bit+1),puntos_c),cos_por*cos_xi_2)
                plt.title('xi(t)*Cos(wct)')
            
            fig2= plt.figure(2, figsize=(10,15))
            fig2.tight_layout(pad=2)
            
            #grafica de bk
            
            plt.subplot(511)
            plt.plot(np.linspace(Ts*num_bit,Ts*(num_bit+1),puntos_c),np.linspace(bk[x],bk[x],puntos_c))
            plt.title('bk(t)')

            #grafica pulso elemental
            plt.subplot(512)
            plt.plot(np.linspace(Ts*num_bit,Ts*(num_bit+1),puntos_c),sen_ele)
            plt.title('Sen(pi*fb*t) "Pulso elemental"')
            
            sen_new=np.sin(np.linspace(0,np.pi*fb*Qk[x],puntos_c))
            
            #grafica seno por Qk
            
            plt.subplot(513)
            plt.plot(np.linspace(Ts*num_bit,Ts*(num_bit+1),puntos_c),sen_new)
            plt.title('xq(t)')
            
            #grafica portadora
            plt.subplot(514)
            plt.plot(np.linspace(Ts*num_bit,Ts*(num_bit+1),puntos_c),sen_por)
            plt.title('-Sen(wct)')
            
            #grafica -xq*portadora
            plt.subplot(515)
            plt.plot(np.linspace(Ts*num_bit,Ts*(num_bit+1),puntos_c),sen_new*sen_por)
            plt.title('-xq(t)*Sen(wct)')

        #grafica de xc(t)
        
            fig3= plt.figure(3, figsize=(10,15))
            fig3.tight_layout(pad=2)
            
            if(alter==0):
                plt.subplot(511)
                plt.plot(np.linspace(Ts*num_bit,Ts*(num_bit+1),puntos_c), sen_new*sen_por+cos_por*cos_xi)
                plt.title('xi(t)*Cos(wct)-xq(t)*Sen(wct)')
                alter=1
            elif(alter==1):
                plt.subplot(511)
                plt.plot(np.linspace(Ts*num_bit,Ts*(num_bit+1),puntos_c), sen_new*sen_por+cos_por*cos_xi_2)
                plt.title('xi(t)*Cos(wct)-xq(t)*Sen(wct)')
                alter=0
            num_bit=num_bit+1
        
        factor=2
        factor_puntos=500
        f=np.linspace((-fc-3*fb/2)*factor,(fc+3*fb/2)*factor,puntos_c*factor_puntos)
        
        Gc1=((Ac**2)/4)*((4)/((np.pi**2)*fb))*(np.cos(np.pi*(f+fc)/fb)/((2*(f+fc)/fb)**2-1))**2
        Gc2=((Ac**2)/4)*((4)/((np.pi**2)*fb))*(np.cos(np.pi*(f-fc)/fb)/((2*(f-fc)/fb)**2-1))**2
        Gc=Gc1+Gc2
        
        Gi=0*f
        Gq=((4)/((np.pi**2)*fb))*(np.cos(np.pi*(f)/fb)/((2*(f)/fb)**2-1))**2
        Glp=Gi+Gq
        
        #graficos de las dep correspondientes
        plt.subplot(512)
        plt.plot(np.linspace((-fc-fs)*factor,(fc+fs)*factor,puntos_c*factor_puntos),Gi)
        plt.plot([fb/2,fb/2+dirac],[1/4,0])
        plt.plot([-fb/2,-fb/2+dirac],[1/4,0])
        plt.title('DEP Gi(f)')
        
        plt.subplot(513)
        plt.plot(np.linspace((-fc-fs)*factor,(fc+fs)*factor,puntos_c*factor_puntos),Gq)
        plt.title('DEP Gq(f)')
        
        plt.subplot(514)
        plt.plot(np.linspace((-fc-fs)*factor,(fc+fs)*factor,puntos_c*factor_puntos),Glp)
        plt.title('DEP Glp')
        

        
    




        
    


