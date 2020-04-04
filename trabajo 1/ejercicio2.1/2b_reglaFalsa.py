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

H = np.linspace(0,10,100)
f = (lambda x : np.sqrt(19.6*x)*np.tanh(np.sqrt(2.45*x)*2.5)-5)
y = f(H)
plt.plot(H,y,color = 'blue')
plt.title('Grafico de la función')
plt.xlabel('Eje x')
plt.ylabel('Eje y')
plt.grid()
plt.show()


a = 0
b = 4
tol = 0.0000001
p,i = ModFalsePos(a,b,f,tol)
print("El valor de la raíz es: {} y el numero de interaciones es: {}".format(p, i))
