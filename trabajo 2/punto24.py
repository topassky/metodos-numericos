#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
2.1.4(20 %) La Ley de Hooke, que se cumple cuando un resorte no se estira más allá
 de cierto lı́mite,significa que la extensión de este resorte y la fuerza que
 se le aplica están relacionadas linealmente. Laproporcionalidad está paramet
rizada por la constante k del resorte. Un valor para dicho parámetro se esta
blece de forma experimental con la colocación de pesos conocidos en el 
resorte y la medición de la compresión que resulta. Tales datos a parecen en
la siguiente tabla: Si se grafican los datos,
x, m 		0.10  	0.17 	0.27 	0.35 	0.39 	0.42 	0.43 	0.44
F, 10 4 N 	10 	20 	30 	40 	50 	60 	70 	80
se puede observar que por encima de un peso de 40 × 10 4 N , la relación
 lineal entre la fuerza y el desplazamiento desaparece. Esta clase de compor
tamiento es común de lo que se denomina “resorteen deformación”.
'''

import numpy as np
import matplotlib.pyplot as plt	


def f(x,m,b,X,Y):
	'''Funciòn de retornanr una funcion evaluada en cierto punto para 
	este ejercicio con una inflexion en el punto 40 se retorna
	ala funcion lienal y la cuadràtica para x>40:
	Entradas: valores de X, pendiente y desplazamiento b, Vector cuadraticos (X,Y)
	SAlidas: Funciòn evaluada en el punto x'''
	if x<50:	return (m*x+b)
	else:		
		cons = regresion_cuadratica(X, Y)
		return(cons[2]*(x*x) + cons[1]*(x) + cons[0])


def regresion_cuadratica(x, y):
    '''
	Muestra la regresion cuadràtica de dos variables
	Entradas: los dos vectores X, y
	
    '''
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


def regresion_lineal(x, y):
    '''
	Muestra la regresion lineal de dos variables
	Entradas: los dos vectores X, y
	Salidas: m (opcional)
    '''
    '''
	Muestra la regresion lineal de dos variables
	Entradas: los dos vectores X, y
	Salidas: m (opcional b)
    '''

    n=len(x);
    a1=b1=0.0
    
    #pendiente de la recta de regresión, a
    sy=sx=sx2=xy=0
    for i in range(len(x)):
      xy=xy+x[i]*y[i]
      sx=sx+x[i]
      sx2=sx2+(x[i]*x[i])
      sy=sy+y[i]
    
    a1=(n*xy-sx*sy)/(n*sx2-sx*sx)
    #%ordenada en el origen, b
    b1=(sy-a1*sx)/n
   
    #errores de a y de b
    '''sd2=((y-a1*sx-b1)**0.5)
    a2=(sd2/(n-2)**0.5)/((sx2-sx*sx/n))**0.5
    #b2=((sx2/n)*a[2])**0.5'''
    #print (a1,b1)

    return a1,b1

def parteB(X,Y):
	'''
	Funcion que calcula la regresiòn por segmentos
	'''

	cons = regresion_cuadratica(X, Y)
	func = (lambda x : cons[2]*(x*x) + cons[1]*(x) + cons[0])
	u = func(75)
	return u
	#print(u)

Fl= [10, 	20, 	30, 	40]
Fnl=[50, 	60 ,	70 ,	80]
Xl=[0.10,  	0.17, 	0.27, 	0.35 	]
Xnl=[0.39, 	0.42, 	0.43, 	0.44]

F=[10, 	20, 	30, 	40,50, 	60 ,	70 ,	80 ]
X=[0.10,  	0.17, 	0.27, 	0.35, 0.39, 	0.42, 	0.43, 	0.44]
k,b=regresion_lineal(Fl, Xl)
print("a) La parte lineal muestra una constante de resorte de " +str(k))
print("b) La funciòn en el punto dado vale: "+str(parteB(Fnl,Xnl)));

plt.plot(F,X,'bo',F,[f(i,k,b,Fnl,Xnl) for i in F] , 'g-')
plt.title('resorte en deformación')
plt.xlabel('x') 
plt.ylabel('F') 
plt.grid()
plt.show()

