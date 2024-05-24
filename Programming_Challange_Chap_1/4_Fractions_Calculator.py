'''
Create a calculator that can handle basic fraction operations
'''

from fractions import Fraction

def add(a, b):
    print('Result of Addition: {0}'.format(a + b))

def subtract(a, b):
    print('Result of Subtraction: {0}'.format(a - b))

def multiply(a, b):
    print('Result of Multiplication: {0}'.format(a * b))

def divide(a, b):
    if b != 0:
        print('Result of Division: {0}'.format(a / b))
    else:
        print('Error: Division by zero is not allowed.')

if __name__ == "__main__":
    while True:
        a = Fraction(input('Enter the first fraction: '))
        b = Fraction(input('Enter the second fraction: '))
        op = input('Operation to perform - Add, Subtract, Divide, Multiply: ').lower()
        
        if op == 'add':
            add(a, b)
        elif op == 'subtract':
            subtract(a, b)
        elif op == 'multiply':
            multiply(a, b)
        elif op == 'divide':
            divide(a, b)
        else:
            print('Invalid operation. Please select Add, Subtract, Divide, or Multiply.')
        
        cont = input('Do you want to perform another operation? (yes/no): ').lower()
        if cont not in ('yes', 'y'):
            print('Goodbye!')
            break