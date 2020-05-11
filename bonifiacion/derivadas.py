import numpy as np

def dudb(x,y,ca,ba):
    n=len(x)
    suma1 = 0
    for i in range(n):
        suma1= suma1+(np.log(y[i])*y[i]*(ca+1))/((x[i]-ba)**(ca+2))
        
    suma2 = 0
    for i in range(n):
        suma2 = suma2 +(1)/((x[i]-ba)**(2*ca+1))
        
    suma3 = 0
    for i in range(n):
         suma3 = suma3 + (np.log(y[i])*y[i])/(x[i]-ba)**(ca)

    suma4 = 0
    for i in range(n):
        suma4 = suma4 +(2*ca+1)/(x[i]-ba)**(2*ca+2)
    
    suma5 = 0
    for i in range(n):
        suma5 = suma5 + (np.log(y[i])*y[i]*(ca+1))/((x[i]-ba)**(ca+2))
    
    suma6 = 0
    for i in range(n):
        suma6 = suma6 +(1/(x[i]-ba)**(2*ca+1))
    
    suma7 = 0
    for i in range (n):
        suma7 =  suma7 + (np.log(y[i])*y[i])/((x[i]-ba)**(ca+1))
    
    suma8 = 0
    for i in range (n):
        suma8 = suma8 + (2*ca)/(x[i]-ba)**(2*ca+1)
        
    
    return (suma1*suma2 + suma3*suma4)-(suma5*suma6+ suma7*suma8)

def dudc(x,y,ca,ba):
    n=len(x)
    suma1 = 0
    for i in range(n):
        suma1 = suma1 + (np.log(y[i])*y[i]*(-1)*(np.log(x[i])-ba))/(x[i]-ba)**(ca)
    
    suma2 = 0
    for i in range(n):
        suma2 =  suma2 +(1)/(x[i]-ba)**(2*ca+1)
        
    suma3 = 0
    for i in range(n):
        suma3 = suma3 + (np.log(y[i])*y[i])/(x[i]-ba)**(ca)
        
    suma4 = 0
    for i in range(n):
        suma4 = suma4 + ((-2)*np.log(x[i]-ba))/(x[i]-ba)**(2*ca+1)
    
    suma5 = 0
    for i in range(n):
        suma5 = suma5 + (np.log(y[i])*y[i]*(-1)*(np.log(x[i]-ba)))/(x[i]-ba)**(ca+1)
    
    suma6 = 0
    for i in range(n):
        suma6 = suma6 + (1)/(x[i]-ba)**(2*ca)
        
    suma7 = 0
    for i in range(n):
        suma7 = suma7 + (np.log(y[i])*y[i])/((x[i]-ba)**(ca+1))
    
    suma8 = 0
    for i in range(n):
        suma8 = suma8 + ((-2)*np.log(x[i]-ba)/(x[i]-ba)**(2*ca))
    
    return (suma1*suma2+suma3*suma4)-(suma5*suma6+suma7*suma8)

def dvdb(x,y,ca,ba):
    n=len(x)
    suma1 = 0
    for i in range (n):
        suma1 = suma1 + (np.log(y[i])*y[i])*(ca+1)/((x[i]-ba)**(ca+2))
    
    suma2 = 0
    for i in range(n):
        suma2 = suma2 +(np.log(x[i]-ba))/(x[i]-ba)**(2*ca)
    
    suma3 = 0
    for i in range(n):
        suma3 = suma3+(np.log(y[i])*y[i])/(x[i]-ba)**(ca)
        
    suma4 = 0
    for i in range(n):
        suma4 = suma4 + (2*ca*np.log(x[i]-ba)-1)/((x[i]-ba)**(2*ca+1))
        
    suma5 = 0
    for i in range(n):
        suma5 = suma5 + (np.log(y[i])*y[i])*(ca*np.log(x[i]-ba)+1)/(x[i]-ba)**(ca+1)
    
    suma6 = 0
    for i in range(n):
        suma6 = suma6 + (1)/(x[i]-ba)**(2*ca)
    
    suma7 = 0
    for i in range(n):
        suma7 = suma7 +(np.log(y[i])*y[i]*np.log(x[i]-ba)/(x[i]-ba)**(ca))
        
    suma8 = 0
    for i in range(n):
        suma8 = suma8 + (2*ca)/(x[i]-ba)**(2*ca+1)
    
    return (suma1*suma2+suma3*suma4)-(suma5*suma6+suma7*suma8)


def dvdc(x,y,ca,ba):
    n=len(x)
    suma1 = 0
    for i in range (n):
        suma1 = suma1+ (np.log(y[i])*y[i]*(-1)*np.log(x[i]-ba))/(x[i]-ba)**(ca)
        
    suma2 = 0
    for i in range(n):
        suma2 = suma2 + (np.log(x[i]-ba))/((x[i]-ba)**(2*ca))
    
    suma3 = 0
    for i in range(n):
        suma3 = suma3 +(np.log(y[i])*y[i])/((x[i]-ba)**(ca))
        
    suma4 = 0
    for i in range(n):
        suma4 = suma4 +((-2)*(np.log(x[i]-ba))**(2))/(x[i]-ba)**(2*ca)
        
    suma5 = 0
    for i in range(n):
        suma5 = suma5 +(np.log(y[i])*y[i]*(np.log(x[i]-ba))**(2))*(-1)/(x[i]-ba)**(ca)
    
    suma6 = 0
    for i in range(n):
        suma6 = suma6 + (1)/(x[i]-ba)**(2*ca)
    
    suma7 = 0
    for i in range(n):
        suma7 = suma7 +(np.log(y[i])*y[i]*(np.log(x[i]-ba)))/(x[i]-ba)**(ca)
    
    suma8 = 0
    for i in range(n):
        suma8 = suma8 +(-2*np.log(x[i]-ba))/(x[i]-ba)**(2*ca)
    
    return (suma1*suma2+suma3*suma4)-(suma5*suma6+suma7*suma8)
































    











    
    
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
     
    






































        
        
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
