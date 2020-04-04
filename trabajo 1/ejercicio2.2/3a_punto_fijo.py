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

#Graficar la derivada para saber el intervalo de la función
x = np.linspace(0,50,100)
f = (lambda x : (((0.0002)**(1/2)*(20*x)**(5/3))/((0.03)*(20+2*x)**(2/3)))-5)
y = f(x)
plt.plot(x,y,color = 'blue')
plt.title('Grafico de la función')
plt.xlabel('Eje x')
plt.ylabel('Eje y')
plt.grid()
plt.show()

g = (lambda x :((((0.15)*(20+2*x)**(2/3))/((0.0002)**(1/2)))**(3/5))/20)
x0 = 1.1
a = 0
b = 10
tol = 0.0005

xr, i = Fixpt(g,x0,a,b,tol)
print("El valor de la raíz es: {} y el numero de interaciones es: {}".format(xr, i))