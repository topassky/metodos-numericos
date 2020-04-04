import numpy as np
import matplotlib.pyplot as plt

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


x = np.linspace(-0.5e10,0.5e10,100)
fu = (lambda x : (6.5e6*(1.7e-19*((1/2)*(x**2+np.sqrt(x**2+4*(6.21e9)**2)))*1360*(1000/300)**(-2.42))-1))
y = fu(x)
plt.plot(x,y,color = 'blue')
plt.title('Grafica de la función')
plt.xlabel('Eje x')
plt.ylabel('Eje y')
plt.grid()
plt.show()

a = -2.5e9
b = 2.5e9
tol = 1e-6
p,i = biseccion(fu,a,b,tol)
print("El valor de la raíz es: {} y el numero de interaciones es: {}".format(p, i))