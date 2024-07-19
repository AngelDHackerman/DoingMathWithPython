'''
La transformación no lineal es una técnica de preprocesamiento de datos que se utiliza para aplicar funciones no lineales a las características de los datos. 
Estas transformaciones pueden ayudar a manejar relaciones no lineales entre las características y las variables objetivo, y a mejorar el rendimiento de los modelos de machine learning.

Genera nuevas características elevando las características originales a diferentes potencias y combinándolas. Esto puede capturar relaciones complejas entre las características.
'''

import numpy as np
from sklearn.preprocessing import PolynomialFeatures

# Datos originales
data = np.array([[1, 2], [3, 4], [5, 6]])

# Transformacion polinomica de grado 2
poly = PolynomialFeatures(degree=2)
poly_data = poly.fit_transform(data)

print(poly_data)
# Output: 
# [[ 1.  1.  2.  1.  2.  4.]
#  [ 1.  3.  4.  9. 12. 16.]
#  [ 1.  5.  6. 25. 30. 36.]]