'''
Create a generator so that the user can specify both the number and up to which multiple. 
For example, I should be able to input that I want to see a table listing the first 15 multiples of 9
'''

def multi_table(a, b):
  for i in range(1, b + 1):
    print('{0} x {1} = {2}'.format(a, i, a*i))

def get_integer_input(prompt, default=None):
  while True:
    user_input = input(prompt)
    # Si default no es None y el usuario no ingresa nada (cadena vacía), retorna default
    if default is not None and user_input == "":
      return default
    try:
      # Intenta convertir la entrada del usuario a entero
      user_input = int(user_input)
      return user_input
    except ValueError:
      # Si ocurre un error, pide al usuario que ingrese un número válido
      print("Please enter a valid integer")


if __name__ == "__main__":
  a = get_integer_input("Enter the number to multiply: ")
  b = get_integer_input("Enter the number of times to multiply (press Enter for default 10): ", default=10)

  multi_table(a, b)
