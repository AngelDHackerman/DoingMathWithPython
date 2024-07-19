from scipy.stats.mstats import winsorize
import numpy as np

# Array de datos con valores extremos
data = np.array([1, 2, 3, 100, 200, 300])

# winsorizing al 5% y 95%
winsorize_data = winsorize(data, limits=[0.05, 0.05])

print(winsorize_data)
# Output: [ 1 2 3 100 100 100 ]