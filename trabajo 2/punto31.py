import matplotlib.pyplot as plt	
import numpy as np
from math import *
def f(x) :
    return np.exp(-(x**2.0)/2.0)

def print_row(lst):
    print (' '.join('%11.8f' % x for x in lst))

def romberg(f, a, b, n=20):
    """Approximate the definite integral of f from a to b by Romberg's method.
    eps is the desired accuracy."""
    R = [[0.5 * (b - a) * (f(a) + f(b))]]  # R[0][0]
    for n in range (1,n+1):
        h = float(b-a)/2**n
        R.append((n+1)*[None])  # Add an empty row.
        R[n][0] = 0.5*R[n-1][0] + h*sum(f(a+(2*k-1)*h) for k in range(1, 2**(n-1)+1)) # for proper limits
        for m in range(1, n+1):
            R[n][m] = R[n][m-1] + (R[n][m-1] - R[n-1][m-1]) / (4**m - 1)
    return R[n][n]
   



def pm(a, b, n):
	'''
	Funcion para punto medio
	Entradas: limites y numero de iteracciones
	Salida: integral por este medio
	'''
	if (n%2)!=0:
		print("no se puede integrar")
	else:	
		h=(b-a)/n
		suma=0.0
		for i in range(0,int((n-1)/2)):
			
			xm=(a+float(i*h));
			suma=suma+f(xm)*2*h;
		XI = suma
	return XI

integral = (1/((2*np.pi)**(1/2)))*(pm(-0.5,0.0,20)+romberg(lambda x: np.exp(-(x**2.0)/2.0), -2, 1))
print("El resultado de la parte impropia mas la parte definida es:"+ str(integral))
plt.plot([f(i/100) for i in range(-1000,800)] , 'g-',)
plt.title('Función normal')
plt.xlabel('X') 
plt.ylabel('Y') 
plt.grid()
plt.show()
