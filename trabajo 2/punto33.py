#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''2.2.3(20 %) Es frecuente que las reacciones quı́micas sigan este modelo:
dc
= −kc**n
dt
donde c es la concentración, t es el tiempo, k es la tasa de reacción y n el
 orden de dicha reacción.Es posible evaluar valores dados de c y dc/dt, k
 y n por medio de regresión lineal del logaritmo de la siguiente ecuación:

     dc
           = ln k + n ln c
ln   ----
      dt
---y------= b + m *ln c
Use este enfoque y los datos que siguen para estimar los valores de k 
y n usando las fórmulas de aproximación más precisas:
t=    10  20     30    40    50    60
c=  3.52, 2.48, 1.75, 1.23, 0.87, 0.61'''
import numpy as np
import matplotlib.pyplot as plt	


def f(x,m,b):
	return (m*x+b)

def inicio():
  t=   [ 10,  20,     30,    40,    50 ,   60]### p variable independiente
  c=  [np.log(3.52), np.log(2.48), np.log( 1.75), np.log( 1.23), np.log( 0.87), np.log( 0.61)] ## T variable dependiente
 
  m,b=pendiente(t,c)
  plt.plot(t,c,'bo',t,[f(i,(m),(b)) for i in t] , 'g-',)
  plt.title('Regresion lineal')
  plt.xlabel('X')
  plt.ylabel('Y') 
  plt.show()
  print("El valor de n es: " + str(m)+" y el valor de ln(k)= "+str(b))
  
  
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

inicio()
