
# Calculating the mode

from collections import Counter

def calculate_mode(numbers):
  c = Counter(numbers)
  mode = c.most_common(1)
  mode, frequency = mode[0][0], mode[0][1]
  return mode, frequency


if __name__ == "__main__":
  scores = [7, 8, 9, 2, 10, 9, 9, 9, 4, 5, 6, 7, 8, 6, 1, 10]
  mode, frequency = calculate_mode(scores)

  print('The mode of the list of numbers is: {0}, it appears {1} times'.format(mode, frequency))
