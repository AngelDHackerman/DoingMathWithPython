import numpy as np

# Array de datos con valores extremos
data = np.array([1, 2, 3, 100, 200, 300])

# Clipping al rango [0, 100]
clipped_data = np.clip(data, 0, 100)

print(clipped_data)
# Output: [ 1 2 3 100 100 100]