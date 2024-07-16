import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Datos de ejemplo
data = [2, 4, 4, 4, 5, 5, 7, 9]

# Crear el box plot
sns.boxplot(data=data)

# Mostrar el gráfico
plt.title("Box Plot de Datos de Ejemplo")
plt.show()
