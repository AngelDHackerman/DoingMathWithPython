# This script resolves quadratic functions and displays visualy how they looks like

import matplotlib.pyplot as plt 

# define a range of values for x 
x_values  = list(range(-5, 6))  # values from -5 to 5

# calculate the values of y
y_values = [x**2 + 2*x + 1 for x in x_values]

# Graficar los resultados
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, marker='o', linestyle='-', color='b')
plt.title('Quadratic Function y = x^2 + 2x + 1')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()