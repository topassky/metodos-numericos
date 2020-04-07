#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
2.1.2(20 %) Se sabe que la caida de voltaje a traves de un inductor sigue la ley 
de Faraday:V L = L(di/dt)
donde V L es la caida de voltaje (en voltios), L es la inductancia (en henrys;
 1H = 1V * s/A), e i es la corriente (en amperes). Emplee los datos de la 
siguiente tabla para estimar L
di/dt, A/s 	1 	2	4 	6 	8 	10
V i , V 	5.5	12.5 	17.5 	32 	38 	49
'''

import numpy as np
import matplotlib.pyplot as plt

def f(x,m,b):
	'''Funciòn genérica:
	Entradas: valores de X, pendiente y desplazamiento b
	SAlidas: Funciòn evaluada en el punto x'''
	return (m*x+b)

def inicio():
  
  As = [1 ,	2,	4 ,	6 ,	8 ,	10] ## variable independiente
  V = [5.5,	12.5 ,	17.5 ,	32 ,	38 ,	49] ## variable dependiente
  m,b=pendiente(As,V)
  print("El valor de decrecimiento del voltaje es: "+str(m))
  plt.plot(As,V,'bo',As,[f(i,m,b) for i in As] , 'g-',)
  plt.title('Regresion lineal')
  plt.xlabel('di/dt') 
  plt.ylabel('VL') 
  plt.grid()
  plt.show()
  
  
def pendiente(x,y): #cada punto contiene dos vectores  = [independiente,dependiente] 
    '''
	Muestra la regresion lineal de dos variables
	Entradas: los dos vectores X, y
	Salidas: m y b)
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

    return a1,b1
inicio()