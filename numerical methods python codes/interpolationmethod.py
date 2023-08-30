#interpolation method
import numpy as np
import matplotlib.pyplot as plt

x = np.array([-2, 0, 1, 3])
y = np.array([-27, -1, 0, 1])

def lagrange_int(x, y, x_interpolate):
    uz = len(x)
    interpolatedy = np.zeros_like(x_interpolate)
    
    for i in range(uz):
        pay = 1
        payda = 1
        for j in range(uz):
            if j != i:
                pay *= (x_interpolate - x[j])
                payda *= (x[i] - x[j])
        
        interpolatedy += y[i] * (pay / payda)
    
    return interpolatedy


x_interpolate = np.linspace(-2, 2, 100)  
y_interpolate = lagrange_int(x, y, x_interpolate)

plt.figure(figsize=(10, 5))
plt.plot(x, y, 'ro', label='Data Points')
plt.plot(x_interpolate, y_interpolate, 'b-', label='Curve')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Lagrange Interpolation')
plt.legend()
plt.grid(True)
plt.show()


x_interp = 3.0 #value that we want to find !!

def lagrange_int_1(x, y, x_interp):
    uz = len(x)
    y_interp = 0.0
    
    for i in range(uz):
        formula = 1.0
        for j in range(uz):
            if i != j:
                formula *= (x_interp - x[j]) / (x[i] - x[j])
        y_interp += y[i] * formula

    return y_interp

y_interp = lagrange_int_1(x, y, x_interp)



print(f"Interpolated y when x = {x_interp} is {y_interp}")
