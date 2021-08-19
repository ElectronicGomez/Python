import sqlite3
import tkinter as tk
import tkinter.ttk as ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from collections import deque

class Database:
    def __init__(self,datafile):
        self.conn = sqlite3.connect(datafile)
        self.cur = self.conn.cursor()
        
    def __del__(self):
        self.conn.close()
  
    #SE HALLAN LOS PAISES EN LAS REGION
    def paises_en_reg(self, region):
        sql = """SELECT nombre_pais
                    FROM regiones
                    JOIN paises
                    ON paises.id_region = regiones.id_region
                    WHERE nom_region = ?
                    """
        self.cur.execute(sql,(region,))
        return [items[0] for items in self.cur]
    
    #SE HALLAN EL PAIS Y SU POBLACION EN LA REGION
    def poblacion_paises(self,region):
        sql = """SELECT nombre_pais, poblacion
                    FROM regiones
                    JOIN paises
                    ON paises.id_region = regiones.id_region
                    WHERE nom_region = ?
                    ORDER BY poblacion DESC
                    """
        return self.cur.execute(sql, (region,)).fetchall()
    
    def area_paises(self,region):
        sql = """SELECT nombre_pais, area
                    FROM regiones
                    JOIN paises
                    ON paises.id_region = regiones.id_region
                    WHERE nom_region = ?
                    ORDER BY area DESC
                    """
        return self.cur.execute(sql, (region,)).fetchall()
    
    def densidad_paises(self,region):
        sql = """SELECT nombre_pais, den_pol
                    FROM regiones
                    JOIN paises
                    ON paises.id_region = regiones.id_region
                    WHERE nom_region = ?
                    ORDER BY den_pol DESC
                    """
        return self.cur.execute(sql, (region,)).fetchall()
    
    def linea_paises(self,region):
        sql = """SELECT nombre_pais, lin_cost
                    FROM regiones
                    JOIN paises
                    ON paises.id_region = regiones.id_region
                    WHERE nom_region = ?
                    ORDER BY lin_cost DESC
                    """
        return self.cur.execute(sql, (region,)).fetchall()
    


