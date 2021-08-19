# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 18:06:50 2020

@author: ASUS
"""

#%%

import serial.tools.list_ports

ports = serial.tools.list_ports.comports() #Traer los puertos disponibles en el sistema

for port in ports:
    print(port)
    
#%%

# RX
    
import serial

PORT = "COM1"
#stopbit_one: un bit de parada
try:
    print(f"Estabeciendo conexion via {PORT}...")
    ser = serial.Serial(port = PORT,
                        baudrate=9600,
                        bytesize=8,
                        timeout=2,
                        stopbits=serial.STOPBITS_ONE) #timeout: Tiempo que va tomar el puerto cuando es uqe haya llegado el dato en reconocer
                                
    print("Conexion establecida")
    
    #Se escucha al COM para recibir los datos
    while True:
        try:
            #Ver si hay datos en buffer de entrada
            if ser.in_waiting > 0:
                #Se leen los datos y se espera el caracter en offline
                #readline: lee una trama y espera un back slash n (\n)
                data = ser.readline()
                #La data es binaria (en str). Se tiene qu decodificar
                string = data.decode('utf-8') #decode: cambia la codificacion de lo que haya llgado: Convertir esos bytes de string a string literales
                print(f"Rx: {string}")  
                
                
        except KeyboardInterrupt: #Al presionar Ctrl + C se cierra la conexion
            print("Conexión cerrada")
            ser.close()
            break
            
    
    
except:
    print(f"puerto {PORT} no disponible")

#%%

#Tx

import serial

try:
    print(f"Estabeciendo conexion via {PORT}...")
    ser = serial.Serial(port = PORT,
                        baudrate=9600,
                        bytesize=8,
                        timeout=2,
                        stopbits=serial.STOPBITS_ONE) #timeout: Tiempo que va tomar el puerto cuando es uqe haya llegado el dato en reconocer
                                
    print("Conexion establecida")
    
    #Pedir información
    
    while True:
        # Pedir el texto a enviar
        string = input("Tx: ")
        #Se define un código reservado para cancelar
        if string == "END":
            break
        else:
            #Se codifica el mensaje para su envio: en data binaria
            string = "Rx: " + string + "\n" #Se da la forma de mensaje
            data = string.encode('utf-8') #Decodificar
            ser.write(data) #Escribo sobre el puerto serial la data que se acaba de armar
            
    
    print("Conexión cerrada")
    ser.close()
    
except:
    print(f"puerto {PORT} no disponible")
    
#Escribir en el terminal de comando: ser.close() para cerrar la conexion porque no se cerró
#y volver a correr Tx





    
    
    
    
    
    