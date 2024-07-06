import scipy.stats as stats
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Generando datos de ejemplo
np.random.seed(42)
sample_income = np.random.normal(loc=50000, scale=15000, size=100)

# Intervalo de confianza para la media
confidence_level = 0.95
degrees_freedom = len(sample_income) - 1
sample_mean = np.mean(sample_income)
sample_std_err = stats.sem(sample_income)
confidence_interval = stats.t.interval(confidence_level, degrees_freedom, sample_mean, sample_std_err)

print(f"Sample Mean Income: {sample_mean}")
print(f"95% Confidence Interval for Mean Income: {confidence_interval}")
