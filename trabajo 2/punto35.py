#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''La tasa de enfriamiento de un cuerpo se expresa como:
dT
__ = −k(T − T a )
dt
donde T es la temperatura del cuerpo ( ◦ C), T a es la temperatura del medio circundante ( ◦ C) y k
la constante de proporcionalidad (min −1 ). Ası́, esta ecuación, (denominada ley de Newton para el
enfriamiento) especı́fica que la tasa de enfriamiento es proporcional a la diferencia de temperaturas
del cuerpo y del medio circundante. Si una bola de metal calentada a 80 ◦ se sumerge en agua que
se mantiene a T a = 20 ◦ C constante, la temperatura de la bola cambia ası́:
t, min 		0 	5 	10 	15 	20 	25
T, ◦ 		80 	44.5 	30.0 	24.1 	21.7 	20.7

Utilice diferenciación numérica para determinar dT /dt en cada valor del tiempo. Grafique dT /dt
contra T − T a y empl
'''

import numpy as np
import matplotlib.pyplot as plt

def f(x,m,b):
	return (m*x+b)

		
def temperatura():
  p =[80.0-20 ,44.5-20 ,30.0-20 ,24.1-20 ,21.7-20 ,20.7-20] ### p variable dependiente
  T = [0 ,	5, 	10 ,	15, 	20 ,	25]  ## T variable independiente
  m,b=pendiente(T,p)
  
  K= m
  print("El valor de K es: "+str(K)+" min ^-1")
  #Crear la grafica

  plt.plot(T,p,'bo',T,[f(i,m,b) for i in T] , 'g-',)
  plt.title("Decaimiento de la temperatura") # Establece el título del gráfico.
  plt.xlabel("dT/dt") # Establece el título del eje x.
  plt.ylabel("T-Ta") # Establece el título del eje y.
  plt.grid()
  plt.show()

  
  
def pendiente(x,y): #cada punto contiene dos vectores  = [independiente,dependiente] 
    '''
	Muestra la regresion lineal de dos variables
	Entradas: los dos vectores X, y
	Salidas: m (opcional b)
    '''

    n=len(x);
    a1=b1=0.0
    
    #pendiente de la recta de regresión, a
    sy=sx=sx2=xy=0
    for i in range(len(x)):
      xy=xy+x[i]*y[i]
      sx=sx+x[i]
      sx2=sx2+(x[i]*x[i])
      sy=sy+y[i]
    
    a1=(n*xy-sx*sy)/(n*sx2-sx*sx)
    #%ordenada en el origen, b
    b1=(sy-a1*sx)/n
   
    #errores de a y de b
    '''sd2=((y-a1*sx-b1)**0.5)
    a2=(sd2/(n-2)**0.5)/((sx2-sx*sx/n))**0.5
    #b2=((sx2/n)*a[2])**0.5'''


    print (a1,b1)

    return a1,b1

temperatura()
