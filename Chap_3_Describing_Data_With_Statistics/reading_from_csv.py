
import csv
import matplotlib.pyplot as plt

def scatter_plot(x, y):
  plt.scatter(x, y)
  plt.xlabel('Number')
  plt.ylabel('Squared')
  plt.show()

def read_csv(filename):
  numbers = []
  squared = []
  with open(filename) as f:
    reader = csv.reader(f) # crea un objeto iterable capaz de leer archivos CSV.
    next(reader) # salta la primera linea del archivo, (evita los headers: number, squared)
    for row in reader:
      numbers.append(int(row[0]))
      squared.append(int(row[1]))
    return numbers, squared
  
if __name__ == "__main__":
  numbers, squared = read_csv('./numbers.csv')
  scatter_plot(numbers, squared)