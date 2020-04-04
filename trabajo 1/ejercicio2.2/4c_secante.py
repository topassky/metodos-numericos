import numpy as np
import sympy as sp
import matplotlib.pyplot as plt


def Fixpt(g,x0,a,b,tol):
  #definir el errro para el arranque.
  error = 99999
  #agregar el contador
  i = 0
  #raiz inicial
  xr = x0
  m= abs(g(b)-g(a))/(b-a)
  if (m < 1):
    while error > tol:
      xrold = xr
      xr = g(xrold)
      i = i + 1
      if(xr != 0):
        error = abs((xr-xrold)/xr)
      else:
        break
  else:
    xr = np.nan
  
  return xr, i

g = (lambda x :(1/(-2*np.log10((0.0000015)/(3.7*0.005)+((2.51)/((13743.01676)*(x)**(1/2))))))**2)
x0 = 0.0001
a = 0.0001
b = 1
tol = 1e-5

xr, i = Fixpt(g,x0,a,b,tol)
print("El valor de la raíz es: {} y el numero de interaciones es: {}".format(xr, i))
