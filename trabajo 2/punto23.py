#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
2.1.3(20 %) La viscosidad dinámica del agua μ(10 −3 N · s/m 2 )
 se relaciona con la temperatura T ( ◦ C) de la siguiente manera:
T, ◦ C 		0 	5 	10 	20 	30 	40
μ, N · s/m 2 	1.787 	1.519 	1.307 	1.002 	0.7975 	0.6529

(a) (10 %) Use interpolación para predecir μ con T = 7.5 ◦ C (b) 
(10 %) Emplee regresión polinomial para ajustar una parábola a los datos
 a fin de hacer la misma predicción. Compare los resultados.
'''

import numpy as np
import matplotlib.pyplot as plt	
def  DifDiv(x,y):
	'''
	Metodo de las diferencias divididas
	Entradas: vectores t, u
	Salidas: La matriz de interpolaciòn F

	'''
	#Tammaño del vector
	n=len(x)
	#Los coheficientes se van a guardar en F(n,n)
	fdd = np.zeros([n,n])
	for i in range (0, n):
		fdd[i][0] = y[i]
    
	for j in range (1, n):
		for i in range (0, n - j):
			fdd[i][j] = (fdd[i+1][j-1] - fdd[i][j-1])/(x[i+j] - x[i])


	return(fdd)

def Eval_Pol(F, x, n_eval):
	'''
	Método para evaluar un polinomio en un punto especìfico
	Entradas:  La matriz F, el vector de variables independientes y 
		el punto a evaluar
	Salidas: el resultado de la interpolaciòn en p para ( p , n_eval)
	'''
	#Tamaño de la matriz
	n= len(F)
	sum=0
	for i in range (1,n):
		prod=1	
		for j in range(i):
			prod=prod*(n_eval - x[j])
		sum=sum+F[i,i]*prod
	p= F[0,0]+sum
	return p


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


def parteA(T,mu):
	'''
	Funcion que calcula la regresiòn mediante interpolaciòn
	'''
	F=DifDiv(T,mu)
	n_eval=7.5
	p=Eval_Pol(F,T, n_eval)
	cons = F[0]
	
	func = (lambda x : cons[0] + cons[1]*(x-T[0]) + cons[2]*(x-T[0])*(x-T[1]) +cons[3]*(x-T[0])*(x-T[1])*(x-T[2]) + cons[4]*(x-T[0])*(x-T[1])*(x-T[2])*(x-T[3]) + cons[5]*(x-T[0])*(x-T[1])*(x-T[2])*(x-T[3])*(x-T[4]))
	x = np.linspace(T[0],T[len(T)-1],100)
	y = func(x)
	plt.plot(T,mu,'bo',color = 'red')
	plt.plot(x,y)
	plt.title('Interpolación')
	plt.xlabel('T') 
	plt.ylabel('u') 
	plt.grid()
	plt.show()
	
	P = func(7.5)
	print("El resultado de u con el metodo de interpolación = "+str(P))
	return F


def parteB(T,mu):
	'''
	Funcion que calcula la regresiòn a polinomial
	'''
	cons = regresion_cuadratica(T, mu)
	func = (lambda x : cons[2]*(x*x) + cons[1]*(x) + cons[0])
	u = func(7.5)
	x = np.linspace(T[0],T[len(T)-1],100)
	y = func(x)
	plt.plot(T,mu,'bo',color='red')
	plt.plot(x,y)
	plt.title('Regresion polinomial')
	plt.xlabel('T') 
	plt.ylabel('u') 
	plt.grid()
	plt.show()	
	print('El resultado de u con el metodo de regresion_cuadratica= '+str(u))
	return func

T=[0, 	5, 	10 ,	20, 	30, 	40]
mu= [1.787, 	1.519, 	1.307 ,	1.002, 	0.7975, 	0.6529]
Seleccion= int(input("ingrese el indice del punto 3 (a=1 o b=2)="))
if (Seleccion == 1):
    reg=parteA(T, mu)
else: 
    reg=parteB(T,mu)


