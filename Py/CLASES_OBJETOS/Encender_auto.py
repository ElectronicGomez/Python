# -*- coding: utf-8 -*-
"""
Created on Sat May  2 22:22:40 2020

@author: ASUS
"""

class Auto:
    def __init__(self):
        self.largoChasis = 250
        self.anchoChasis = 120
        self.ruedas = 4
        self.enmarcha = False
        
    def Arrancar(self,arrancamos):
        self.enmarcha = arrancamos #dato tipo bool
        
        if self.enmarcha == True:
            return "el auto está en marcha"
        else:
            return "El auto está parado"
        
    def Estado(self):
        print("El auto tiene ",self.ruedas)
        
miauto = Auto()
print(miauto.Arrancar(False))