# -*- coding: utf-8 -*-
"""TDMA.ipynb
TDMA
"""

import numpy as np  
 
def TDMA(a,b,c,d):    
    a = a.astype('double')  
    b = b.astype('double')  
    c = c.astype('double')  
    d = d.astype('double')  
    
    n=np.shape(a)[0]  
  
    x=np.zeros(n)  
 
    c[0]=c[0]/b[0]  
    for i in np.arange(1,n-1,1):  
       c[i]=c[i]/(b[i]-a[i]*c[i-1])  
 
    d[0]=d[0]/b[0]  
    for i in np.arange(1,n,1):  
       d[i]=(d[i]-a[i]*d[i-1])/(b[i]-a[i]*c[i-1])  
 
    x[n-1]=d[n-1]  
    for i in np.arange(n-2,-1,-1):  
       x[i]=d[i]-c[i]*x[i+1]  
 
    return x  
a = np.array([0,-13.422,-12.252,-12.377])
b = np.array([13.422,12.252,12.377,11.797])
c = np.array([0,0,0,0])
d = np.array([750.5, 300, 102, 30])

x = TDMA(a,b,c,d)

print('la solución es: c1 = {},c2 = {},c3 = {},c4 = {}'.format(x[0],x[1],x[2],x[3]))
