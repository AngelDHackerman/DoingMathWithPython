import scipy.stats as stats
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Generando datos de ejemplo
np.random.seed(42)
sample_income = np.random.normal(loc=50000, scale=15000, size=100)

# Intervalo de confianza para la media
confidence_level = 0.95 # define el nivel de confianza para el intervalo de confianza. Un nivel de confianza del 95% significa que, si repetimos este proceso muchas veces, el 95% de los intervalos de confianza calculados contendrá la media verdadera de la población.
degrees_freedom = len(sample_income) - 1 # Los grados de libertad se calculan como el tamaño de la muestra menos uno (n - 1). Se utilizan en la distribución t de Student, que es apropiada para muestras pequeñas.
sample_mean = np.mean(sample_income) 
sample_std_err = stats.sem(sample_income) # calcula el error estándar de la media de la muestra. El error estándar mide la precisión con la que la media muestral estima la media de la población.
confidence_interval = stats.t.interval(confidence_level, degrees_freedom, sample_mean, sample_std_err) # calcula el intervalo de confianza para la media poblacional usando la distribución t de Student.

print(f"Sample Mean Income: {sample_mean}")
print(f"95% Confidence Interval for Mean Income: {confidence_interval}")
