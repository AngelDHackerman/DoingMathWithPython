import matplotlib.pyplot as plt

# Datos de ejemplo
horas_estudiadas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
calificaciones = [50, 55, 60, 65, 70, 75, 80, 85, 90, 95]

# Crear el gráfico de dispersión
plt.scatter(horas_estudiadas, calificaciones)
plt.title('Relación entre horas estudiadas y calificaciones')
plt.xlabel('Horas estudiadas')
plt.ylabel('Calificaciones')
plt.show()
