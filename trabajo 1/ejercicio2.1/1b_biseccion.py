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
    p, i = biseccion(fu,a,b,tol)
    print("El valor de la raíz es: {} y el numero de interacciones es: {}".format(p, i))
