
# Frequency table for a list of numbers 
# Enhanced to display the table sorted by the numbers

from collections import Counter

def frequency_table(numbers):
  table = Counter(numbers)
  numbers_freq = table.most_common()
  # print(numbers_freq)
  numbers_freq.sort()
  # print(numbers_freq)

  print('Number\tFrenquency')
  for number in numbers_freq:
    print('{0}\t{1}'.format(number[0], number[1]))


if __name__ == "__main__":
  score = [7, 8, 9, 2, 10, 9, 9, 9, 4, 5, 6, 1, 5, 9, 6, 7, 8, 6, 1, 10]
  frequency_table(score)