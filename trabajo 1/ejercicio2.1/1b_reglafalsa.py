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

#Graficar la función para determinar el intervalo la raíz negativa
x = np.linspace(-10,10,200)
fu = (lambda x : x**2*abs((np.cos(x)))-5)
y = fu(x)
plt.plot(x,y,color = 'blue')
plt.title('Grafico de la función')
plt.xlabel('Eje x')
plt.ylabel('Eje y')
plt.grid()
#plt.show()

rangos = [[-4.8, -3.],[-3.,0.], [0., 3.], [3., 4.8]]
for i in range (0, len(rangos)):
    a = rangos[i][0]
    b = rangos[i][1]
    tol = 1e-5
    p, i = ModFalsePos(a,b,fu,tol)
    print("El valor de la raíz es: {} y el numero de interacciones es: {}".format(p, i))
