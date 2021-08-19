# -*- coding: utf-8 -*-
"""
Created on Sun May  3 02:52:35 2020

@author: ASUS
"""

class Punto:
#    def __init__(self,x,y):
#        self.x = x
#        self.y = y
    def __init__(self):
        self.x = int(input("Ingrese la abcisa x: "))
        self.y = int(input("Ingrese la ordenada y: "))
    def Imprimir(self):
        print("\nCoordenadas del punto: ",end='')
        print("(%s , %s)"%(self.x,self.y))
    def Cuadrante(self):
        if self.x > 0 and self.y > 0:
            print("Primer cuadrante")
        elif self.x < 0 and self.y >0:
            print("Segundo cuadrante")
        elif self.x < 0 and self.y < 0:
            print("Tercer cuadrante")
        else:
            print("Cuarto cuadrante")
#punto = Punto(-20,-2)
punto = Punto()
punto.Imprimir()
punto.Cuadrante()
        