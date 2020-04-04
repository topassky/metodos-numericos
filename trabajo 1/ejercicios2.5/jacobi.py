import numpy as np

 
def jacobi(A,b,x0,tol,N):  
    #preliminares  
    A = A.astype('double')  
    b = b.astype('double')  
    x0 = x0.astype('double')  
 
    n=np.shape(A)[0]  
    x = np.zeros(n)  
    it = 0  
    #iteracoes  
    while (it < N):  
        it = it+1  
        #iteracao de Jacobi  
        for i in np.arange(n):  
            x[i] = b[i]  
            for j in np.concatenate((np.arange(0,i),np.arange(i+1,n))):  
                x[i] -= A[i,j]*x0[j]  
            x[i] /= (A[i,i]+1e-6)  
        #tolerancia  
        if (np.linalg.norm(x-x0,np.inf) < tol):  
            return x  
        #prepara nova iteracao  
        x0 = np.copy(x)  
    
    return x

a = np.array([[6,0,-1,0,0],[1,-1,0,0,0],[3,1,0,0,-4],[0,1,8,-11,2],[0,1,-9,0,0]])
b = np.array([50,0,0,0,-160])
n = 5
x = np.array([10.,10.,10.,10.,10.])

x = jacobi (a,b,x,0.0001, 20)

print('la solución es: c1 = {},c2 = {},c3 = {},c4 = {},c5 = {} '.format(x[0],x[1],x[2],x[3],x[4]))

