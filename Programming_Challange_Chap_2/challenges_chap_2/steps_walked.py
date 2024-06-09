'''
Example of drawing a horizontal bar chart
'''

import matplotlib.pyplot as plt

def create_bar_chart(data, labels):
  # Number of bars
  num_bars = len(data)
  # this list is the point on the y-axis where each 
  # bar is centered. Here it will be [1, 2, 3...]
  positions = range(1, num_bars+1)
  plt.barh(positions, data, align= 'center')
  # set the label of each bar 
  plt.yticks(positions, data)
  plt.xlabel('Steps')
  plt.ylabel('Day')
  plt.title('Number of steps walked')
  # Turns on the grid which may assist visual estimation 
  plt.grid()
  plt.show()

if __name__ == "__main__":
  # Number of steps I walked during the past week 
  steps = [6534, 7000, 8900, 10786, 3467, 11045, 5095]
  # corresponding days
  labels = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
  create_bar_chart(steps, labels)