import numpy as np
import matplotlib.pyplot as plt

def ModFalsePos(xl,xu, f, tol):
    i = 0
    xr = (xl+xu)/2
    fl = f(xl)
    fu = f(xu)
    error = 99999
    while (error > tol):

        xold = xr
        xr = xu - fu * (xl - xu) / (fl - fu)
        test = f(xl)*f(xr)
        if (test<0):
            xu = xr
            fu = f(xu)
        else:
            xl = xr
            fl = f(xl)
        error = abs((xr - xold)/xr)
        
        i=i+1
        
    return xr, i
#Graficar la derivada para saber el intervalo de la función
x = np.linspace(-20,20,100)
f = (lambda x : 3.5*x**4 - 32*x**3 + 132*x**2 - 180*x - 25182)
y = f(x)
plt.plot(x,y,color = 'blue')
plt.title('Grafico de la primera derivada')
plt.xlabel('Eje x')
plt.ylabel('Eje y')
plt.grid()
#plt.show()

a = -7.5
b = -5
tol = 1e-5

p,i = ModFalsePos(a,b,f,tol)
print("El valor de la raíz es: {} y el numero de interaciones es: {}".format(p, i))

def maxomin(f,x):
  y = f(x)
  if (y > 0):
    resp = "minimo"
  else:
    resp = "maximo"
  return resp
 
segundaderi = (lambda x :14.0*x**3 - 96*x**2 + 264*x - 180)
resp = maxomin(segundaderi,p)

funcion = (lambda x: -25182*x-90*x**2+44*x**3-8*x**4+0.7*x**5)
valor = funcion (p)

print ("el valor {} es: {}".format(resp, valor ))

a = 10
b = 12
tol = 1e-5
p,i = ModFalsePos(a,b,f,tol)
print("El valor de la raíz es: {} y el numero de interaciones es: {}".format(p, i))
resp = maxomin(segundaderi,p)
funcion = (lambda x: -25182*x-90*x**2+44*x**3-8*x**4+0.7*x**5)
valor = funcion (p)
print ("el valor {} es: {}".format(resp, valor ))
