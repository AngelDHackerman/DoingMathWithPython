

# todo: TERMINAR DE entender los pasos que se siguen para ver la formula de el factor de correlation (la formula dibujada en el libro)

def find_corr_x_y(x, y):
  n = len(x)

  # Encuentra el producto de los pares de valores y suma los productos
  prod = []
  for xi, yi in zip(x, y):
    prod.append(xi * yi)
  sum_prod_x_y = sum(prod)

  # Suma de x y y
  sum_x = sum(x)
  sum_y = sum(y)
  
  # Suma de los cuadrados de las sumas de x y y
  squared_sum_x = sum_x**2
  squared_sum_y = sum_y**2

  # Suma de los cuadrados de cada elemento en x
  x_square = []
  for xi in x:
    x_square.append(xi**2)
  x_square_sum = sum(x_square)

  # Suma de los cuadrados de cada elemento en y
  y_square = []
  for yi in y:
    y_square.append(yi**2)
  y_square_sum = sum(y_square)

  # Calcula el numerador de la fórmula del coeficiente de correlación
  numerator = n * sum_prod_x_y - sum_x * sum_y

  # Calcula los términos del denominador
  denominator_term1 = n * x_square_sum - squared_sum_x
  denominator_term2 = n * y_square_sum - squared_sum_y
  denominator = (denominator_term1 * denominator_term2)**0.5

  # Calcula el coeficiente de correlación
  correlation = numerator / denominator

  return correlation
