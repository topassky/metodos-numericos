import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

def Secante(f,x0, x1, tol):
  error = 99999
  raiz = []
  raiz.insert(0,0)
  i = 0

  while error > tol:
    x2 = x1- (f(x1)*(x1-x0))/((f(x1)-f(x0)))
    raiz.append(x2)
    i = i + 1
    x0 = x1
    x1 = x2
    error = abs ((raiz[i]-raiz[i-1])/(raiz[i]))
  return x2, i

x0 = 0.0001
x1 = 0.001
tol = 1e-5
f = (lambda x : (1/(x)**(1/2))+2*np.log10((0.0000015)/(3.7*0.005)+((2.51)/((13743.01676)*(x)**(1/2)))))
xr, i = Secante(f,x0,x1,tol)
print("El valor de la raíz es: {} y el numero de interaciones es: {}".format(xr, i))
