from tkinter import *
import time
import Serial as P
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np

c=0
lat="74N"
long="6E"
listaAx= [0,0,0,0,0,0,0,0,0,0]
listaAy= [0,0,0,0,0,0,0,0,0,0]
listaAz= [0,0,0,0,0,0,0,0,0,0]
listaAt= [0,0,0,0,0,0,0,0,0,0]

listaP= [0,0,0,0,0,0,0,0,0,0]
listaT= [0,0,0,0,0,0,0,0,0,0]
listaH= [0,0,0,0,0,0,0,0,0,0]
listaA= [0,0,0,0,0,0,0,0,0,0]

#Ventana principal
def ventanaPrincipal():
    root = Tk()
    root.geometry("500x300")
    root.resizable(0, 0)
    root.title("Estación en tierra GITI2305")
    root.etiqueta = Label(root, text="")
    root.etiqueta.pack()
    root.etiqueta = Label(root, text="Bienvenido a nuestra plataforma de monitoreo")
    root.etiqueta.pack()
    root.etiqueta = Label(root, text="¿Qué datos desea revisar?")
    root.etiqueta.pack()
    root.etiqueta = Label(root, text="")#SALTO DE LINEA 2
    root.etiqueta.pack()
    root.botonAcelerometro= Button(root, text="Aceleraciones",  bg="yellow", font= ("Times New Roman", 12), fg="black", command=ventanaAcel)
    root.botonAcelerometro.pack()
    root.botonAcelerometro= Button(root, text="Presión",  bg="yellow", font= ("Times New Roman", 12), fg="black", command=ventanaPres)
    root.botonAcelerometro.pack()
    root.botonPresion = Button(root, text="Humedad",  bg="darkblue", font= ("Times New Roman", 12), fg="white", command=ventanaHum)
    root.botonPresion.pack()
    root.botonAltitud = Button(root, text="Temperatura",  bg="red", font= ("Times New Roman", 12), fg="white", command=ventanaTemp)
    root.botonAltitud.pack()
    root.etiqueta = Label(root, text="")#SALTO DE LINEA 3
    root.etiqueta.pack()        
    root.etiqueta = Label(root, text="Fundación de Educación Superior San José")
    root.etiqueta.pack()        
    root.etiqueta = Label(root, text="Semillero GITI")
    root.etiqueta.pack() 
    root.etiqueta = Label(root, text="Categoría Cóndores")
    root.etiqueta.pack() 

#Definimos las ventanas de aceleraciones
def ventanaAcel():
  global ventana1
  ventana1 = Tk()
  ventana1.title("Observación de aceleraciones")
  ventana1.geometry("300x170")
  ventana1.etiqueta = Label(ventana1, text="")#SALTO DE LINEA 3
  ventana1.etiqueta.pack() 
  ventana1.botonAx= Button(ventana1, text="Aceleración en x",  bg="yellow", font= ("Times New Roman", 12), fg="black", command=ventanaAx)
  ventana1.botonAx.pack()
  ventana1.botonAy= Button(ventana1, text="Aceleración en y",  bg="yellow", font= ("Times New Roman", 12), fg="black", command=ventanaAy)
  ventana1.botonAy.pack()
  ventana1.botonAz = Button(ventana1, text="Aceleración en z",  bg="darkblue", font= ("Times New Roman", 12), fg="white", command=ventanaAz)
  ventana1.botonAz.pack()
  ventana1.botonAt = Button(ventana1, text="Aceleración Total",  bg="red", font= ("Times New Roman", 12), fg="white", command=ventanaAt)
  ventana1.botonAt.pack()
  ventana1.etiqueta = Label(ventana1, text="")#SALTO DE LINEA 3
  ventana1.etiqueta.pack()
  
