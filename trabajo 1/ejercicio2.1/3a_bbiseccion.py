import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Se calcula la derivada para sacar los puntos criticos.
x = sp.Symbol('x') 
y = ((2500/(120*50000000*3000*600))*(-5*x**5+2*((600)**(2))*x**(3)-((600)**(4))*x))
deri = sp.diff(y,x)
segundaderi = sp.diff(deri,x)
print(deri)
print(segundaderi)

x = np.linspace(-10,10,100)
fu = (lambda x : -5.78703703703704e-12*x**4 + 5.0e-7*x**2 - 0.03)
y = fu(x)
plt.plot(x,y,color = 'blue')
plt.title('Derivada de la función')
plt.xlabel('Eje x')
plt.ylabel('Eje y')
plt.grid()
plt.show()

def biseccion(f,a,b,tol):
  #definir el errro para el arranque.
  error = 99999
  #agregar el contador
  i = 0
  while error > tol:
    #Calcular el punto medio
    p = (a+b)/2
    #Evaluar los signos
    if (f(b)*f(a) < 0):
      b = p
    else:
      a = p
    #actualizar el error
    error = (b-a)/2
    #actualizar las interacciones
    i += 1
  return p,i


def maxomin(f,x):
  y = f(x)
  if (y > 0):
    resp = "minimo"
  else:
    resp = "maximo"
  return resp


a = -10
b = 10
tol = 1e-6
p,i = biseccion(fu,a,b,tol)
print("El valor de la raíz es: {} y el numero de interaciones es: {}".format(p, i))

seg = (lambda x : -2.31481481481481e-11*x**3 + 1.0e-6*x)
resp = maxomin(seg,p)

funcion = (lambda x: ((2500/(120*50000000*3000*600))*(-5*x**5+2*((600)**(2))*x**(3)-((600)**(4))*x)))
valor = funcion(p)
print ("el valor {} es: {}".format(resp, valor ))

x = np.linspace(-20,20,100)
y = funcion(x)
plt.plot(x,y,color = 'red')
plt.title('Grafica de la función')
plt.xlabel('Eje x')
plt.ylabel('Eje y')
plt.grid()
plt.show()
