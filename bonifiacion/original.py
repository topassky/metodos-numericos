import numpy as np

def u(x,y,ca,ba):
    n=len(x)
    suma1 = 0
    for i in range(n):
        suma1=suma1+(np.log(y[i])*y[i])/(x[i]-ba)**(ca)
    
    suma2 = 0
    for i in range(n):
        suma2 = suma2 + (1)/(x[i]-ba)**(2*ca+1)
    
    suma3 = 0
    for i in range(n):
        suma3 = suma3 + (np.log(y[i])*y[i])/(x[i]-ba)**(ca+1)
    
    suma4 = 0
    for i in range(n):
        suma4 = suma4 +(1)/(x[i]-ba)**(2*ca)
    
    return suma1*suma2-suma3*suma4

def v(x,y,ca,ba):
    n=len(x)
    suma1 = 0
    for i in range (n):
        suma1 = suma1 + (np.log(y[i])*y[i])/(x[i]-ca)**(ca)
    
    suma2 = 0
    for i in range(n):
        suma2 = suma2 +(np.log(x[i]-ba))/(x[i]-ba)**(2*ca)
    
    suma3 = 0
    for i in range(n):
        suma3 = suma3 +(np.log(y[i])*y[i]*(np.log(x[i]-ba)))/(x[i]-ba)**ca
        
    suma4 = 0
    for i in range(n):
        suma4 = suma4 +(1/(x[i]-ba)**(2*ca))
        
    return suma1*suma2-suma3*suma4

def a(x,y,ca,ba):
    n = len(x)
    suma1 = 0
    for i in range(n):
        suma1 =suma1 +(np.log(y[i])*y[i])/(x[i]-ba)**(ca)
    suma2 = 0
    for i in range(n):
        suma2 = suma2+(1/(x[i]-ba)**(2*ca))
        
    return suma1/suma2
    
    
    
