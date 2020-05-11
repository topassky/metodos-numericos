import numpy as np 
from derivadas import dudb
from derivadas import dudc
from derivadas import dvdb
from derivadas import dvdc
from original import u 
from original import v 
from original import a 


if __name__ == "__main__":
    y = [2.4,3.8,4.75,21.60]
    x = [31.8, 31.5, 31.2,30.2]
    tol = 1e-4
    errorb = 99999
    errorc = 99999
    #agregar el contador
    i = 0
    #raiz inicial
    br = 26.8
    cr = 8.3 
    while (errorb > tol)and(errorc > tol):
        brold = br
        crold = cr
        
        #derivadas parciales
        dudbr = dudb(x,y,crold,brold)
        #print(dudbr)
        #print(i)
        dudcr = dudc(x,y,crold,brold)
        dvdbr = dvdb(x,y,crold,brold)
        dvdcr = dvdc(x,y,crold,brold)
        
        #jacobiano
        jacobiano= (dudbr*dvdcr-dudcr*dvdbr)
        #funciones originales
        ur = u(x,y,crold,brold)
        vr = v(x,y,crold,brold)
    
        br = brold -((ur*dvdcr-vr*dudcr)/jacobiano)
        cr = crold - ((vr*dudbr-ur*dvdbr)/jacobiano)
        i = i + 1
        if(br != 0):
            errorb = abs((br-brold)/br)
            errorc = abs((cr-crold)/cr)
            #print(error)
        else:
            break
    # Valor resultante al evalualr las raíces, este valor tiende a 0    
    print(ur,vr)
    # Valor resultante de las raíces
    ar = a(x,y,cr,br)
    print(ar,br,cr)
    
    
    
    


        
