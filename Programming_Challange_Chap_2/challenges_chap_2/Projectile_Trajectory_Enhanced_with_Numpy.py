# Draw the trajectory of a body in projectile motion (using numpy)

import numpy as np
from matplotlib import pyplot as plt 

def draw_graph(x, y, labels):
  print(f'Array use to calculate the trajectory of X {x}')
  print(f'Array use to calculate the trajectory of Y {y}')
  print(labels)

  for i in range(len(x)):
    plt.plot(x[i], y[i], label=labels[i])
  plt.xlabel('x-coordinate')
  plt.ylabel('y-coordinate')
  plt.title('Projectile motion of ball')
  plt.legend()

def calculate_trajectory(u, theta): 
  theta = np.radians(theta)
  g = 9.8

  # Time to flight 
  t_flight = 2 * u * np.sin(theta) / g
  # Generate intervals using numpy
  t = np.arange(0, t_flight, 0.001)

  # Calculate x and y coordiantes using numpy arrays
  x = u * np.cos(theta) * t
  y = u * np.sin(theta) * t - 0.5 * g * t**2

  return x, y

def draw_trajectory(num_trajectories, velocities, angles):
  all_x = []
  all_y = []
  labels = []

  for i in range(num_trajectories):
    u = velocities[i]
    theta = angles[i]
    x, y = calculate_trajectory(u, theta)
    all_x.append(x)
    all_y.append(y)
    labels.append(f'Trajectory {i + 1}')

  draw_graph(all_x, all_y, labels)


if __name__ == "__main__":
  try: 
    num_trajectories = int(input('How many trajectories? '))
    velocities = []
    angles = []

    for i in range(num_trajectories):
      u = float(input(f'Enter the initial velocity for trajectory {i + 1} (m/s): '))
      theta = float(input(f'Enter the angle of projection for trajectory {i + 1} (degrees): '))
      velocities.append(u)
      angles.append(theta)

  except ValueError:
    print('You entered an invalid input')
  else:
    draw_trajectory(num_trajectories, velocities, angles)
    plt.show()