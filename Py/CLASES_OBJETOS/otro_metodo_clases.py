# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

class Alumno:
    def Inicializar(self):
#        self.nombre = nombre
#        self.nota = nota
        self.nombre1 = input("Ingrese nombre 1: ")
        self.nota1 = int(input("Ingrese nota 1: "))
    
    def Imprimir(self):
        print("Nombre: ",self.nombre1)
        print("Nota: ",self.nota1)  

    def Mostrar_estado(self):
        if self.nota1>=4:
            print("Regular")

        else:
            print("Mal")       
alumno1 = Alumno()
alumno2 = Alumno()

alumno1.Inicializar()
alumno2.Inicializar()

alumno1.Imprimir()
alumno1.Mostrar_estado()

alumno2.Imprimir()
alumno2.Mostrar_estado()
#alumno2 = Alumno()
#
#alumno1.Inicializar()
#alumno1.Imprimir()
#alumno1.Mostrar_estado()
#
#alumno2.Inicializar()
#alumno2.Imprimir()
#alumno2.Mostrar_estado()

