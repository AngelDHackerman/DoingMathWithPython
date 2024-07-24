# Crea una columna binaria para cada categoría.

from sklearn.preprocessing import OneHotEncoder
import numpy as np

encoder = OneHotEncoder(sparse=False)
data = np.array([['red'], ['blue'], ['green']])
encoded_data = encoder.fit_transform(data)
