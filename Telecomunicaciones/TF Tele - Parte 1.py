# -*- coding: utf-8 -*-

# se importan las librerias necesarias
import numpy as np
import matplotlib.pyplot as plt
import math
from sympy.combinatorics.graycode import GrayCode

#%%

#se cierran las ventanas abiertas
plt.close('all')

#funcion Q
def Q(x):
    a=0.5-0.5*math.erf(x/math.sqrt(2))
    return a

#funcion para hallar varianza del caso polar y snr
def db_snr(db,M,N,Ac):
    snr=pow(10,db/10)  
    aa=(M**2-1)/3   
    varianza_ruido=(Ac*aa)/(2*snr*N)
    return snr, varianza_ruido

#creacion de los valores aleatorios
num_valores=100000*3
cadena_bits=np.random.randint(2, size=num_valores)
Ac=1

cadena_str=''
for x in cadena_bits:
    cadena_str=cadena_str+str(x)
cadena_bits=cadena_str


#creacion de tabla gray y tabla polar
n=3#numero de bits 
M=2**n #se halla el valor de M

lista_gray=list(GrayCode(n).generate_gray()) #se genera una lista tabla gray de n bits
corri=0
ak=np.zeros(int(len(cadena_bits)/n))
tabla_polar=np.arange(-M+1,M,2)          #tabla polar para el caso polar

for x in range(int(len(cadena_bits)/n)):
    ak[x]=tabla_polar[int(lista_gray.index(cadena_bits[corri:corri+n]))] 
    corri=corri+n

sh_demo=ak*Ac

#datos de creacion de los BER
min_ber=1
max_ber=10
salto_ber=1

ber_ejex=np.arange(min_ber,max_ber,salto_ber)
ber_ejey=[]
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
    
#se halla el ber
for x in range(len(sh_ruido)):
    error=0
    for y in range(len(cadena_bits)):
        if int(array_salida[x][y]) != int(cadena_bits[y]):
              error=error+1         
    ber_ejey.append(error/len(cadena_bits))
    
    
#Pub teorico
snr_t=np.linspace(0,10,1500)
raiz=np.sqrt(snr_t)
Pu=[]
for x in snr_t:
    Pu.append(((2/n)*(1-1/M))*Q(np.sqrt(((6*n)/(M**2-1))*x)))
    
snr_tdb=10*np.log10(snr_t)


#Se grafican los BER y la curva teorica
plt.figure(1)
plt.plot(snr_tdb,Pu,'b',ber_ejex,ber_ejey,'rx')#,snr_tdb,funQ
plt.legend(('Pub Teorico','BER'),prop={'size':15})
plt.title("Pub y BER vs SNR")
plt.xlabel("SNR (db)")
plt.ylabel("Pb")
plt.yscale('log')
plt.xlim((0,10))
plt.grid(True)






#%%%%%%%%%%% ASK - ON OFF y POLAR
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
    return X

def bits_diff_num(num_1,num_2):
    count=0;
    for i in range(0,len(num_1),1):
        if num_1[i]!=num_2[i]:
            count=count+1
    return count
 
def viterbi(obs, start_metric, state_machine):
    #Trellis structure
    V = [{}]
    for st in state_machine:
        # Calculating the probability of both initial possibilities for the first observation
        V[0][st] = {"metric": start_metric[st]}
    #for t>0
    for t in range(1, len(obs)+1):
        V.append({})
        for st in state_machine:
            #Check for smallest bit difference from possible previous paths, adding with previous metric
            prev_st = state_machine[st]['b1']['prev_st']
            first_b_metric = V[(t-1)][prev_st]["metric"] + bits_diff_num(state_machine[st]['b1']['out_b'], obs[t - 1])
            prev_st = state_machine[st]['b2']['prev_st']
            second_b_metric = V[(t - 1)][prev_st]["metric"] + bits_diff_num(state_machine[st]['b2']['out_b'], obs[t - 1])
            #print(state_machine[st]['b1']['out_b'],obs[t - 1],t)
            if first_b_metric > second_b_metric:
                V[t][st] = {"metric" : second_b_metric,"branch":'b2'}
            else:
                V[t][st] = {"metric": first_b_metric, "branch": 'b1'}
    smaller = min(V[len(obs)-1][st]["metric"] for st in state_machine)    
    #traceback the path on smaller metric on last trellis column
    decoded = ""
    for st in state_machine:
        if V[len(obs)][st]["metric"] <= smaller:
            source_state = st
            for t in range(len(obs),0,-1):
                print(t)
                branch = V[t][source_state]["branch"]
                decoded+=str(state_machine[source_state][branch]['input_b'])
                source_state = state_machine[source_state][branch]['prev_st']
            print(state_machine[source_state][branch]['input_b'])
    return decoded[-1::-1]

#se cierran las ventanas abiertas
plt.close('all')

#funcion Q
def Q(x):
    a=0.5-0.5*math.erf(x/math.sqrt(2))
    return a

#funcion para hallar varianza del caso polar y snr
def db_snr(db,M,N,Ac):
    snr=pow(10,db/10)  
    aa=(M**2-1)/3   
    varianza_ruido=(Ac*aa)/(2*snr*N)
    return snr, varianza_ruido

#creacion de los valores aleatorios
num_valores=10
cadena_bits=np.random.randint(2, size=num_valores)
Ac=1

cadena_str=''
for x in cadena_bits:
    cadena_str=cadena_str+str(x)
cadena_bits=cadena_str

cadena_bits=codificadorConv212(cadena_bits)
#creacion de tabla gray y tabla polar
n=3#numero de bits 
M=2**n #se halla el valor de M

lista_gray=list(GrayCode(n).generate_gray()) #se genera una lista tabla gray de n bits
corri=0
ak=np.zeros(int(len(cadena_bits)/n))
tabla_polar=np.arange(-M+1,M,2)          #tabla polar para el caso polar

for x in range(int(len(cadena_bits)/n)):
    ak[x]=tabla_polar[int(lista_gray.index(cadena_bits[corri:corri+n]))] 
    corri=corri+n

sh_demo=ak*Ac

#datos de creacion de los BER
min_ber=1
max_ber=10
salto_ber=1

ber_ejex=np.arange(min_ber,max_ber,salto_ber)
ber_ejey=[]
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

start_metric = {'zero':0,'one': 10, 'two': 10,'three':10}
state_machine = {
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

array_decod = []
for codificado in array_salida:
    obs = [codificado[i:i+2] for i in range(0,len(codificado),2)]
    array_decod.append(viterbi(obs,start_metric,state_machine))
#se halla el ber
for x in range(len(sh_ruido)):
    error=0
    for y in range(len(cadena_bits)):
        if int(array_decod[x][y]) != int(cadena_bits[y]):
              error=error+1         
    ber_ejey.append(error/len(cadena_bits))
    
    
#Pub teorico
snr_t=np.linspace(0,10,1500)
raiz=np.sqrt(snr_t)
Pu=[]
for x in snr_t:
    Pu.append(((2/n)*(1-1/M))*Q(np.sqrt(((6*n)/(M**2-1))*x)))
    
snr_tdb=10*np.log10(snr_t)


#Se grafican los BER y la curva teorica
plt.figure(1)
plt.plot(snr_tdb,Pu,'b',ber_ejex,ber_ejey,'rx')#,snr_tdb,funQ
plt.legend(('Pub Teorico','BER'),prop={'size':15})
plt.title("Pub y BER vs SNR")
plt.xlabel("SNR (db)")
plt.ylabel("Pb")
plt.yscale('log')
plt.xlim((0,10))
plt.grid(True)


"011101101001111011"
"00110110100111001110"


    