# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

class Alumno:
    def Inicializar(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota
    def Imprimir(self):
        print("Nombre: ",self.nombre)
        print("Nota: ",self.nota)  
    def Mostrar_estado(self):
        if self.nota>=4:
            print("Regular")
        else:
            print("Mal")       
alumno1 = Alumno()
alumno2 = Alumno()
nombre1 = input("Ingrese nombre 1: ")
edad1 = int(input("Ingrese nota 1: "))
nombre2 = input("Ingrese nombre 2: ")
edad2 = int(input("Ingrese nota 2: "))

alumno1.Inicializar(nombre1,edad1)
alumno1.Imprimir()
alumno1.Mostrar_estado()

alumno2.Inicializar(nombre2,edad2)
alumno2.Imprimir()
alumno2.Mostrar_estado()

