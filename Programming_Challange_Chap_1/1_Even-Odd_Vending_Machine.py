'''
Challange 1:

Print whether the input is even or odd. If even, print the next 9 even numbers
If odd, print the next 9 odd numbers.

if number is 2 (even) then it should display: 2, 4, 6, 8, 10, 12, 14, 16, 18, 20.
if number is 1 (odd) then it should display: 1, 3, 5, 7, 9, 11, 13, 15, 17, 19.

your program should use the is_integer() method to display an error message if the input is a number
with significant digits beyond the decimal point. 
'''

def is_integer(prompt):
    while True:
        try:
            user_input = input(prompt)
            # Convert the input to an integer
            user_input_int = int(user_input)
            # Check if the input is a float
            if float(user_input) != user_input_int:
                raise ValueError("Input is a float number.")
            return user_input_int
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid integer.")

def even_odd_vending(num):
  if (num % 2) == 0:
    print(num)
  else:
    print(num)

  count = 1
  while count <= 9:
    num += 2
    print(num)
    count += 1

def get_integer_input(prompt):
  while True:
    try:
      user_input = float(input(prompt))
      
      if user_input.is_integer():
        return int(user_input)
      else: 
        print("Please enter an integer.")
    except ValueError:
      print("Please enter a valid number.")

if __name__ == "__main__":
  num = get_integer_input("Enter an integer: ")
  even_odd_vending(num)