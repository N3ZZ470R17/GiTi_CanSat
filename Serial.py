import serial as S
import time
import numpy as np

#Serial_10 = S.Serial('/dev/ttyAMA0', baudrate=9600, timeout=1) #Pin de enviar

#Serial_8 = S.Serial('/dev/ttyUSB1', baudrate=9600, timeout=1) #Pin de recibir
contador=0
for i in range(0,3):
   try:
      numpuerto= '/dev/ttyUSB'+str(i)
      Serial_8 = S.Serial(numpuerto, baudrate=9600, timeout=1)
   except:
      print("Error conectando")
   else:
      print("Hubo conexión correcta, Puerto: "+str(i))
def lectura():
   global texto
   texto = ""
   Cod = 'utf-8'
   lectura = Serial_8.readline() #Se realiza lectura en Binario por serial.
   #lectura = "V"+str(np.random.rand()*100)+"V"+str(np.random.rand()*100)+"V"+str(np.random.rand()*100)+"V"
   while lectura==b'':
      lectura = Serial_8.readline()
      
   '''if lectura!=b'': #Se discriminan las lecturas sin contenido alguno
      texto = str(lectura, Cod) #Se codifica  para su lectura como String. 
      return texto
   else:
      return "nada"
   '''
   try:
      print(lectura)
      texto=str(lectura, Cod)
      #texto=lectura#str(lectura, Cod)#Se puede omitir para la prueba
      print(texto)
      #raise UnicodeDecodeError("Error decodificación")
   except:
      print("Con error de codificación")
      print(lectura)
      time.sleep(2)
   else:
      print("Sin error de codificación")
   return texto
'''
while True:
    try:
        v=lectura()
    except TypeError:
        print("Error de Byte")
        v="Nada"
    else:
        temporal=v.split('V')
        ax2=temporal[1]
        ay2=temporal[2]
        az2=temporal[3]
        at2=temporal[4]
        p2=temporal[5]
        t2=temporal[6]
        h2=temporal[7]
        a2=temporal[8]
    print("AX:",ax2, "AY: ",ay2,"AZ: ",az2,"AT: ",at2,"P:",p2,"T:",t2,"H:",h2,"A:",a2)
    time.sleep(1)

def adjuntar():
  global t,h,h2
  t,h,h2 = datos()
  try:
    c=0
    listaT.append(float(t))
    c=1
    listaH.append(float(h))
    c=2
    listaH2.append(float(h2))
  except ValueError:
    if c==0:
      adjuntar()
    elif c==1:
      listaT.pop(0)
      adjuntar()
    else:
      listaT.pop(0)
      listaH.pop(0)
      adjuntar()
  else:
      print("Todo Bien")

'''
