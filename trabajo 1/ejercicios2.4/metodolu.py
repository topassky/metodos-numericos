# -*- coding: utf-8 -*-
"""metodoLU

"""

import numpy as np
def factorizacionLU(matrix,vector,m):
  x =np.zeros(m)
  u = np.zeros([m,m])
  l = np.zeros([m,m])
  u = matrix
  for k in range(0, m):
    for r in range(0,m):
      if(k==r):
          l[k,r] = 1
      if (k<r):
          factor = (matrix[r,k]/matrix[k,k])
          l[r,k] = factor
          for c in range(0,m):
              matrix[r,c] = matrix[r,c]-(factor*matrix[k,c])
              u[r,c] = matrix[r,c]
  
  z = np.linalg.inv(l)@ vector
  #sustitución hacia atrás
  x[m-1] = z[m-1]/u[m-1,m-1]
  for r in range(m-2,-1,-1):
    suma = 0 
    for c in range(0,m):
      suma=suma+u[r,c]*x[c]
      x[r]=(vector[r]-suma)/u[r,r]

  return l,u,x

matrix = np.array([[130,-30,0],[1,-1,0],[40,60,-120]],dtype=np.float64)
vector = np.array([500,0,-500],dtype=np.float64)
m = 3
l,u,x = factorizacionLU(matrix,vector,m)
print('la solución es: c1 = {},c2 = {},c3 = {}'.format(x[0],x[1],x[2]))
