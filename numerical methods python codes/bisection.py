number = input("Enter a rational number:")

def rationaln_to_binaryn(num):
    integer = int(num)
    fractional = (num- integer)


    binary_int = bin(integer)[2:]

   
    binary = ""
    while fractional> 0:
       
        fractional *= 2

       
        if fractional >= 1:
            binary += "1"
            fractional -= 1
        
        else:
            binary += "0"
            binary = format(integer) + "." + binary
print(rationaln_to_binaryn(200))