'''
you can experiment with numerous interesting data sources freely available on the internet.
the webiste http://www.quandl.com/ is one such source. For this challange, download the following dat as a CVS file from
http://www.quandl.com/WORLDBANK/USA_SP_POP_TOTL/: the total population of the united states at the end 
of each year for the years 1969 to 2012. then calculate the mean, median, variance, and standard deviation of the difference in 
population over the years and create a graph showing these differences. 
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Create doomy data of population
years = np.arange(1969, 2013)
population = np.random.randint(200_000_000, 330_000_000, size=len(years))

# Create a dataframe with the data
data = pd.DataFrame({'Year': years, 'Population': population})

# Save the dataframe in a CSV file
data.to_csv('simulated_population_data.csv', index=False)


# Step 2: Calculate the differences between years, adds the 'Population_Difference' column to the data frame
data['Population_Difference'] = data['Population'].diff().fillna(0) # .diff() es un metodo de pandas que calcula la diferencia entre un valor y otro de data['Population']

# Calculate statistics of the differences
mean_diff = data['Population_Difference'].mean()
median_diff = data['Population_Difference'].median()
variance_diff = data['Population_Difference'].var()
std_dev_diff = data['Population_Difference'].std()

print(f"Mean of Population Differences: {mean_diff}")
print(f"Median of Population Differences: {median_diff}")
print(f"Variance of Population Differences: {variance_diff}")
print(f"Standard Deviation of Population Differences: {std_dev_diff}")


# Step 3: Crear el grafico de las diferencias de poblacion
plt.figure(figsize=(10, 6))
plt.plot(data['Year'], data['Population_Difference'], marker='o', linestyle='-', color='b')
plt.title('Yearly Population Differences in the United States (Simulated Data)')
plt.xlabel('Year')
plt.ylabel('Population Difference')
plt.grid(True)
plt.show()