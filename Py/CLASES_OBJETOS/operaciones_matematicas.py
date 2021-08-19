# -*- coding: utf-8 -*-
"""
Created on Sun May  3 03:20:27 2020

@author: ASUS
"""

class Operaciones:
    def __init__(self):
        self.num1 = int(input("Ingrese el primer valor: "))
        self.num2 = int(input("Ingrese el segundo valor: "))
    def Suma(self):
        suma = self.num1 + self.num2
        print("La suma es: %s"%(suma))
    def Resta(self):
        resta = self.num1 - self.num2
        print("La resta es: %s"%(resta))
    def Multiplicacion(self):
        mul = self.num1 * self.num2
        print("La multiplicacion es: ",mul)
    def Division(self):
        div = self.num1 / self.num2
        print("La division es: ",div)

operacion = Operaciones()
operacion.Suma()
operacion.Resta()
operacion.Multiplicacion()
operacion.Division()
















