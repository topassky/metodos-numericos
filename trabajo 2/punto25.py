#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
'''
2.1.5 20 %) La ley de Ohm establece que la caı́da de voltaje V a través de un resistor ideal es linealmente
proporcional a la corriente i que fluye a través del resistor, como V = iR, donde R es la resistencia.
Sin embargo, los resistores reales no siempre obedecen la ley de Ohm. Suponga que usted lleva a cabo
algunos experimentos muy precisos para medir la caı́da de voltaje y la corriente correspondiente
para un resistor. Los resultados que se enlistan en la siguiente tabla, sugieren una relación curvilı́nea.
i -2 -1 -0.5 0.5 1 2
V -637 -96.5 -20.5 20.5 96.5 637
Debido al error en la medición, es común que la regresión sea el método preferido de ajuste de
curvas para analizar dichos datos experimentales. Sin embargo, la suavidad de la relación, ası́ como
la precisión de los métodos experimentales, sugieren que quizá serı́a apropiada la interpolación.
(a) (10 %) Utilice interpolación de polinomios de Newton para ajustar los datos y calcular V para
i = 0.10 ¿Cuál es el grado del polinomio que usó para generar los datos?
(b) (10 %) Repita el pro
'''

def coef(x, y):

    x.astype(float)
    y.astype(float)
    n = len(x)
    a = []
    for i in range(n):
        a.append(y[i])

    for j in range(1, n):
        for i in range(n-1, j-1, -1):
            a[i] = float(a[i]-a[i-1])/float(x[i]-x[i-j])
    

    return np.array(a)


def puntoa(x,y,a):
    func = (lambda x1 : a[0] + a[1]*(x1-x[0]) + a[2]*(x1-x[0])*(x1-x[1]) +a[3]*(x1-x[0])*(x1-x[1])*(x1-x[2]))
    x1 = np.linspace(x[0],x[len(x)-1],100)
    y1 = func(x1)
    P = func(0.10)
    plt.plot(x,y,'bo',color = 'red')
    plt.plot(x1,y1)
    plt.title('Interpolación')
    plt.xlabel('i') 
    plt.ylabel('V') 
    plt.grid()
    plt.show()
    
    return P


def b(i,V,punto):
	C = np.polyfit(i, V, 3)
	func = (lambda th: C[0]*th**3 + C[1]*th**2 + C[2]*th**1 + C[3])
	x1 = np.linspace(i[0],i[len(i)-1],100)
	y = func(x1)
	plt.plot(x1,y,color='red')
	plt.plot(i,V,'bo')
	plt.title('Interpolación polinomica')
	plt.xlabel('i') 
	plt.ylabel('V') 
	plt.grid()
	plt.show()
	u = func(punto)
	return (u)
punto=0.1
i = np.array([-2, -1, -0.5, 0.5, 1, 2])
V = np.array([-637, -96.5, -20.5, 20.5, 96.5, 637])

const= coef(i,V)
P = puntoa(i,V,const)
print("Polinomios de Newton "+str(P)+" Para un polinomio de grado 3")
print("Regresión polinómica "+str(b(i,V,punto)))


