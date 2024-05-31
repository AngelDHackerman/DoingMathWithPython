# Comparing temperatures using arrays

import matplotlib.pyplot as plt
import pandas as pd

# fake data for guatemala city
time_guatemala = ['12:00 AM', '3:00 AM', '6:00 AM', '9:00 AM', '12:00 PM', '3:00 PM', '6:00 PM', '9:00 PM']
temp_guatemala = [17, 16, 15, 18, 23, 25, 22, 19]

# fake data for Xela city 
time_xela = ['12:00 AM', '3:00 AM', '6:00 AM', '9:00 AM', '12:00 PM', '3:00 PM', '6:00 PM', '9:00 PM']
temp_xela = [5, 4, 5, 10, 18, 20, 15, 10]

# set the graphic

plt.figure(figsize=(12, 8)) # 12" x 8"

plt.plot(time_guatemala, temp_guatemala, marker='o', label='Guatemala City', color='orange')
plt.plot(time_xela, temp_xela, marker='o', label='Xela', color='blue')

# adjust the limits of the graphic

plt.axis([0, 7, 0, 30]) # [xmin, xmax, ymin, ymax]

plt.title('Temperature variation comparison: Guatemala city vs Xela city')
plt.xlabel('Time of Day')
plt.ylabel('Temperature (°C)')
plt.grid(True) # shows a grid in the figure
plt.xticks(rotation=45) # rotation for the tags in the x axis
plt.legend()
plt.tight_layout() 

plt.show()