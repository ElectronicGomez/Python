def conv_dec_bin(num):
  lista = [0]*8
  cont=7
  while(num>=2):
    a=num%2
    num=num//2
    lista[cont]=a
    cont-=1
  lista[cont]=num
  return lista
a=True

def complemento_2(num):
       num &= (2 << 8-1)-1 # mask
       formatStr = '{:0'+str(8)+'b}'
       ret =  formatStr.format(int(num))
       return ret
   
while (a):
  try:
    num = int(input("Ingrese un numero entre -127 y 127: "))
    if ((num>=-127) and (num<128)):
      a=False
    else:
      print("Numero incorrecto, ingrese de nuevo")
  except:
    print("Numero incorrecto, ingrese de nuevo")
if (num>0):
    a = conv_dec_bin(num)
    cont1 = 0
    for i in range(len(a)):
        if (a[i] == 1):
            cont1 = cont1 + 1
    print("El numero binario es: %s"%( conv_dec_bin(num) ))
    print("La cantidad de unos que tiene el numero binario es: %s"%(cont1))
    
elif (num < 0):
    b = complemento_2(num)
    cont2 = 0
    for i in range(len(b)):
        if (b[i] == "1"):
            cont2 = cont2 + 1
    print("El numero binario es: %s"%( complemento_2(num) ))
    print("La cantidad de unos que tiene el numero binario es: %s"%(cont2))



