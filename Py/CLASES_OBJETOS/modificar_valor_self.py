# -*- coding: utf-8 -*-
"""
Created on Sun May  3 01:21:41 2020

@author: ASUS
"""
class Auto:
    def __init__(self):
        self.largoChasis = 250
        self.anchoChasis = 120
        self.ruedas = 4
        self.enmarcha = False
        
    def Arrancar(self,arrancamos):
        self.enmarcha = arrancamos
        if self.enmarcha == True:
            return "El auto está en marcha"
        else:
            return "El auto esta parado"
    def Estado(self):
        print("El carro tiene %s"%(self.ruedas),"ruedas")
#        print("El carro tiene {} ruedas".format(self.ruedas))
        
miauto = Auto()
miauto.ruedas = 2
miauto.Estado()

#%%
class Auto:
    def __init__(self):
        self.largoChasis = 250
        self.anchoChasis = 120
        self.__ruedas = 4 #Atributo privado
        self.enmarcha = False
    def Arrancar(self,arrancamos):
        self.enmarcha = arrancamos
        if self.enmarcha == True:
            return "El carro está en marcha"
        else:
            return "El carro esta en marcha"
    def Estado(self):
        print("el auto tiene %s "%(self.__ruedas),"ruedas")

miauto = Auto()
miauto.ruedas = 2
miauto.Estado()

        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    




