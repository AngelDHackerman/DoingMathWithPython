
# Draw the trajectory of a body in projectile motion

from matplotlib import pyplot as plt 
import math

def draw_graph(x, y, labels):
  for i in range(len(x)):
    plt.plot(x[i], y[i], label = labels[i])
  plt.xlabel('x-coordiante')
  plt.ylabel('y-coordiante')
  plt.title('Projectile motion of ball')
  plt.legend()


# Generate equally spaced floating point numbers between two given values

def frange(start, final, increment):
  numbers = []
  while start < final:
    numbers.append(start)
    start = start + increment

  return numbers

def calculate_trajectory(u, theta):
  theta = math.radians(theta)
  g = 9.8

  # Time to flight 
  t_flight = 2 * u * math.sin(theta) / g 
  # Find the intervals 
  intervals = frange(0, t_flight, 0.001)
  # List of x and y coordinates
  x = []
  y = []
  for t in intervals: 
    x.append(u * math.cos(theta) * t )
    y.append(u * math.sin(theta) * t - 0.5 * g * t * t)

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
