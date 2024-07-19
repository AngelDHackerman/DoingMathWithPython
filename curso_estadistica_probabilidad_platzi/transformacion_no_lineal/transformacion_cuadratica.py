'''
La transformación no lineal es una técnica de preprocesamiento de datos que se utiliza para aplicar funciones no lineales a las características de los datos. 
Estas transformaciones pueden ayudar a manejar relaciones no lineales entre las características y las variables objetivo, y a mejorar el rendimiento de los modelos de machine learning.

Eleva las características al cuadrado. Es útil para capturar relaciones cuadráticas entre las características y la variable objetivo.
'''
import numpy as np

# Datos originales
data = np.array([1, 2, 3, 4])

# Transformacion cuadratica
square_data = np.power(data, 2)

print(square_data)
# Output: [ 1  4  9 16]

