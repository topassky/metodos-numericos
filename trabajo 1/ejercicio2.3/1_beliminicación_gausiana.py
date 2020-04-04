# -*- coding: utf-8 -*-
"""Eliminicación Gausiana.ipynb

"""

import numpy as np

def eliminacionGausian(matrix,vector,m,n):
    x =np.zeros((m))
    for k in range(0, m):
        for r in range(k+1,m):
            factor=(matrix[r,k]/matrix[k,k])
            vector[r]=vector[r]-(factor*vector[k])
            for c in range(0,n):
                matrix[r,c]=matrix[r,c]-(factor*matrix[k,c])

#sustitución hacia atrás
    x[m-1]=vector[m-1]/matrix[m-1,m-1]
    for r in range(m-2,-1,-1):
        suma = 0 
        for c in range(0,n):
            suma=suma+matrix[r,c]*x[c]
            x[r]=(vector[r]-suma)/matrix[r,r]
    return x

matrix = np.array([[130,-30,0],[1,-1,0],[40,60,-120]],dtype=np.float64)
vector = np.array([500,0,-500],dtype=np.float64)
m = 3
n =3
x = eliminacionGausian(matrix,vector,m,n)
print('la solución es: c1 = {},c2 = {},c3 = {}'.format(x[0],x[1],x[2]))
