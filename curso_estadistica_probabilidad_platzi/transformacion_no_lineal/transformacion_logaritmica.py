'''
La transformación no lineal es una técnica de preprocesamiento de datos que se utiliza para aplicar funciones no lineales a las características de los datos. 
Estas transformaciones pueden ayudar a manejar relaciones no lineales entre las características y las variables objetivo, y a mejorar el rendimiento de los modelos de machine learning.

Aplica el logaritmo natural a las características. Es útil para datos que siguen una distribución exponencial o cuando se quiere reducir la varianza de los datos.
'''

import numpy as np

# Datos originales
data = np.array([1, 10, 100, 1000])

# Tranformacion logaritmica 
log_data = np.log(data)

print(log_data)
# Output: [0.         2.30258509 4.60517019 6.90775528]