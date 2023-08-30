# ada berfu kaynak 820210314
import numpy as np
from math import e
ln =np.log
import matplotlib.pyplot as plt

xi = np.array([0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10])
yi = np.array([0.72, 1.63, 1.88, 3.39, 4.02, 3.89, 4.25, 3.99, 4.68, 5.03, 5.27, 4.82, 5.67, 5.95, 5.72, 6.01, 5.5, 6.41, 5.83, 6.33])


def sum_x(xi):
    return np.sum(xi)


def sum_y(yi):
    return np.sum(yi)


def sum_squaredx(xi):
    return np.sum(xi**2)


def sum_squaredy(yi):
    return np.sum(yi**2)


def sumsquaredx(xi):
    return np.sum(xi) ** 2


def sumsquaredy(yi):
    return np.sum(yi) ** 2


def sum_xi_yi(xi, yi):
    return np.sum(xi * yi)


def linearab(xi, yi):
    i_last = len(xi)
    sum_xi = sum_x(xi)
    sum_yi = sum_y(yi)
    sum_squared_xi = sum_squaredx(xi)
    sumxoncekaresonra=sumsquaredx(xi)
    sum_xy = sum_xi_yi(xi, yi)
    assa = (i_last * sum_squared_xi) - sumxoncekaresonra 
    
    b = ((i_last * sum_xy) - (sum_xi * sum_yi)) / assa
    a = (sum_yi - (b * sum_xi)) / i_last
    print("b =", b)
    print("a =", a)
    return a, b

a, b = linearab(xi,yi)

plt.scatter(xi, yi, color='blue', label='Data points')
plt.plot(xi, a + b * xi, color='red', label='Linear regression line')
plt.xlabel('xi')
plt.ylabel('yi')
plt.title('Linear regression')
plt.legend()
plt.show()


def poli(xi, yi):
    n = len(xi)
    sum_xi = sum_x(xi)
    sum_yi = sum_y(yi)
    sum_squared_xi = sum_squaredx(xi)
    sum_xy = sum_xi_yi(xi, yi)

    c = ((n *(sum_xi**2)  * sum_yi )- sum_xi * sum_xy * sum_xi +( (sum_xi ** 3) * sum_yi )- ( (sum_xi**2)* sum_xy)) / (n * (sum_xi ** 4) - ((sum_xi**2))**2)
    d = ((n * sum_xy * sum_squared_xi) - sum_xi * sum_xi ** 2 * sum_yi  + (sum_xi ** 3) * sum_yi - sum_squared_xi * sum_xy) / (n * (sum_xi ** 4) - (sum_squared_xi)**2)
    e = (sum_yi - c * sum_squared_xi - d * sum_xi) / n

    print("c =", c)
    print("d =", d)
    print("e =", e)
    
    return c, d, e

c, d, e = poli(xi, yi)

# Define x values to plot the function
x = np.linspace(0.5, 10, 100)

# Calculate y values for the quadratic function
y = c * x**2 + d * x + e

# Plot the function
plt.plot(x, y)
plt.scatter(xi, yi)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Quadratic Function')
plt.show()
   


def fonklog(xi, yi):
    i_last = len(xi)
    sum_ln_x = np.sum(ln(xi))
    sumy = sum_y(yi)
    sum_ln_x_squared = np.sum(ln(xi)**2)
    sum_ln_x_y = sum_xi_yi(ln(xi), yi)
    
    m = (i_last * sum_ln_x_y - sum_ln_x * sumy) / (i_last * sum_ln_x_squared - sum_ln_x ** 2)
    k = (sumy - m * sum_ln_x) / i_last
    print("k =", k)
    print("m =", m)
    return m, k

k,m = fonklog(xi,yi)

x = np.linspace(0.5, 10, 100)

# Calculate y values for the quadratic function
y =k+m*np.log(x)


plt.plot(x, y)
plt.scatter(xi, yi)
plt.xlabel('x')
plt.ylabel('y')
plt.title('log Function')
plt.show()

    
