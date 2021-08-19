# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import math
from sympy.combinatorics.graycode import GrayCode

#%%
# plt.close('all')

def Q(x):
    a=0.5-0.5*math.erf(x/math.sqrt(2))
    return a

def db_snr(db,M,N,Ac):
    snr=pow(10,db/10)  
    aa=(M**2-1)/3   
    varianza_ruido=(Ac*aa)/(2*snr*N)
    return snr, varianza_ruido

def codificadorConv212(mensaje):
    mj1=0
    mj2=0
    X=""
    for bit in mensaje:
        xprima = mj2^mj1^int(bit)
        x2prima = mj2^int(bit)
        X+=str(xprima)+str(x2prima)
        mj2 = mj1
        mj1 = int(bit)
    X+="00"
    return X

def bits_diff_num(num_1,num_2):
    count=0;
    for i in range(0,len(num_1),1):
        if num_1[i]!=num_2[i]:
            count=count+1
    return count
 
def viterbi(obs, metricaInicial, maquinaEstado):
    #Trellis structure
    V = [{}]
    for st in maquinaEstado:
        # Calculando la metrica del estado inicial
        V[0][st] = {"metric": metricaInicial[st]}
    #for t>0
    for t in range(1, len(obs)+1):
        V.append({})
        for st in maquinaEstado:
            #Revisa la metrica mas pequeñas y se añade con la anterior
            prev_st = maquinaEstado[st]['b1']['prev_st']
            first_b_metric = V[(t-1)][prev_st]["metric"] + bits_diff_num(maquinaEstado[st]['b1']['out_b'], obs[t - 1])
            prev_st = maquinaEstado[st]['b2']['prev_st']
            second_b_metric = V[(t - 1)][prev_st]["metric"] + bits_diff_num(maquinaEstado[st]['b2']['out_b'], obs[t - 1])
            if first_b_metric > second_b_metric:
                V[t][st] = {"metric" : second_b_metric,"branch":'b2'}
            else:
                V[t][st] = {"metric": first_b_metric, "branch": 'b1'}
    smaller = min(V[len(obs)][st]["metric"] for st in maquinaEstado)    
    #traceback del camino con la menor metrica en la ultima columna del diagrama de Trellis
    print(V[len(obs)][st]["metric"] for st in maquinaEstado)
    decoded = ""
    print(smaller)
    for st in maquinaEstado:
        print(V[len(obs)][st]["metric"])
        if V[len(obs)][st]["metric"] <= smaller:
            source_state = st
            cont=1
            for t in range(len(obs),0,-1):
                branch = V[t][source_state]["branch"]
                decoded+=str(maquinaEstado[source_state][branch]['input_b'])
                source_state = maquinaEstado[source_state][branch]['prev_st']
    return decoded[-1::-1]

def askConRuido(mensaje,N,M,Ac):
    
    lista_gray=list(GrayCode(n).generate_gray()) #se genera una lista tabla gray de n bits
    corri=0
    ak=np.zeros(int(len(mensaje)/n))
    tabla_polar=np.arange(-M+1,M,2)          #tabla polar para el caso polar
    
    for x in range(int(len(mensaje)/n)):
        ak[x]=tabla_polar[int(lista_gray.index(mensaje[corri:corri+n]))] 
        corri=corri+n
    
    sh_demo=ak*Ac
    
    #datos de creacion de los BER
    min_ber=1
    max_ber=10
    salto_ber=1
    
    ber_ejex=np.arange(min_ber,max_ber,salto_ber)
    sh_ruido=[]
    
    #se agrega el ruido al SH
    for x in ber_ejex:
        snr_ber,var_ber=db_snr(x,M,n,Ac)
        desv_ber=np.sqrt(var_ber)
        
        sh_ruido.append(sh_demo+np.random.normal(0,desv_ber,len(ak)))
        
    #bloque cuantizador para aproximacion de valores segun umbral
    cuantizador=[]
    for x in range(len(sh_ruido)):
        cadenacua=[]
        for y in range(len(ak)):
            if sh_ruido[x][y]<-6*Ac:
                cadenacua.append(-7)
            elif sh_ruido[x][y]<-4*Ac:
                cadenacua.append(-5)
            elif sh_ruido[x][y]<-2*Ac:
                cadenacua.append(-3)
            elif sh_ruido[x][y]<0:
                cadenacua.append(-1)
            elif sh_ruido[x][y]<2*Ac:
                cadenacua.append(1)
            elif sh_ruido[x][y]<4*Ac:
                cadenacua.append(3)
            elif sh_ruido[x][y]<6*Ac:
                cadenacua.append(5)
            else:
                cadenacua.append(7)
        cuantizador.append(cadenacua)
    
    
    #convertidor de datos
    array_salida=[]
    for x in range(len(cuantizador)):
        cadena_salida=''
        for y in range(len(ak)):
            cadena_salida=cadena_salida+lista_gray[np.where(tabla_polar==cuantizador[x][y])[0][0]]
        array_salida.append(cadena_salida)
    return [array_salida,ber_ejex]

