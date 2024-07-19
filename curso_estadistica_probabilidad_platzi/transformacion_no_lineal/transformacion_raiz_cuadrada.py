'''
La transformación no lineal es una técnica de preprocesamiento de datos que se utiliza para aplicar funciones no lineales a las características de los datos. 
Estas transformaciones pueden ayudar a manejar relaciones no lineales entre las características y las variables objetivo, y a mejorar el rendimiento de los modelos de machine learning.

Aplica la raíz cuadrada a las características. Es útil para datos que tienen una varianza creciente.
'''

import numpy as np

# Datos originales
data = np.array([1, 4, 9, 16])

# Transformacion de raiz cuadrada
sqrt_data = np.sqrt(data)

print(sqrt_data)

# Output: [1. 2. 3. 4.]