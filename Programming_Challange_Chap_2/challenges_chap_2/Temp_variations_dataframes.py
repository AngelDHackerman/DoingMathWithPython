import pandas as pd
import matplotlib.pyplot as plt 

# Fake data for Guatemala city
data_guatemala = {
  'Time of Day': ['12:00 AM', '3:00 AM', '6:00 AM', '9:00 AM', '12:00 PM', '3:00 PM', '6:00 PM', '9:00 PM'],
  'Temperature (°C)': [17, 16, 15, 18, 23, 25, 22, 19]
}

# Fake data for Xelaju city
data_xela = { 
  'Time of Day': ['12:00 AM', '3:00 AM', '6:00 AM', '9:00 AM', '12:00 PM', '3:00 PM', '6:00 PM', '9:00 PM'],
    'Temperature (°C)': [5, 4, 5, 10, 18, 20, 15, 10]
}

# Convert to dataframes
df_guatemala = pd.DataFrame(data_guatemala)
df_xela = pd.DataFrame(data_xela)

# print(df_guatemala)
# print(df_xela)

# set the graphic
plt.figure(figsize=(12, 8)) # 12" x 8"

# Add lines of temperature using dataframes
plt.plot(df_guatemala['Time of Day'], df_guatemala['Temperature (°C)'], marker='o', label='Guatemala City', color='orange')
plt.plot(df_xela['Time of Day'], df_xela['Temperature (°C)'], marker='o', label='Xela city', color='blue')

# Adjust the limits of graphic
plt.axis([0, 7, 0, 30]) # [xmin, xmax, ymin, ymax]

# Add Details
plt.title('Temperature variation comparison: Guatemala City Vs Xela')
plt.xlabel('Time of Day')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()

# show the graphic
plt.show()