
# The script below finds the coefficient correlation of 2 array variables 
# this code checks if the 2 variables x & y have the same lenght 

def calculate_mean(numbers):
  return sum(numbers) / len(numbers)

def calculate_correlation(x, y):
  # Validate that both list have the same lenght
  if len(x) != len(y):
    print('Error: the arrays "x" and "y" does not have the same lenght, it is not posible to calculate the correlation')
    return None
  
  mean_x = calculate_mean(x)
  mean_y = calculate_mean(y)

  numerator = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip (x, y))
  denominator_x = sum((xi - mean_x)**2 for xi in x)
  denominator_y = sum((yi - mean_y)**2 for yi in y)

  denominator = (denominator_x * denominator_y) ** 0.5

  correlation = numerator / denominator
  return correlation

if __name__ == "__main__":
  x = [10, 20, 30, 40, 50, 60]
  y = [10, 20, 30, 40, 50, 60]
  correlation = calculate_correlation(x, y)
  if correlation is not None:
    print("the correlation coefficient is: ", correlation)
