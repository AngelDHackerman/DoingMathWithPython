
# Draw the trajectory of a body in projectile motion

from matplotlib import pyplot as plt 
import math

def draw_graph(x, y):
  plt.plot(x, y)
  plt.xlabel('x-coordiante')
  plt.ylabel('y-coordiante')
  plt.title('Projectile motion of ball')


# Generate equally spaced floating point numbers between two given values

def frange(start, final, increment):
  numbers = []
  while start < final:
    numbers.append(start)
    start = start + increment

  return numbers

def draw_trajectory(u, theta):
  theta = math.radians(theta) # converst from degrees to radians
  g = 9.8

  # Time of flight 
  t_flight = 2*u*math.sin(theta)/g
  # Find the intervals
  intervals = frange(0, t_flight, 0.001)
  # List of x and y coordiantes
  x = []
  y = []
  for t in intervals:
    x.append(u*math.cos(theta)*t)
    y.append(u*math.sin(theta)*t - 0.5*g*t*t) # 0.5*g*t*t, this represents the fall of the projectil due to gravety

  draw_graph(x, y)


if __name__ == "__main__":
  try:
    u = float(input('Enter the initial velocity (m/s): '))
    theta = float(input('Enter the angle of projection (degrees): '))
  except ValueError:
    print('You entered an invalid input')
  else:
    draw_trajectory(u, theta)
    plt.show()