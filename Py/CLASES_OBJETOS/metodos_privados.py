# -*- coding: utf-8 -*-
"""
Created on Sun May  3 02:18:11 2020

@author: ASUS
"""

class Usuario:
    def __init__(self,username,clave,correo):
        self.username = username
        self.__clave = self.__Generar_clave(clave)
        self.correo = correo
        
    
    def __Generar_clave(self,clave):
        return clave.upper()
    def Estado(self):
        print(self.__clave)
    
ruben = Usuario("ruben","ruben123","racostaadmin@gmail.com")
print(ruben.username)
print(ruben.correo)
ruben.Estado()
#%%
class Empleado:
    def __init__(self):
        self.nombre = input("Ingrese un nombre: ")
        self.sueldo = int(input("Ingrese el sueldo: "))
    def Imprimir(self):
        print("Su nombres es: %s"%(self.nombre))
        print("su sueldo es %s"%(self.sueldo))
    def Impuestos(self):
        if self.sueldo > 3000:
            print("Tiene que pagar impuestos")
        else:
            print("No tiene que pagar impuestos")

empleado = Empleado()
empleado.Imprimir()
empleado.Impuestos()


































