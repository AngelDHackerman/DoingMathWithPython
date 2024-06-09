
# Exploring relationship between Fibonacci numbers and golder ratio

import matplotlib.pyplot as plt

def fibo(n):
  if n == 1:
    return [1]
  if n == 2:
    return [1, 1]

  # n > 2 
  a, b = 1, 1
  # First two members of the series 
  series = [a, b]
  for _ in range(n - 2):
    c = a + b
    series.append(c)
    a, b = b, c 

  return series

def calculate_ratios(fibonacci_series):
  ratios = []
  for i in range(1, len(fibonacci_series)):
    ratio = fibonacci_series[i] / fibonacci_series[i - 1]
    ratios.append(ratio)
  return ratios

def plot_ratios(ratios):
  plt.figure(figsize=(10, 5))
  plt.plot(ratios, marker='o', linestyle='-', color='black')
  plt.axhline(y=1.61803398875, color='r', linestyle='--', label='Golder Ratio')
  plt.xlabel('Number of Fibonacci Terms')
  plt.ylabel('Ratio')
  plt.title('Ratios between consecutive Fibonacci numbers')
  plt.legend()
  plt.show()

if __name__ == "__main__":
  num_terms = 100 # Generate the first 100th terms
  fibonacci_series = fibo(num_terms)
  ratios = calculate_ratios(fibonacci_series)
  plot_ratios(ratios)

