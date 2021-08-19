# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 16:51:11 2020

@author: ASUS
"""


#%%
from tkinter import *
import tkinter.ttk as ttk
import time
import csv
import sqlite3

regiones1=[];liston = [];paises1=[];area1=[];densidad1=[];costa1=[];
migracion1=[];mortalidad1=[];gdp1=[];alfa1=[];poblacion1=[];reg=[];
with open("data.csv", encoding='utf-8') as file:
    reader = csv.reader(file)
    liston = []
    for line in reader:
        liston.append(line)
    aux = liston[0]
    indices = aux[1:10]
    datos = liston[1::]
    #print(indices)
    
    
conn = sqlite3.connect("database.db")

with conn:
    cur = conn.cursor()
    cur.execute("DROP TABLE Regiones")
    cur.execute("""CREATE TABLE IF NOT EXISTS Regiones (
                        nombre_region)
                """)
    cur.execute("DROP TABLE Paises")
    cur.execute("""CREATE TABLE IF NOT EXISTS Paises (
                        nombre_pais TEXT, 
                        nombre_region TEXT,
                        area REAL,
                        pop_density REAL,
                        coastline REAL,
                        net_migration REAL,
                        infant_mortality REAL,
                        gdp REAL ,
                        literacy REAL
                        )
                """)

    for i in range(len(liston)):
            regiones1.append(liston[i][1])
    regiones1 = list(dict.fromkeys(regiones1)); regiones= regiones1[1::]
    
    for i in range(len(liston)):
            paises1.append(liston[i][0])
            poblacion1.append(liston[i][2])
            area1.append(liston[i][3])
            densidad1.append(liston[i][4])
            costa1.append(liston[i][5])
            migracion1.append(liston[i][6])
            mortalidad1.append(liston[i][7])
            gdp1.append(liston[i][8])
            alfa1.append(liston[i][9])
            reg.append(liston[i][1])
            
    paises1 = list(dict.fromkeys(paises1)); paises= paises1[1::]
    poblacion = poblacion1[1::]
    area = area1[1::]
    densidad = densidad1[1::]
    costa = costa1[1::]
    migracion = migracion1[1::]
    mortalidad = mortalidad1[1::]
    gdp = gdp1[1::]
    alfa = alfa1[1::]
    reg=reg[1::]
    conjunto = [paises,reg,area,densidad,costa,migracion,mortalidad,gdp,alfa]
    conjunto2=[];
    for i in range(len(paises)):
        linea=[]
        for j in range(len(conjunto)):
            linea.append(conjunto[j][i])
        conjunto2.append(linea)
    
    for region in regiones:
        cur.execute("""INSERT INTO Regiones (nombre_region)
                    VALUES (?)""", (region,))     
    cur.executemany("""INSERT INTO Paises (nombre_pais,nombre_region,area,pop_density,coastline,net_migration,infant_mortality,gdp,literacy)
                        VALUES (?,?,?,?,?,?,?,?,?)""", conjunto2)

conn.commit()
conn.close()


