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

x = np.linspace(-0.5e10,0.5e10,100)
fu = (lambda x : (6.5e6*(1.7e-19*((1/2)*(x**2+np.sqrt(x**2+4*(6.21e9)**2)))*1360*(1000/300)**(-2.42))-1))
y = fu(x)
plt.plot(x,y,color = 'blue')
plt.title('Grafica de la función')
plt.xlabel('Eje x')
plt.ylabel('Eje y')
plt.grid()
plt.show()

a = 0
b = 2.5e9
tol = 1e-6
p,i = ModFalsePos(a,b,fu,tol)
print("El valor de la raíz es: {} y el numero de interaciones es: {}".format(p, i))