
# takes a list of numbers in the file mydata.txt and then calculates and prints their
# mean, median, mode, variance and standard deviation.

import math
import statistics

def read_data(file_path):
  with open(file_path, 'r') as file:
    data = [int(line.strip()) for line in file]
  return data

def calculate_statistics(data):
  mean = statistics.mean(data)
  median = statistics.median(data)
  mode = statistics.mode(data)
  variance = statistics.variance(data)
  std_dev = statistics.stdev(data)

  return mean, median, mode, variance, std_dev

if __name__ == "__main__":
  file_path = "../mydata.txt"
  data = read_data(file_path)

  mean, median, mode, variance, std_dev = calculate_statistics(data)

  print(f"Mean: {mean}")
  print(f"Median: {median}")
  print(f"Mode: {mode}")
  print(f"Varian: {variance}")
  print(f"Standard Deviation: {std_dev}")


