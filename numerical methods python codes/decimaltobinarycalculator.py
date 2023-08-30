#decimal to binary calculator

dec=int(input('numbers before the dot: '))
no_folat = float(input('numbers after the dot(example:0.1// 0.65// 0.5...): '))

def dectobin(dec):
    if dec >= 1:
        dectobin(dec//2)
        dec=dec % 2
    elif dec<0:
        dec=bin(dec)                      
print(dec,end=" ")    
dectobin(dec)
print(".",end=" ")      
def ada(no_folat):    
    while no_folat >0 and no_folat < 2:
        no_folat=no_folat*2
        if no_folat >= 1:
            print('1',end=" ")
            no_folat= no_folat-1
        else:
            print('0',end=" ")          
    if no_folat<0:
        no_folat=bin(no_folat)    
ada(no_folat)