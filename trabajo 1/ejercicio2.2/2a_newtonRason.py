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

#Graficar la derivada para saber el intervalo de la función
x = np.linspace(-20000,20000,100)
f = (lambda x : ((x/10)*(np.cosh(500/x))-(x/10)-10),
     lambda x: (1/10)*((-(500*np.sinh(500/x))/x) +np.cosh(500/x) -1))

y = f[0](x)
plt.plot(x,y,color = 'blue')
plt.title('Grafico de la función')
plt.xlabel('Eje x')
plt.ylabel('Eje y')
plt.grid()
plt.show()

x0 = 1
tol = 1e-6
xr, i = NewtonRaphson(f[0],f[1],x0,tol)
print("El valor de la raíz es: {} y el numero de interaciones es: {}".format(xr, i))