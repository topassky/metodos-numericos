#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''2.2.4
(20 %) Un flujo desarrollado por completo que pasa a través de un tubo de 40 cm de diámetro tiene
el perfil de velocidad siguiente:
r, cm 0 2.5 5.0 7.5 10.0 12.5 15.0 17.5 20.0
v, m/s 0.914 0.890 0.847 0.795 0.719 0.543 0.427 0.204 0
Z
Encuentre la tasa de flujo volumétrico, Q, con la relación Q = INT(2πrvdr)0,r, donde r es el eje radial
0
del tubo, R es el radio del tubo y v es la velocidad. Resuelva el problema con dos enfoques diferentes:(a) (10 %) Realice un ajuste polinomial de grado 2 e integrela de forma analı́tica.
(b) (10 %) Utilice la regla compuesta de Simpson para evaluar la integral numéricamente. Compare
ambos resultados.
'''

import numpy as np
import matplotlib.pyplot as plt	
def f(x):
	return np.sin(x)

def Simpson(a, b, n,X,Y):
	'''
	Mètod de simpson visto en clase
	Entradas: lim inf, lkim sup, n de iteracciones, vector X y vector Y
	Salida: Integral para la tabla (trabajando con XyY)
	'''
	if (n%2)!=0:
		print("no procede")
	else:	
		h=(b-a)/n
		x=a
		XI0a=Y[0]
		x=b
		XI0b=Y[-1]
		XI0=XI0a+XI0b
		XI2=XI1=0
		for i in range(0,9):
			if (i%2) == 0:
				XI2 = XI2 + (Y[i])
			else:
				XI1 = XI1 + (Y[i])
		XI = h*(XI0 + 2*XI2 + 4*XI1)/3
	return XI



def parteA(r,f,x):
	'''
	Funcion que calcula la regresiòn a polinomial
	Entradas: Variable independiente(r), variable dependiente(f), punto a evaluar
	Salidas: Funcion evaluada en un punto especìfico	
	'''
	cons = regresion_cuadratica(r,f)
	func2= (lambda r:cons[2]*((r)*(r)) + cons[1]*(r) + cons[0])
	x = np.linspace(0,0.2,100)
	y = func2(x)
	plt.plot(r,f,'bo',color = 'red')
	plt.plot(x,y)
	plt.title('Regresion cuadratica')
	plt.xlabel('r') 
	plt.ylabel('v') 
	plt.grid()
	plt.show()

	return cons

def regresion_cuadratica(x, y):
    x = np.array(x)
    y = np.array(y)  
    n = len(x)
    sumx = sum(x)
    sumx2 = sum(x*x)
    sumx3 = sum(x*x*x)
    sumx4 = sum(x*x*x*x)
    sumy = sum(y)
    sumxy = sum(x*y)
    sumx2y = sum((x*x)*y)
    a = np.array([[n, sumx, sumx2], [sumx, sumx2, sumx3], [sumx2, sumx3, sumx4]])
    b = np.array([sumy,sumxy,sumx2y])    
    c = np.linalg.solve(a,b)
    
    return c

f=[0,0,0,0,0,0,0,0,0]
r=[0.0,2.5/100,5.0/100,7.5/100,10.0/100,12.5/100,15.0/100,15.5/100,20.0/100]
v=[0.914, 0.890, 0.847, 0.795, 0.719, 0.543 ,0.427, 0.204 ,0]
for i in range(len(r)):
	f[i]=r[i]*v[i]
print("Metodo de Simpson : "+str(Simpson(0,0.20,20,r,f)))
parteA(r,v,0)

plt.plot([Simpson(0,i,20,r,f) for i in r] , 'g-',)
plt.title('Integral de Simpson')
plt.grid()
plt.show()
