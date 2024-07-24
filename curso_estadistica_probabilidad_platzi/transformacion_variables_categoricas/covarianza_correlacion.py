import numpy as np
import pandas as pd

# Datos de ejemplo 
data = {
  'X': [1, 2, 3, 4, 5],
  'Y': [2, 4, 5, 4, 5]
}

df = pd.DataFrame(data)

# Calcular la covarianza 
cov_matrix = np.cov(df['X'], df['Y'])
cov_XY = cov_matrix[0, 1]
print(f"Covarianza entre X y Y: {cov_XY}")

# Calcular la correlacion de Pearson
corr_matrix = np.corrcoef(df['X'], df['Y'])
corr_XY = corr_matrix[0, 1]
print(f"Correlacion entre X y Y: {corr_XY}")