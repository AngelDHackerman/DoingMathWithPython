# This script resolves quadratic functions and displays visualy how they looks like

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Definir los valores de x
x_values = np.array([-1, 1, 2, 3, 4, 5])

# Calcular los valores de y
y_values = x_values**2 + 2*x_values + 1

# Crear un DataFrame para almacenar los resultados
data = pd.DataFrame({'x': x_values, 'y': y_values})

# Graficar los resultados
plt.figure(figsize=(10, 6))
plt.plot(data['x'], data['y'], marker='o', linestyle='-', color='b')
plt.title('Quadratic Function y = x^2 + 2x + 1')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()
