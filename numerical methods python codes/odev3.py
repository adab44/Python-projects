

import matplotlib.pyplot as plt
import numpy as np

x = [0, 1, 2, 4, 6]
fx = [1, 9, 23, 93, 259]

xtest = 4.2  # for part c

def div_dif(x, fx):
    n = len(x)
    diftable = [[0] * n for x in range(n)]
    for i in range(n):
        diftable[i][0] = fx[i]

    for j in range(1, n):
        for i in range(n - j):
            diftable[i][j] = (diftable[i + 1][j - 1] - diftable[i][j - 1]) / (x[i + j] - x[i])

    return diftable

def interpolation(x, fx, a):
    n = len(x)
    diff_table = div_dif(x, fx)
    result = diff_table[0][0]
    x_new = 1

    for i in range(1, n):
        x_new *= (a - x[i - 1])
        result += diff_table[0][i] * x_new

    return result

a = div_dif(x, fx)

for row in a:
    for i in row:
        print(f"{i}\t", end='')
    print()

interpolation_value = interpolation(x, fx, xtest)
print(f"div. diff. value at x = {xtest}: {interpolation_value}")

# Plotting the interpolated function
x_values = np.linspace(min(x), max(x), 100)
y_values = [interpolation(x, fx, x_val) for x_val in x_values]

plt.plot(x, fx, 'bo', label='Data Points')
plt.plot(x_values, y_values, 'r-', label='Function')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Interpolation')
plt.legend()
plt.grid(True)
plt.show()

for row in a:
    for i in row:
        print(f"{i}\t", end='')
    print()

interpolation_value = interpolation(x, fx, xtest)
print(f" div. diff. value at x = {xtest}: {interpolation_value}")