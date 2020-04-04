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
p,i = biseccion(f,a,b,tol)
print("El valor de la raíz es: {} y el numero de interaciones es: {}".format(p, i))
