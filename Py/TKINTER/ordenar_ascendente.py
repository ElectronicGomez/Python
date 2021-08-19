# -*- coding: utf-8 -*-
"""
Created on Fri May 15 20:19:33 2020

@author: ASUS
"""

#----ORDENAR FORMA ASCENDENTE----

while(1):
  try:
    num1 = int(input("Ingrese un numero entero1: "))
    num2 = int(input("Ingrese un numero entero2: "))
    num3 = int(input("Ingrese un numero entero3: "))
    num4 = int(input("Ingrese un numero entero4: "))
    num5 = int(input("Ingrese un numero entero5: "))
    num6 = int(input("Ingrese un numero entero6: "))
    num7 = int(input("Ingrese un numero entero7: "))
    num8 = int(input("Ingrese un numero entero8: "))
    
    break
  except ValueError:
      print("Parametro ingresado incorrecto")
  except SyntaxError:
      print("Parametro ingresado incorrecto")
  except NameError:
      print("Parametro ingresado incorrecto")
  except IndexError:
      print("Parametro ingresado incorrecto")

lista=[num1,num2,num3,num4,num5,num6,num7,num8]
print(lista)
cont=0
a=0
while(a<len(lista)-1):
  for i in range(len(lista)-1):
    if lista[i]>lista[i+1]:
      var=lista[i]
      lista[i]=lista[i+1]
      lista[i+1]=var
  a+=1
print(lista,"\nMenor a Mayor:")
for i in range(len(lista)):
  print(lista[i],end=", ")
  cont+=1
print()