import numpy as np

# Datos originales
data = np.array([1, 10, 100, 1000])

# Tranformacion logaritmica 
log_data = np.log(data)

print(log_data)
# Output: [0.         2.30258509 4.60517019 6.90775528]