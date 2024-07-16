import matplotlib.pyplot as plt

# Datos de ejemplo
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

# Crear el diagrama de dispersión
plt.scatter(x, y)

# Añadir etiquetas y título
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.title('Diagrama de Dispersión de Ejemplo')

# Mostrar el gráfico
plt.show()
