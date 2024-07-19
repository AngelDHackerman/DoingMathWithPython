import numpy as np
from sklearn.preprocessing import MinMaxScaler

# Supongamos que tenemos un array de datos
data = np.array([[20], [30], [40], [50], [60], [70]])

# creamos un scaler min-max 
scaler = MinMaxScaler()

# Ajustamos el scaler a los datos y transformamos los datos
scaled_data = scaler.fit_transform(data)

print(scaled_data)