def ventanaAx():
  global v1,label1,tempx,guail,latx,longx,altx
  tempx = 5
  guail = 1
  v1 = Tk()
  v1.title("Aceleración en x")
  v1.geometry("330x420")
  label1 = crearBoton(v1,"Aceleracion en X","yellow")
  label1.grid(row=0,column=0)
  latx = crearBoton(v1,"Latitud","yellow")
  latx.grid(row=2,column=0)  
  longx = crearBoton(v1,"Longitud","blue")
  longx.grid(row=3,column=0)    
  altx = crearBoton(v1,"Altura","red")
  altx.grid(row=4,column=0)    
    #ciclo(tempx)
  v1.after(1000,ciclo(5))
  
  #ubicar(label1,0,0)
  
def ventanaAy(): 
  global v2,label2,tempay,laty,longy,alty
  tempay = 6
  v2=Tk()
  v2.title("Aceleración en y")
  v2.geometry("330x420")
  label2 = crearBoton(v2,"Aceleracion en Y","white")
  label2.grid(row=0,column=0)
  laty = crearBoton(v2,"Latitud","yellow")
  laty.grid(row=2,column=0)  
  longy = crearBoton(v2,"Longitud","blue")
  longy.grid(row=3,column=0)    
  alty = crearBoton(v2,"Altura","red")
  alty.grid(row=4,column=0)    
  
  
  ciclo(tempay)
  #ubicar(label2,0,1)

def ventanaAz():
  global v3,label3, tempaz, latz, longz, altz
  tempaz = 7
  v3=Tk()
  v3.title("Aceleración en z")
  v3.geometry("330x420")
  label3 = crearBoton(v3,"Aceleracion en Z","green")
  label3.grid(row=0,column=0)
  latz = crearBoton(v3,"Latitud","yellow")
  latz.grid(row=2,column=0)  
  longz = crearBoton(v3,"Longitud","blue")
  longz.grid(row=3,column=0)    
  altz = crearBoton(v3,"Altura","red")
  altz.grid(row=4,column=0)  
  
  ciclo(tempaz)

def ventanaAt():
  global v4,label4, tempat, latt, longt, altt
  tempat = 8
  v4=Tk()
  v4.title("Aceleración Total")
  v4.geometry("330x420")
  label4 = crearBoton(v4,"Aceleracion Total","yellow")
  label4.grid(row=0,column=0)
  latt = crearBoton(v4,"Latitud","yellow")
  latt.grid(row=2,column=0)  
  longt = crearBoton(v4,"Longitud","blue")
  longt.grid(row=3,column=0)    
  altt = crearBoton(v4,"Altura","red")
  altt.grid(row=4,column=0)  
  
  ciclo(tempat)
  #ubicar(label2,0,1)
  #ventana.mainloop()

#Aquí termina las ventanas de aceleraciones
#---------------------------------------------------
  
#Definimos la ventana de presión y altura
def ventanaPres():
  global ventana2,label5, label6, label7,label8,temp2
  temp2= 2
  ventana2 = Tk()
  ventana2.title("Observación de Presión")
  ventana2.geometry("330x420")
  label5 = crearBoton(ventana2,"Presión","red")
  label5.grid(row=0,column=0)
  
  #ubicar(label1,0,0)
  label6 = crearBoton(ventana2,"Latitud","white")
  label6.grid(row=2,column=0)
  #ubicar(label2,0,1)
  label7 = crearBoton(ventana2,"Longitud","green")
  label7.grid(row=3,column=0)
  
  label8 = crearBoton(ventana2,"Altitud","yellow")
  label8.grid(row=4,column=0)
  ciclo(temp2)
  #ubicar(label1,0,0)
  #ventana.mainloop()

