# -*- coding: utf-8 -*-
"""
Created on Sat May  2 21:46:03 2020

@author: ASUS
"""

class Triangulo:
    def Inicializar(self):
        self.lado1 = int(input("Ingrese el lado 1: "))
        self.lado2 = int(input("Ingrese el lado 2: "))
        self.lado3 = int(input("Ingrese el lado 3: "))
    def Imprimir(self):
        print("Valores de los lados del triangulo:")
        print("lado 1: ",self.lado1)
        print("lado 2: ",self.lado2)
        print("lado 3: ",self.lado3)
    def Lado_mayor(self):
        print("el lado mayor es: ",end='')
        if self.lado1 > self.lado2 and self.lado1 > self.lado3:
            print(self.lado1)
        else:
            if self.lado2 > self.lado3:
                print(self.lado2)
            else:
                print(self.lado3)
    def Equilatero(self):
        if self.lado1 == self.lado2 and self.lado1 == self.lado3:
            print("El triangulo es equiñatero")
        else:
            print("El triangulo no es equilatero")
triangulo = Triangulo()
triangulo.Inicializar()
triangulo.Imprimir()
triangulo.Lado_mayor()
triangulo.Equilatero()
        
        