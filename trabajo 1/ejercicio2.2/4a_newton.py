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

f = (lambda x : (1/(x)**(1/2))+2*np.log10((0.0000015)/(3.7*0.005)+((2.51)/((13743.01676)*(x)**(1/2)))),
     lambda x: (-1.12627 - 1.47826*np.sqrt(x))/(2.25254*x**(3/2) + x**2))
x = np.linspace(0.0001,20,100)
y = f[0](x)
plt.plot(x,y,color = 'blue')
plt.title('Grafico de la función')
plt.xlabel('Eje x')
plt.ylabel('Eje y')
plt.grid()
plt.show()
x0 = 0.01
tol = 1e-5

xr, i = NewtonRaphson(f[0],f[1],x0,tol)
print("El valor de la raíz es: {} y el numero de interaciones es: {}".format(xr, i))