#Definimos ventana de temperatura y humedad
def ventanaHum():
  global ventana3,label9, label10, label11,label12,temp3
  temp3=3
  
  ventana3 = Tk()
  ventana3.title("Observación de Humedad relativa")
  ventana3.geometry("330x420")

  label9 = crearBoton(ventana3,"Humedad:","red")
  label9.grid(row=0,column=0)
  
  #ubicar(label1,0,0)
  label10 = crearBoton(ventana3,"Latitud","white")
  label10.grid(row=2,column=0)
  #ubicar(label2,0,1)
  label11 = crearBoton(ventana3,"Longitud","green")
  label11.grid(row=3,column=0)
  
  label12 = crearBoton(ventana3,"Altitud","yellow")
  label12.grid(row=4,column=0)
  ciclo(temp3)
  #ubicar(label2,0,1)
  #ventana.mainloop()

#Definimos ventana de temperatura y humedad
def ventanaTemp():
  global ventana4, label13,label14,label15,label16, temp4
  temp4 = 4
  ventana4 = Tk()
  ventana4.title("Principal")
  ventana4.geometry("330x420")

  label13 = crearBoton(ventana4,"Temperatura","red")
  label13.grid(row=0,column=0)
  #ubicar(label1,0,0)
  label14 = crearBoton(ventana4,"Latitud","white")
  label14.grid(row=2,column=0)
  #ubicar(label2,0,1)
  label15 = crearBoton(ventana4,"Longitud","green")
  label15.grid(row=3,column=0)
  
  label16 = crearBoton(ventana4,"Altitud","yellow")
  label16.grid(row=4,column=0)
  ciclo(temp4)
  #ubicar(label2,0,1)
  #ventana.mainloop()
  
  
#Definimos el canvas para la gráfica
def canvas(color1,color2,color3,color4,comp):
    
    if comp==5:
      fig1 =  Figure(figsize=(3,3), dpi=100)
      t=[1,2,3,4,5,6,7,8,9,10]
      fig1.add_subplot(111).plot(t,listaAx,color1)
      canvas1=FigureCanvasTkAgg(fig1,master=v1)
      canvas1.draw()
      canvas1.get_tk_widget().grid(row=1,column=0)
      v1.update()
  
    if comp==6:
      fig1 =  Figure(figsize=(3,3), dpi=100)
      t=[1,2,3,4,5,6,7,8,9,10]
      fig1.add_subplot(111).plot(t,listaAy,color1)
      canvas1=FigureCanvasTkAgg(fig1,master=v2)
      canvas1.draw()
      canvas1.get_tk_widget().grid(row=1,column=0)     
      v2.update()   
    if comp==7:
      fig1 =  Figure(figsize=(3,3), dpi=100)
      t=[1,2,3,4,5,6,7,8,9,10]
      fig1.add_subplot(111).plot(t,listaAz,color1)
      canvas1=FigureCanvasTkAgg(fig1,master=v3)
      canvas1.draw()
      canvas1.get_tk_widget().grid(row=1,column=0)     
      v3.update()           
    if comp==8:
      fig1 =  Figure(figsize=(3,3), dpi=100)
      t=[1,2,3,4,5,6,7,8,9,10]
      fig1.add_subplot(111).plot(t,listaAx,color1)
      canvas1=FigureCanvasTkAgg(fig1,master=v4)
      canvas1.draw()
      canvas1.get_tk_widget().grid(row=1,column=0)     
      v4.update()  
        
  
    elif comp==3:
      fig1 =  Figure(figsize=(3,3), dpi=100)
      t=[1,2,3,4,5,6,7,8,9,10]
      fig1.add_subplot(111).plot(t,listaH,color1)
      canvas1=FigureCanvasTkAgg(fig1,master=ventana3)
      canvas1.draw()
      canvas1.get_tk_widget().grid(row=1,column=0)
      ventana3.update()
    elif comp==2:
      fig1 =  Figure(figsize=(3,3), dpi=100)
      t=[1,2,3,4,5,6,7,8,9,10]
      fig1.add_subplot(111).plot(t,listaP,color1)
      canvas1=FigureCanvasTkAgg(fig1,master=ventana2)
      canvas1.draw()
      canvas1.get_tk_widget().grid(row=1,column=0)
      ventana2.update()
    elif comp==4:
      fig1 =  Figure(figsize=(3,3), dpi=100)
      t=[1,2,3,4,5,6,7,8,9,10]
      fig1.add_subplot(111).plot(t,listaT,color1)
      canvas1=FigureCanvasTkAgg(fig1,master=ventana4)
      canvas1.draw()
      canvas1.get_tk_widget().grid(row=1,column=0)
      ventana4.update()
   
      '''
      fig2 =  Figure(figsize=(3,3), dpi=100)
      fig2.add_subplot(111).plot(t,listaAy,color2)
      canvas2=FigureCanvasTkAgg(fig2,master=ventana)
      canvas2.draw()
      canvas2.get_tk_widget().grid(row=1,column=1)

      fig3 =  Figure(figsize=(3,3), dpi=100)
      fig3.add_subplot(111).plot(t,listaAz,color3)
      canvas3=FigureCanvasTkAgg(fig3,master=ventana)
      canvas3.draw()
      canvas3.get_tk_widget().grid(row=1,column=2)
      
      fig4 =  Figure(figsize=(4,4), dpi=100)
      fig4.add_subplot(111).plot(t,listaAt,color4)
      canvas4=FigureCanvasTkAgg(fig4,master=ventana)
      canvas4.draw()
      canvas4.get_tk_widget().grid(row=2,column=1)'''
      
  