class App:
    def __init__(self,master):
        global seleccion
        seleccion = ""
        self.master = master
        self.master.resizable(0,0)
        self.master.title('ESTADISTICAS MUNDIALES')
        
        self.db = Database('database.db')
        
        #VARIABLES
        self.var_option = tk.IntVar()
        
        frame = tk.Frame(self.master)
        frame.pack(padx=10, pady=10)
        
        frame1 = tk.Frame(frame)
        frame2 = tk.Frame(frame)
        frame11 = tk.LabelFrame(frame1,text='REGIONES',padx=10,pady=10)
        frame12 = tk.LabelFrame(frame1,text='PAISES',padx=10,pady=10)
        frame21 = tk.Frame(frame2)
        frame22 = tk.LabelFrame(frame2,text='Estadisticas')
        
        frame1.pack(side=tk.LEFT,padx =10,pady=10)
        frame2.pack(side=tk.RIGHT,padx =10,pady=10)
        
        frame11.pack(side=tk.TOP,padx=10,pady=10)
        frame12.pack(side=tk.BOTTOM,padx=10,pady=10)
        
        frame21.pack(side=tk.TOP,padx=10,pady=10)
        frame22.pack(side=tk.BOTTOM,padx=10,pady=10)
        
        #CONFIGURACION FRAME
        frame21.config(bg='#F0F0F0')
        
        #-----------------------------FRAME 11 --------------------------------------------------------
        self.scrY1 = tk.Scrollbar(frame11,orient='vertical')
        self.lstRegiones = tk.Listbox(frame11,height=10,yscrollcommand=self.scrY1.set,
                                      highlightcolor="#0000ff",
                                      highlightbackground="#ff0000")

        self.scrY1.config(command=self.lstRegiones.yview)
        
        self.lstRegiones.pack(side=tk.LEFT)
        self.scrY1.pack(side=tk.LEFT, expand=True, fill=tk.Y)
        self.lstRegiones.bind("<<ListboxSelect>>", self.mostrar_paises)
        
        aux = [(0, 'SUB-SAHARAN AFRICA'), (1, 'LATIN AMER. & CARIB'), (2, 'ASIA (EX. NEAR EAST)'), 
               (3, 'NEAR EAST'), (4, 'OCEANIA'), (5, 'NORTHERN AMERICA'), (6, 'C.W. OF IND. STATES'), 
               (7, 'WESTERN EUROPE'), (8, 'NORTHERN AFRICA'), (9, 'EASTERN EUROPE'), (10, 'BALTICS')]
        
        regiones = [region[1] for region in aux]
        for region in regiones:
            self.lstRegiones.insert(tk.END,region)
        #-----------------------------FRAME 12---------------------------------------------------------
        self.scrY2 = tk.Scrollbar(frame12,orient='vertical')
        self.lstPaises = tk.Listbox(frame12,height=12,yscrollcommand=self.scrY2.set)
        self.scrY2.config(command=self.lstPaises.yview)
        self.lstPaises.bind("<<ListboxSelect>>", self.mostrar_paises)
        
        self.lstPaises.pack(side=tk.LEFT)
        self.scrY2.pack(side=tk.LEFT, expand=True, fill=tk.Y)
        #-----------------------------FRAME 21 ---------------------------------------------------------
        self.fig, self.ax = plt.subplots(figsize=(15,7))
        
        
        self.graph = FigureCanvasTkAgg(self.fig,master=frame21)
        self.graph.get_tk_widget().pack()
        #-----------------------------FRAME 22 ---------------------------------------------------------
        self.rdoOpcion1 = tk.Radiobutton(frame22,text='Poblacion',variable=self.var_option,value=1,
                                        command = self.graph_opcion1)
        self.rdoOpcion2 = tk.Radiobutton(frame22,text='Area',variable=self.var_option,value=2,
                                        command = self.graph_opcion2)
        self.rdoOpcion3 = tk.Radiobutton(frame22,text='Dens. Poblacional',variable=self.var_option,value=3,
                                        command = self.graph_opcion3)
        self.rdoOpcion4 = tk.Radiobutton(frame22,text='Linea Costera',variable=self.var_option,value=4,
                                        command = self.graph_opcion4)
        
        self.rdoOpcion1.grid(row=0,column=0,padx=5,pady=5)
        self.rdoOpcion2.grid(row=0,column=1,padx=5,pady=5)
        self.rdoOpcion3.grid(row=0,column=2,padx=5,pady=5)
        self.rdoOpcion4.grid(row=0,column=3,padx=5,pady=5)
        
        #--------------------- B L O Q U E ------- D E -------- F U N C I O N E S ------------------------
    def mostrar_paises(self, event):
        global seleccion
        
        self.lstPaises.delete(0,tk.END)
        seleccion = self.lstRegiones.get(self.lstRegiones.curselection())
        for pais in self.db.paises_en_reg(seleccion):
            self.lstPaises.insert(tk.END,pais)
        
        if self.var_option.get() == 1:
            self.graph_opcion1()
        elif self.var_option.get() == 2:
            self.graph_opcion2()
        elif self.var_option.get() == 3:
            self.graph_opcion3()
        elif self.var_option.get() == 4:
            self.graph_opcion4()
        else:
            pass
            
    def graph_opcion1(self):
        global seleccion
        try:
            poblacion = [valor[1] for valor in self.db.poblacion_paises(seleccion)]
            paises = [valor[0] for valor in self.db.poblacion_paises(seleccion)]
           
            self.ax.cla()
            self.ax.set_ylabel('POBLACION')
            self.ax.set_ylim(0,max(poblacion) + max(poblacion)/2)
            self.ax.xaxis.set_tick_params(rotation=90)
            
            for idx,valor in enumerate(poblacion):
                self.ax.text(idx,valor+ valor/10, f'{valor}',rotation=90)
            #Colocamos una etiqueta en el eje X
            self.ax.set_title(f'Poblacion en los paises de la region de {seleccion}')
            #Creamos la grafica de barras utilizando 'paises' como eje X y 'ventas' como eje y.
            self.ax.bar(paises, poblacion)
            self.ax.grid()
          
            self.graph.draw()
        except:
            pass
        
    def graph_opcion2(self):
        global seleccion
        try:
            area = [valor[1] for valor in self.db.area_paises(seleccion)]
            paises = [valor[0] for valor in self.db.area_paises(seleccion)]
           
            self.ax.cla()
            self.ax.set_ylabel('AREA (milla cuadrada)')
            self.ax.set_ylim(0,max(area)+max(area)/2)
            self.ax.xaxis.set_tick_params(rotation=90)
            
            for idx,valor in enumerate(area):
                self.ax.text(idx,valor+max(area)/10, f'{valor}',rotation=90)
            #Colocamos una etiqueta en el eje X
            self.ax.set_title(f'Area en los paises de la region de {seleccion}')
            #Creamos la grafica de barras utilizando 'paises' como eje X y 'ventas' como eje y.
            self.ax.plot(paises, area)
            self.ax.grid()
          
            self.graph.draw()
        except:
            pass
    def graph_opcion3(self):
        global seleccion
        try:
            dens = []
            densidad = [valor[1] for valor in self.db.densidad_paises(seleccion)]
            paises = [valor[0] for valor in self.db.densidad_paises(seleccion)]
            
            #Se convierten a flotantes
            for dato in densidad:
                dato = float(dato.replace(',','.'))
                dens.append(dato)
            
            self.ax.cla()
            self.ax.set_ylabel('DENSIDAD POBLACIONAL(persona por mill. cuadrada)')
            self.ax.set_ylim(0,max(dens)+max(dens)/2)
            self.ax.xaxis.set_tick_params(rotation=90)
            
            for idx,valor in enumerate(dens):
                self.ax.text(idx,valor+max(dens)/10, f'{valor}',rotation=90)
            #Colocamos una etiqueta en el eje X
            self.ax.set_title(f'Densidad poblacional en los paises de la region de {seleccion}')
            #Creamos la grafica de barras utilizando 'paises' como eje X y 'ventas' como eje y.
            self.ax.stem(paises, dens)
            self.ax.grid()
              
            self.graph.draw()
        except:
            pass
    def graph_opcion4(self):
        global seleccion
        try:
            lin = []
            lin_cost = [valor[1] for valor in self.db.linea_paises(seleccion)]
            paises = [valor[0] for valor in self.db.linea_paises(seleccion)]
            
            for dato in lin_cost:
                dato = float(dato.replace(',','.'))
                lin.append(dato)
            
            self.ax.cla()
            self.ax.set_ylabel('LINEA COSTERA (coast/ area ratio)')
            self.ax.set_ylim(0,max(lin)+max(lin)/2)
            self.ax.xaxis.set_tick_params(rotation=90)
              
            for idx,valor in enumerate(lin):
                self.ax.text(idx,valor+max(lin)/10, f'{valor}',rotation=90)
            #Colocamos una etiqueta en el eje X
            self.ax.set_title(f'Linea costera en los paises de la region de {seleccion}')
            #Creamos la grafica de barras utilizando 'paises' como eje X y 'ventas' como eje y.
            self.ax.plot(paises, lin,marker='x',linestyle='--',color='r')
            self.ax.grid()
              
            self.graph.draw()
        except:
            pass
        
root= tk.Tk()
app = App(root)
root.mainloop()
