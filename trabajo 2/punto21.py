#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''2.1.1(20 %) Los siguientes datos fueron obtenidos para determinar la 
relación entre la presión y temperatura de un volumen fijo de Nitrógeno (N).
 El volumen fijo es de 10m 3

T, ◦ C 			-40 	0   40    80   120   160
p, N/m 2 		6900 8100 9350 10500 11700 12800

Emplee la ley de gases ideales, pV = nRT , donde p en N/m 2 es la presión, 
V el volumen en m 3 ,
'''

import numpy as np
import matplotlib.pyplot as plt

def f(x,m,b):
	return (m*x+b)

def inicio():
  p = [6900.0, 8100.0, 9350.0, 10500.0, 11700.0, 12800.0] ### p variable dependiente
  Tc = [-40.0, 0.0, 40.0, 80.0, 120.0, 160.0] ## T variable independiente
  V = 10.0 
  n = 1/0.028
  #Convertir de C a Kelvin
  T=[]
  for i in Tc:
    T.append(i+273.15)
 
  m,b=pendiente(T,p)
  R= m *V/n
  print(str(R)+" J/(K*mol)")
  #Crear la grafica

  plt.plot(T,p,'bo',T,[f(i,m,b) for i in T] , 'g-',)
  plt.title('Regresion lineal')
  plt.xlabel('T') 
  plt.ylabel('P') 
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
    b1=(sy-a1*sx)/n
   
    return a1,b1

inicio()