def crearBoton(ventana,texto,color):
  return Label(ventana,text=texto,bg=color,width=40)

def ubicar(elemento,fila,columna):
  return elemento.grid(row=fila,column=columna)

#Se descompone el texto que se lee de los sensores para cada variable
def datos():
  try:
    cadena = P.lectura()
  except TypeError:
    print("Error de Byte")
  else:
    temporal=cadena.split('V')
    ax2=temporal[1]
    ay2=temporal[2]
    az2=temporal[3]
    at2=temporal[4]
    p2=temporal[5]
    t2=temporal[6]
    h2=temporal[7]
    a2=temporal[8]
  return (ax2,ay2,az2,at2,p2,t2,h2,a2)

#Función de excepción para valores que no se pueden convertir
def adjuntar():
  global ax,ay,az,at,p,t,h,a
  ax,ay,az,at,p,t,h,a = datos()
  try:
    c=0
    listaAx.append(float(ax))
    c=1
    listaAy.append(float(ay))
    c=2
    listaAz.append(float(az))
    c=3
    listaAt.append(float(az))
    c=4
    listaP.append(float(p))
    c=5
    listaT.append(float(t))
    c=6
    listaH.append(float(h))
    c=7
    listaA.append(float(a))     
    
  except ValueError:
    if c==0:
      adjuntar()
    elif c==1:
      listaAx.pop(0)
      adjuntar()
    elif c==2:
      listaAx.pop(0)
      listaAy.pop(0)
      adjuntar()
    elif c==3:
      listaAx.pop(0)
      listaAy.pop(0)
      listaAz.pop(0)
      adjuntar()
    elif c==4:
      listaAx.pop(0)
      listaAy.pop(0)
      listaAz.pop(0)
      listaAt.pop(0)
      adjuntar()
    elif c==5:
      listaAx.pop(0)
      listaAy.pop(0)
      listaAz.pop(0)
      listaAt.pop(0)
      listaP.pop(0)
      adjuntar()
    elif c==6:
      listaAx.pop(0)
      listaAy.pop(0)
      listaAz.pop(0)
      listaAt.pop(0)
      listaP.pop(0)
      listaT.pop(0)
      adjuntar()
    else:
      listaAx.pop(0)
      listaAy.pop(0)
      listaAz.pop(0)
      listaAt.pop(0)
      listaP.pop(0)
      listaT.pop(0)
      listaH.pop(0)
      adjuntar()
  else:
      print("Todo Bien")

