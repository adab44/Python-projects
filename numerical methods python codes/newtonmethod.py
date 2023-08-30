# newton method
import numpy as np
from math import e
ln =np.log

x0 = float(input("Enter x0(start): "))
maxnumit = int(input("Enter max iterations: "))

def freal(x):
    return 4.0*ln(x)-x
                                                                       
def fderi(x):
     return (4.0/x)-1.0   

def error(iterates):
    errors = []
    for y in range(1, len(iterates)):
        errors.append(abs(iterates[y] - iterates[y-1]))
        
    return errors 

def convergence(iterates):
    rates = []
    for y in range(1, len(iterates)-1):
        rates.append(np.log(abs(iterates[y+1] - iterates[y]) / abs(iterates[y] - iterates[y-1])))
    
    return rates
 
def newtonmeth(freal,fderi,x0,maxnumit):                             
    x=x0
    iterates = [x]
                                                                
    for y in range (maxnumit):                                     
        xnew = x - (freal(x)/fderi(x))
        
        x = xnew
        iterates.append(x)
    
    rates = convergence(iterates)
    print("Convergence rates: ", rates)
    errors = error(iterates)
    print("Errors for nw.meth it.: ", errors)
       
    return iterates                                               


print("Newton method iterations",newtonmeth(freal,fderi,x0,maxnumit))


X1 = float(input("Enter x1 for the secand method: "))


def secandmeth(freal,x0,x1,maxnumit):
    x=x0
    xa=x1
    iterates =[x0,x1]
    
    for y in range(maxnumit):
        xnew = xa-freal(xa)*((xa-x)/(freal(xa)-freal(x)))
        
        x = xa
        xa =xnew
        iterates.append(xa)
    
    rates = convergence(iterates)
    print("Convergence rates: ", rates)
    errors = error(iterates)
    print("Errors for sec.meth it.: ", errors)   
    return iterates 

print("Secand method iterations",secandmeth(freal,x0,X1,maxnumit))







