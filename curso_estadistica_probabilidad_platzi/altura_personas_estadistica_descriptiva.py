import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Generando datos de ejemplo
np.random.seed(42)
heights = np.random.normal(loc=170, scale=10, size=100)

# Cálculos de estadística descriptiva
mean_height = np.mean(heights)
median_height = np.median(heights)
std_dev_height = np.std(heights)
variance_height = np.var(heights)

print(f"Mean Height: {mean_height}")
print(f"Median Height: {median_height}")
print(f"Standard Deviation of Height: {std_dev_height}")
print(f"Variance of Height: {variance_height}")

# Visualización de los datos
plt.hist(heights, bins=20, edgecolor='black')
plt.title('Distribution of Heights')
plt.xlabel('Height (cm)')
plt.ylabel('Frequency')
plt.axvline(mean_height, color='red', linestyle='dashed', linewidth=1, label=f'Mean: {mean_height:.2f}')
plt.axvline(median_height, color='yellow', linestyle='dashed', linewidth=1, label=f'Median: {median_height:.2f}')
plt.legend()
plt.show()