def ciclo(comp):
  
  global c
  listaAx.pop(0)
  listaAy.pop(0)
  listaAz.pop(0)
  listaAt.pop(0)
  listaP.pop(0)
  listaT.pop(0)
  listaH.pop(0)
  listaA.pop(0)

  adjuntar()

  print("Aceleracion en X:"+ax)               
  print("Aceleracion en Y:"+ay)
  print("Aceleracion en Z:"+az)
  print("Aceleracion Total:"+at)
  print("Presion:"+p)
  print("Temperatura:"+t)
  print("Humedad:"+h)
  print("Altura:"+a)
  
  if comp==5:
      canvas('r','b','g','y',5)
      pedroaja="Aceleracion en X: "+ax+" m/s²"
      label1.configure(text=pedroaja)
      pedrolatx="Latitud: "+lat
      pedrolongx="Longitud: "+long
      pedroaltx="Altura: "+a+" mts"
      latx.configure(text=pedrolatx)
      longx.configure(text=pedrolongx)
      altx.configure(text=pedroaltx)
      #v1.after(1000,ciclo(5))
      ciclo(5)
      #v1.update()

  
  elif comp==6:
      canvas('r','b','g','y',6)
      pedroaje="Aceleracion en Y: "+ay+" m/s²"
      label2.configure(text=pedroaje)
      pedrolaty="Latitud: "+lat
      pedrolongy="Longitud: "+long
      pedroalty="Altura: "+a+" mts"
      laty.configure(text=pedrolaty)
      longy.configure(text=pedrolongy)
      alty.configure(text=pedroalty)    
     
      ciclo(6)
        
  elif comp==7:
      canvas('r','b','g','y',7)
      pedroaji="Aceleracion en Z: "+az+" m/s²"
      label3.configure(text=pedroaji)
      pedrolatz="Latitud: "+lat
      pedrolongz="Longitud: "+long
      pedroaltz="Altura: "+a+" mts"
      latz.configure(text=pedrolatz)
      longz.configure(text=pedrolongz)
      altz.configure(text=pedroaltz)       
      
      ciclo(7)
  
  elif comp==8:
      canvas('r','b','g','y',8)
      pedroajo="Aceleracion Total: "+at+" m/s²"
      label4.configure(text=pedroajo)
      pedrolatt="Latitud: "+lat
      pedrolongt="Longitud: "+long
      pedroaltt="Altura: "+a+" mts"
      latt.configure(text=pedrolatt)
      longt.configure(text=pedrolongt)
      altt.configure(text=pedroaltt)       
      
      ciclo(8)
  
  
  elif comp==2:
      canvas('r','b','g','y',2)
      texto5="Presión: "+p+" Pa"
      texto6="Latitud: "+lat
      texto7="Longitud: "+long
      texto8="Altitud: "+a+" mts"
      label5.configure(text=texto5)
      label6.configure(text=texto6)
      label7.configure(text=texto7)
      label8.configure(text=texto8)
      ciclo(2)
  
  elif comp==3:
      canvas('r','b','g','y',3)
      texto1="Humedad: "+h+"%"
      texto2="Latitud: "+lat
      texto3="Longitud: "+long
      texto4="Altitud: "+a+" mts"
      label9.configure(text=texto1)
      label10.configure(text=texto2)
      label11.configure(text=texto3)
      label12.configure(text=texto4)
      ciclo(3)
  
  elif comp==4:
      canvas('r','b','g','y',4)
      texto13="Temperatura: "+t
      texto14="Latitud: "+lat
      texto15="Longitud: "+long
      texto16="Altitud: "+a
      label13.configure(text=texto13)
      label14.configure(text=texto14)
      label15.configure(text=texto15)
      label16.configure(text=texto16)
      ciclo(4)
  
  #ciclo()
  

ventanaPrincipal()
'''  
while True:
  ventana()
  ciclo()
'''
