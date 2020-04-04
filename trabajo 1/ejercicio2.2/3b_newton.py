import numpy as np
import sympy as sp
import matplotlib.pyplot as plt


def NewtonRaphson(f,fde,x0,tol):
  #definir el errro para el arranque.
  error = 99999
  #agregar el contador
  i = 0
  #raiz inicial
  xr = x0
  while error > tol:
    xrold = xr
    xr = xrold-(f(xrold)/fde(xrold))
    i = i + 1
    if(xr != 0):
      error = abs((xr-xrold)/xr)
    else:
      break
  return xr, i

f = (lambda x : (((0.0002)**(1/2)*(20*x)**(5/3))/((0.03)*(20+2*x)**(2/3)))-5,
     lambda x: ((x/(x+10))*(437613*x+729355))/(x+10))

x0 = 0.1
tol = 0.0005

xr, i = NewtonRaphson(f[0],f[1],x0,tol)
print("El valor de la raíz es: {} y el numero de interaciones es: {}".format(xr, i))