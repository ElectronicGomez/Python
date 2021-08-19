# -*- coding: utf-8 -*-
"""
Created on Sun May  3 03:09:56 2020

@author: ASUS
"""

class Cuadrado:
    def __init__(self):
        self.lado = int(input("Ingrese el lado del cuadrado: "))
    def Perimetro(self):
        self.perimetro = self.lado*4
    def Superficie(self): #Area
        self.superficie = self.lado**2
    def Imprimir(self):
        print("El perimetro del cuadrado es: %s"%(self.perimetro))
        print("La superficie del cuadrado es: %s"%(self.superficie), "m2")
cuadrado = Cuadrado()
cuadrado.Perimetro()
cuadrado.Superficie()
cuadrado.Imprimir()