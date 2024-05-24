'''
Create a calculator that can handle basic fraction operations
'''

from fractions import Fraction

def add(a, b):
  print('Result of Addition: {0}'.format(a + b))

def subtract(a, b):
  print('Result of subtraction: {0}'.format(a - b))

def multiply(a, b):
  print('Result of Multiplication: {0}'.format(a * b))

def divide(a, b):
  if b != 0:
    print('Result of Division: {0}'.format(a / b))
  else:
    print('Error: Division by zero is not allowed.')

if __name__ == "__main__":
  a = Fraction(input('Enter the first fraction: '))
  b = Fraction(input('Enter the second fraction: '))
  op = input('Operation to perform - Add, Subtract, Divide, Multiply: ')

  if op == 'Add':
    add(a, b)
  elif op == 'Substract':
    subtract(a, b)
  elif op == 'Divide':
    divide(a, b)
  elif op == 'Multiply':
    multiply(a, b)
  else: 
    print('Invalid operation. Please selec Add, Subtract, Divide or Multiply.')