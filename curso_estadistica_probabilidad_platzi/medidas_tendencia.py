import pandas as pd
import matplotlib.pyplot as plt

# Crear un DataFrame de ejemplo
data = {'values': [1, 2, 2, 3, 4, 4, 4, 5, 6, 7, 8, 8, 9]}
df = pd.DataFrame(data)

# Calcular la media
media = df['values'].mean()

# Calcular la mediana
mediana = df['values'].median()

# Calcular la moda
moda = df['values'].mode()[0]  # Tomamos el primer valor de la moda en caso de multimodalidad

# Mostrar los resultados
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")

# Crear un histograma de los valores con bins definidos manualmente
plt.hist(df['values'], bins=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], alpha=0.5, edgecolor='black')

# Añadir líneas para la media, mediana y moda
plt.axvline(media, color='blue', linestyle='dashed', linewidth=2, label=f'Media: {media}')
plt.axvline(mediana, color='red', linestyle='dashed', linewidth=2, label=f'Mediana: {mediana}')
plt.axvline(moda, color='green', linestyle='dashed', linewidth=2, label=f'Moda: {moda}')

# Agregar leyenda
plt.legend()

# Mostrar el gráfico
plt.title('Histograma de los Valores')
plt.xlabel('Valores')
plt.ylabel('Frecuencia')
plt.show()
