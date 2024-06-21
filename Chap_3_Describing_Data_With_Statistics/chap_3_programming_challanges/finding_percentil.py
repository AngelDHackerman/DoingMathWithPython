import numpy as np

# Fucntion to find the percentil
def find_percentile(data, percentile):
  sorted_data = np.sort(data)
  index = (percentile / 100) * (len(sorted_data) - 1)
  return np.interp(index, np.arange(len(sorted_data)), sorted_data)

# Read the data file
file_path = './percentil_data.txt'
with open(file_path, 'r') as file:
  data = np.array([int(line.strip()) for line in file])

# Ask the percentil to the user
percentile = float(input("provide the percentil to calculate (0 - 100): "))

# Calcular el percentil 
percentil_value = find_percentile(data, percentile)

print(f"The corresponding value to the percentil {percentile} is: {percentil_value}")