#bisectionmethod
a=float(input('enter the number that you want to find is equal:   ')) #input taker
e=float(input('enter the stopper(error %):  ')) #input taker,
x=0.0
def bisectionmeth(a,e,x):
    if a**(1/5)-x<=e:
        x=a**(1/5)
        print('our root is %0.10f' %x)
    else:
        while a**(1/5)-x>e:
            x=a+0/2
            if a**(1/5)-x<=e:
                x=-((e/100)*(a**(1/5))-a**(1/5))
    print('our root is %0.10f' %x)

bisectionmeth(a,e,x)              

    
a=float(input('enter the number that you want to find is equal:   ')) #input taker
e=float(input('enter the stopper(error %):  ')) #input taker,

         
        
            
            
         
              
      
    
    
    

      