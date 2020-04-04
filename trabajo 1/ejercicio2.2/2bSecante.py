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

#Graficar la derivada para saber el intervalo de la función
x = np.linspace(0,10,100)
f = (lambda x : ((x/10)*(np.cosh(500/x))-(x/10)-10))
y = f(x)
plt.plot(x,y,color = 'blue')
plt.title('Grafico de la función')
plt.xlabel('Eje x')
plt.ylabel('Eje y')
plt.grid()
plt.show()

x0 = 501
x1 = 543
tol = 1e-6

xr, i = Secante(f,x0,x1,tol)
print("El valor de la raíz es: {} y el numero de interaciones es: {}".format(xr, i))
