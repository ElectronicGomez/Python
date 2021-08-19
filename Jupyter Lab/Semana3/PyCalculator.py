import tkinter as tk
import tkinter.ttk as ttk

class Calculadora:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculadora")
        self.master.geometry("330x290+100+100")
        self.master.resizable(0, 0)
        # self.master.iconbitmap('icon_calc.ico')
        self.master.config(bg='#0A122A')

        # Status de ingreso del primer numero previo a la operacion
        self.first_num = None
        # Status del resultado (presionar tecla "=")
        self.result = False
        
        self.var_num = tk.StringVar()
        self.var_op = None
        self.var_num.set('0')
        
        frm = tk.Frame(self.master, bg='#0A122A')
        frm.pack(padx=10, pady=10)
        
        #bd=3 para que el entry se vea un borde hundido
        # Widgets en la calculadora
        self.entDisplay = tk.Entry(frm, width=15, font='"Digital-7 Mono" 20', justify='right',
                                   fg='#808080', bg='#ECF6CE', textvariable=self.var_num, bd=3) 
        self.btn0 = tk.Button(frm, text='0', width=4, font='Arial 16', 
                              command=lambda:self.add_num_display('0'), bg='#A9A9F5')
        self.btn1 = tk.Button(frm, text='1', width=4, font='Arial 16', 
                              command=lambda:self.add_num_display('1'), bg='#A9A9F5')
        self.btn2 = tk.Button(frm, text='2', width=4, font='Arial 16', 
                              command=lambda:self.add_num_display('2'), bg='#A9A9F5')
        self.btn3 = tk.Button(frm, text='3', width=4, font='Arial 16', 
                              command=lambda:self.add_num_display('3'), bg='#A9A9F5')
        self.btn4 = tk.Button(frm, text='4', width=4, font='Arial 16', 
                              command=lambda:self.add_num_display('4'), bg='#A9A9F5')
        self.btn5 = tk.Button(frm, text='5', width=4, font='Arial 16', 
                              command=lambda:self.add_num_display('5'), bg='#A9A9F5')
        self.btn6 = tk.Button(frm, text='6', width=4, font='Arial 16', 
                              command=lambda:self.add_num_display('6'), bg='#A9A9F5')
        self.btn7 = tk.Button(frm, text='7', width=4, font='Arial 16', 
                              command=lambda:self.add_num_display('7'), bg='#A9A9F5')
        self.btn8 = tk.Button(frm, text='8', width=4, font='Arial 16', 
                              command=lambda:self.add_num_display('8'), bg='#A9A9F5')
        self.btn9 = tk.Button(frm, text='9', width=4, font='Arial 16', 
                              command=lambda:self.add_num_display('9'), bg='#A9A9F5')
        self.btnPoint = tk.Button(frm, text='.', width=4, font='Arial 16', 
                                  command=lambda:self.add_num_display('.'), bg='#A9A9F5')
        self.btnEqual = tk.Button(frm, text='=', width=4, font='Arial 16', 
                                  command=self.solve, bg='#868A08')
        self.btnAdd = tk.Button(frm, text='+', width=4, font='Arial 16', 
                                command=lambda:self.set_op('+'), bg='#5858FA')
        self.btnSub = tk.Button(frm, text='-', width=4, font='Arial 16', 
                                command=lambda:self.set_op('-'), bg='#5858FA')
        self.btnMul = tk.Button(frm, text='x', width=4, font='Arial 16', 
                                command=lambda:self.set_op('x'), bg='#5858FA')
        self.btnDiv = tk.Button(frm, text='/', width=4, font='Arial 16', 
                                command=lambda:self.set_op('/'), bg='#5858FA')
        self.btnDel = tk.Button(frm, text='DEL', width=4, font='Arial 16',
                                command=self.clear_scr, bg='#FE2E64')
        
        self.btnDel.grid(row=0, column=0, padx=5, pady=5)
        self.entDisplay.grid(row=0, column=1, columnspan=3, padx=5, pady=5)
        
        self.btn7.grid(row=1, column=0, padx=5, pady=5)
        self.btn8.grid(row=1, column=1, padx=5, pady=5)
        self.btn9.grid(row=1, column=2, padx=5, pady=5)
        self.btnAdd.grid(row=1, column=3, padx=5, pady=5)

        self.btn4.grid(row=2, column=0, padx=5, pady=5)
        self.btn5.grid(row=2, column=1, padx=5, pady=5)
        self.btn6.grid(row=2, column=2, padx=5, pady=5)
        self.btnSub.grid(row=2, column=3, padx=5, pady=5)

        self.btn1.grid(row=3, column=0, padx=5, pady=5)
        self.btn2.grid(row=3, column=1, padx=5, pady=5)
        self.btn3.grid(row=3, column=2, padx=5, pady=5)
        self.btnDiv.grid(row=3, column=3, padx=5, pady=5)
        
        self.btn0.grid(row=4, column=0, padx=5, pady=5)
        self.btnPoint.grid(row=4, column=1, padx=5, pady=5)
        self.btnEqual.grid(row=4, column=2, padx=5, pady=5)
        self.btnMul.grid(row=4, column=3, padx=5, pady=5)
        
 
    def clear_scr(self):
        self.var_num.set('0')
        
        
    def add_num_display(self, num):
        # Si hay un resultado previo...
        if self.var_op == None and self.result:
            # ...se limpia la pantalla
            self.clear_scr()
            self.result = False
        
        # Si en la pantalla hay un cero...
        if self.var_num.get() == '0':
            # ...y si ingresa cero...
            if num == '0':
                # ... no se muestra nada
                return
            # ...de lo contrario puede ser que se ingrese un punto
            elif num == '.':
                # ...y si no hay puntos en la pantalla se coloca "0."
                if self.var_num.get().find('.') < 0:
                    self.var_num.set('0.')
            # ...sino se coloca en numero ingresado
            else:
                self.var_num.set(num)
        # Si no hay un cero en la pantalla...
        else:
            # ... y si se ingresa un punto...
            if num == '.':
                # ...si es que ya hay un punto no se muestra nada
                 if self.var_num.get().find('.') >= 0:
                    return
              
            # ...de lo contrario se ingresa el numero o el punto
            self.var_num.set(self.var_num.get() + num)
        
        
    def set_op(self, op):
        # La operacion se registra si se esta ingresado el primer valor
        if self.first_num == None:
            # Se registra la operacion
            self.var_op = op
            # Se guarda el numero inicial
            self.first_num = self.var_num.get()
            # Se coloca '0' en la pantalla
            self.var_num.set('0')

        
    def solve(self):
        # La operacion se resuelve si se ha ingresado el segundo valor
        if self.first_num != None:
            if self.var_op == '+':
                result = float(self.first_num) + float(self.var_num.get())
            elif self.var_op == '-':
                result = float(self.first_num) - float(self.var_num.get())
            elif self.var_op  == 'x':
                result = float(self.first_num) * float(self.var_num.get())
            elif self.var_op == '/':
                result = float(self.first_num) / float(self.var_num.get())
            
            self.var_num.set(result)
            
            # Las variables de control se colocan a sus valores iniciales
            self.var_op = None
            self.first_num = None
            self.result = True
            
  
        
        
root = tk.Tk()
app = Calculadora(root)
root.mainloop()