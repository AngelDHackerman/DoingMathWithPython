import numpy as np
import time

# Array grande
x_values = np.arange(1e6)

# Con numpy (vectorizado)
start_time = time.time()
y_values_numpy = x_values**2 + 2*x_values + 1
end_time = time.time()
print("Tiempo con numpy: ", end_time - start_time)

# Con bucle for tradicional
x_values = list(range(int(1e6)))
start_time = time.time()
y_values_loop = []
for x in x_values:
    y_values_loop.append(x**2 + 2*x + 1)
end_time = time.time()
print("Tiempo con bucle for: ", end_time - start_time)
