#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''2.2.2(20 %) Las profundidades de un rı́o H se miden a distancias espaciadas iguales a través de un canal
como se muestra en la siguiente tabla:

0	2 	4 	6 	8 	10 	12 	14 	16
0	1.9 	2 	2 	2.4	2.6 	2.25 	1.12 	0

El área de dicha sección transversal se determina por integración mediante
 la siguiente ecuación:

Emplee integración de Romberg para llevar a cabo la integración.'''

import matplotlib.pyplot as plt
import numpy as np
def f(x) :
    if x>=0 and x<2:
        return 0.0
    if x>=2 and x<4:
        return 1.9	
    if x>=4 and x<6:
        return 2.0	
    if x>=6 and x<8:
        return 2.0
    if x>=8 and x<10:
        return 2.4
    if x>=10 and x<12:
        return 2.6
    if x>=12 and x<14:
        return 2.25
    if x>=14 and x<16:
        return 1.12
    if x>12:
        return 0.0


def print_row(lst):
    print (' '.join('%11.8f' % x for x in lst))

def romberg(f, a, b, eps = 1E-8):
    """Approximate the definite integral of f from a to b by Romberg's method.
    eps is the desired accuracy."""
    R = [[0.5 * (b - a) * (f(a) + f(b))]]  # R[0][0]
    print_row(R[0])
    n = 1
    while True:
        h = float(b-a)/2**n
        R.append((n+1)*[None])  # Add an empty row.
        R[n][0] = 0.5*R[n-1][0] + h*sum(f(a+(2*k-1)*h) for k in range(1, 2**(n-1)+1)) # for proper limits
        for m in range(1, n+1):
            R[n][m] = R[n][m-1] + (R[n][m-1] - R[n-1][m-1]) / (4**m - 1)
        print_row(R[n])
        if abs(R[n][n-1] - R[n][n]) < eps:
            return R[n][n]
        n += 1

from math import *

# In this example, the error function erf(1) is evaluated.
romberg(f, 0, 16)

X=[0,	2, 	4, 	6 ,	8 ,	10 ,	12 ,	14 ,	16]
plt.plot([-f(i) for i in X] , 'g-',)
plt.title('Función generada por los datos de entreda')
plt.xlabel('X') 
plt.ylabel('Y') 
plt.grid()
plt.show()
