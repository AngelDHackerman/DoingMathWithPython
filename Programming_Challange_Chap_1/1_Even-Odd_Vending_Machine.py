'''
Challange 1:

Print whether the input is even or odd. If even, print the next 9 even numbers
If odd, print the next 9 odd numbers.

if number is 2 (even) then it should display: 2, 4, 6, 8, 10, 12, 14, 16, 18, 20.
if number is 1 (odd) then it should display: 1, 3, 5, 7, 9, 11, 13, 15, 17, 19.

your program should use the is_integer() method to display an error message if the input is a number
with significant digits beyond the decimal point. 
'''

def get_integer_input(prompt):
  while True:
    try:
      # convert the input to a float
      user_input = float(input(prompt))

      # check if the float is an integer
      if user_input.is_integer():
        return int(user_input)
      else:
        print("Please enter an integer")
    except ValueError:
      print("Please enter a valid number.")

def even_odd_vending(num):
  if (num % 2) == 0:
    print(f"{num} is even.")
  else:
    print(f"{num} is odd")

  count =1 
  while count <= 9:
    num += 2
    print(num)
    count += 1

if __name__ == "__main__":
  while True:
    num = get_integer_input("Enter an integer: ")
    even_odd_vending(num)

    cont = input('Do you want to perform another conversation? (yes/y/no): ').lower()
    if cont not in ('yes', 'y'):
      print('Goodbye')
      break