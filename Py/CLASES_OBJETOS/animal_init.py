# -*- coding: utf-8 -*-
"""
Created on Sat May  2 22:39:43 2020

@author: ASUS
"""

class Animal:
    def __init__(self, nombre): #pasando parametros al constructor
        self.nombre = nombre
        self.patas = 4
        self.tipo = "Can"
        
x = Animal("Tobias")
y = Animal("Tony")

print(x.nombre, x.patas, x.tipo)
print(y.nombre, y.patas, y.tipo)

#%%

class Animal:
    def __init__(self,nombre=None, patas = 4):
        self.nombre = nombre
        self.patas = patas
        self.tipo = 'Can'
        
x = Animal("Tobias",2)
y = Animal("Tony")
print(x.nombre, x.patas, x.tipo)
print(y.nombre,y.patas,y.tipo)