def Ber(entrada, salida):
    ber=[]
    for x in range(len(salida)):
        error=0
        for y in range(len(entrada)):
            if int(salida[x][y]) != int(entrada[y]):
                  error=error+1         
        ber.append(error/len(entrada))
    return ber
    

#%%%%%%%%%%% Codificador Convolucional ()




cadena_bits=np.random.randint(2, size=300000)
cadena = list(map(lambda x:str(x),cadena_bits))
cadena_bits="".join(cadena)
 #Codificacion del mensaje
cod = codificadorConv212("".join(cadena_bits))


#Modulacion y demodulacion con ruido
Ac=1
n=3
M=2**n

arraycod_salida, ber_ejex = askConRuido(cod,n,M,Ac)


metricaInicial = {'zero':0,'one': 10, 'two': 10,'three':10}
maquinaEstado = {
    #estado actual, posibles ramas, informacion de la rama
    'zero': {'b1': {'out_b':"11",'prev_st': 'three','input_b':0},
             'b2': {'out_b':"00",'prev_st': 'zero','input_b':0}},
    'one': {'b1': {'out_b': "00", 'prev_st': 'three', 'input_b': 1},
             'b2': {'out_b': "11", 'prev_st': 'zero', 'input_b': 1}},
    'two': {'b1': {'out_b': "01", 'prev_st': 'one', 'input_b': 1},
             'b2': {'out_b': "10", 'prev_st': 'two', 'input_b': 1}},
    'three': {'b1': {'out_b': "10", 'prev_st': 'one', 'input_b': 0},
             'b2': {'out_b': "01", 'prev_st': 'two', 'input_b': 0}},
}
mensajes_decod = []
#Se decodifican todos los mensajes demodulados
for mensaje in arraycod_salida:
    obs = [mensaje[i:i+2] for i in range(0,len(mensaje),2)]
    obs = list(filter(lambda x: len(x)==2,obs))
    mensajes_decod.append(viterbi(obs,metricaInicial,maquinaEstado))

#Se obtiene los BER sin codificar
array_salida, ber_ejex = askConRuido(cadena_bits,n,M,Ac)
ber_ejey = Ber(cadena_bits,array_salida)

#Se obtiene el BER codificado
bercod_ejey = Ber(cadena_bits,mensajes_decod)



snr_t=np.linspace(0,10,1500)

raiz=np.sqrt(snr_t)

Pub=[]

for x in snr_t:
    Pub.append(((2/n)*(1-1/M))*Q(np.sqrt(((6*n)/(M**2-1))*x)))
    
snr_tdb=10*np.log10(snr_t)

plt.figure(1)

plt.close("all")
plt.plot(snr_tdb,Pub,'b',ber_ejex,ber_ejey,'kx', ber_ejex, bercod_ejey, 'rx')
plt.legend(('Pub Teorico','BERub','BER b'),prop={'size':15})
plt.title("Pub y BER vs SNR")

plt.xlabel("SNR (db)")
plt.ylabel("Pub")
plt.yscale('log')
plt.xlim((0,10))

plt.grid(True)

#%%
test2 = codificadorConv212("1100010101")
metricaInicial = {'zero':0,'one': 10, 'two': 10,'three':10}
maquinaEstado = {
    #current state, possible branches, branch information
    'zero': {'b1': {'out_b':"11",'prev_st': 'three','input_b':0},
             'b2': {'out_b':"00",'prev_st': 'zero','input_b':0}},
    'one': {'b1': {'out_b': "00", 'prev_st': 'three', 'input_b': 1},
             'b2': {'out_b': "11", 'prev_st': 'zero', 'input_b': 1}},
    'two': {'b1': {'out_b': "01", 'prev_st': 'one', 'input_b': 1},
             'b2': {'out_b': "10", 'prev_st': 'two', 'input_b': 1}},
    'three': {'b1': {'out_b': "10", 'prev_st': 'one', 'input_b': 0},
             'b2': {'out_b': "01", 'prev_st': 'two', 'input_b': 0}},
}
#1100010101
test="11010111001110001000"
     "000011100000010110"
cod = [test[i:i+2] for i in range(0,len(test),2)]
dec = viterbi(cod,metricaInicial,maquinaEstado)
print(cod)
print(dec)
print(test2)
"000011100001100100010"
"0000111000011001000100"
