import pandas as pd 
import matplotlib.pyplot as plt

# crear un dataframe de ejemplo
data = {'values': [1, 2, 2, 3, 4, 4, 4, 5, 6, 7, 8, 8, 9]}
df = pd.DataFrame(data)

# Calcular la media 
media = df['values'].mean()

# Calcular la mediana 
mediana = df['values'].median()

# Calcular la moda 
moda = df['values'].mode()

# Mostrar los resultados
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")
