# -*- coding: utf-8 -*-
"""
Created on Fri May 15 20:56:55 2020

@author: ASUS
"""



maquina = {'G11':[2,1],'G12':[2,2],'G13':[2,4],'G14':[2,2.5],
            'G21':[2,1],'G22':[2,2],'G23':[2,4],'G24':[2,2.5],
            'G31':[2,1],'G32':[2,2],'G33':[2,4],'G34':[2,2.5],
            'G41':[2,1],'G42':[2,2],'G43':[2,4],'G44':[2,2.5]}


while True:
    while True:
    
        try:
            efectivo = float(input("(1)	Ingresar dinero: "))
            if efectivo>=1 and efectivo<=10:
                break
            else:
                print("El monto a ingresar debe estar en el rango 1 y 10")
        except:
            print("El monto a ingresar debe estar en el rango 1 y 10")

    

    while True:

        try:
            pos = input("(2)	Seleccionar gaseosa[G11-G44]: ")

            if pos in maquina.keys():
                break
            else:
                print("La posicion debe estar entre G11 y G44")
        except:
            print("La posicion debe estar entre G11 y G44")

    precio = maquina[pos][1]
    vuelto = efectivo -precio

    
    if vuelto > 0:
        print("----------------- Despachado -----------------")
        print("Vuelto: ", vuelto)
        maquina[pos][0] = maquina[pos][0]-1
        print("Quedan: ", maquina[pos][0])
    elif vuelto < 0:
        print("El monto ingresado no alcanza para el producto seleccionado, ingrese de nuevo")
    while True:
        try:
            reiniciar = input("(3)	Reiniciar el sistema[yes/no]: ")
            if reiniciar == 'yes' or reiniciar == 'no':
                break
            else:
                print("debe colocar yes o no")
        except:
            print("debe colocar yes o no")

    if reiniciar == 'yes':
        maquina = {'G11':[2,1],'G12':[2,2],'G13':[2,4],'G14':[2,2.5],
                   'G21':[2,1],'G22':[2,2],'G23':[2,4],'G24':[2,2.5],
                   'G31':[2,1],'G32':[2,2],'G33':[2,4],'G34':[2,2.5],
                   'G41':[2,1],'G42':[2,2],'G43':[2,4],'G44':[2,2.5]}
        
        
        
        
        
        
        
        
        
        