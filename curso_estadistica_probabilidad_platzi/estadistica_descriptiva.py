

    # ESTUDIAR ESTE CODIGO CON CHAT-GPT

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Generar datos de ejemplo
np.random.seed(42)
data = pd.DataFrame({
    'sales': np.random.normal(loc=200, scale=50, size=100),
    'marketing_spend': np.random.normal(loc=5000, scale=1000, size=100),
    'region': np.random.choice(['North', 'South', 'East', 'West'], size=100)
})

# Estadísticas descriptivas
print(data.describe())

# Visualización de datos
sns.histplot(data['sales'], kde=True)
plt.title('Distribution of Sales')
plt.xlabel('Sales')
plt.ylabel('Frequency')
plt.show()

# Análisis de correlación
correlation = data['sales'].corr(data['marketing_spend'])
print(f"Correlation between sales and marketing spend: {correlation}")

# Prueba de hipótesis (Prueba t para una muestra)
t_stat, p_value = stats.ttest_1samp(data['sales'], 200)
print(f"T-statistic: {t_stat}, P-value: {p_value}")
