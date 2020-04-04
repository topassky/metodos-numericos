# -*- coding: utf-8 -*-
"""

**Tecnica SOR**

1. (25 %) Para los ejercicios, escriba un código en Matlab/Octave o Pyhton que grafique en el
intervalo pedido y que aplique la técnica SOR automáticamente. En todos los casos use tol = 10 −5
(a) (33.3 %) Escriba la ecuación x 3 + 3x − 6 = 0 de 4 formas distintas y aplique la técnica SOR
para determinar la raı́z existente en el intervalo [1, 2]
"""

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

def m(g, a, b):
  m= abs(g(b)-g(a))/(b-a)
  return m


def Fixpt(g,x0,a,b,tol):
  #definir el errro para el arranque.
  error = 99999
  #agregar el contador
  i = 0
  #raiz inicial
  xr = x0

  while error > tol:
    xrold = xr
    xr = g(xrold)
    i = i + 1
    if(xr != 0):
      error = abs((xr-xrold)/xr)
    else:
      break

  
  return xr, i

#Graficar la derivada para saber el intervalo de la función
x = np.linspace(-20,20,100)
f = (lambda x : x**3+3*x-6)
y = f(x)
plt.plot(x,y,color = 'blue')
plt.title('Grafico de la primera derivada')
plt.xlabel('Eje x')
plt.ylabel('Eje y')
plt.grid()
plt.show()


g = (lambda x :(6-3*x)**(1/3))

x0 = 1.1
a = -10
b = 10
tol = 1e-5
m = m(g,a,b)
G = (lambda x, M = m: (float(M*x)-1.0*(6-3*x)**(1/3))/(float(M)-1))
xr, i = Fixpt(G,x0,a,b,tol)
print("El valor de la raíz es: {} y el numero de interaciones es: {}".format(xr, i))

"""(b) (33.3 %) Escriba la ecuación 10e −x sin (x) − 1 = 0 de 3 formas distintas y encuentre la solución en el intervalo [0, 1]"""

def m(g, a, b):
  m= abs(g(b)-g(a))/(b-a)
  return m


def Fixpt(g,x0,a,b,tol):
  #definir el errro para el arranque.
  error = 99999
  #agregar el contador
  i = 0
  #raiz inicial
  xr = x0

  while error > tol:
    xrold = xr
    xr = g(xrold)
    i = i + 1
    if(xr != 0):
      error = abs((xr-xrold)/xr)
    else:
      break

  
  return xr, i


#Graficar la derivada para saber el intervalo de la función
x = np.linspace(0,1,100)
f = (lambda x :10*np.exp(x)*np.sin(x)-1)
y = f(x)
plt.plot(x,y,color = 'blue')
plt.title('Grafico de la función')
plt.xlabel('Eje x')
plt.ylabel('Eje y')
plt.grid()
plt.show()

g = lambda x : (np.arcsin(1/(10*np.exp(-x))))
x0 = 0.5
a = 0
b = 1
tol = 1e-5
m = m(g,a,b)

G = (lambda x, M = m: (float(M*x)-1.0*(np.arcsin(1/(10*np.exp(-x)))))/(float(M)-1))
xr, i = Fixpt(G,x0,a,b,tol)
print("El valor de la raíz es: {} y el numero de interaciones es: {}".format(xr, i))

"""(c) (33.3 %) Escriba la ecuación tan (2 − x) − x = 0 de 3 formas distintas y encuentre la raı́z en el
intervalo [1.1, 5]
"""

def m(g, a, b):
  m= abs(g(b)-g(a))/(b-a)
  return m


def Fixpt(g,x0,a,b,tol):
  #definir el errro para el arranque.
  error = 99999
  #agregar el contador
  i = 0
  #raiz inicial
  xr = x0

  while error > tol:
    xrold = xr
    xr = g(xrold)
    i = i + 1
    if(xr != 0):
      error = abs((xr-xrold)/xr)
    else:
      break

  
  return xr, i


#Graficar la derivada para saber el intervalo de la función
x = np.linspace(0,5,100)
f = (lambda x :np.tan(2-x)-x)
y = f(x)
plt.plot(x,y,color = 'blue')
plt.title('Grafico de la función')
plt.xlabel('Eje x')
plt.ylabel('Eje y')
plt.grid()
plt.show()

g = lambda x : (2-np.arctan(x))
x0 = 2
a = 1.1
b = 5
tol = 1e-5
m = m(g,a,b)

G = (lambda x, M = m: (float(M*x)-1.0*(2-np.arctan(x))/(float(M)-1)))
xr, i = Fixpt(G,x0,a,b,tol)
print("El valor de la raíz es: {} y el numero de interaciones es: {}".format(xr, i))