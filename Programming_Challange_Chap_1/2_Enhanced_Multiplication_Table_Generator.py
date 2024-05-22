'''
Create a generator so that the user can specify both the number and up to which multiple. 
For example, I should be able to input that I want to see a table listing the first 15 multiples of 9
'''

def multi_table(a, b):
  for i in range(1, b +1):
    print('{0} x {1} = {2}'.format(a, i, a*i))

if __name__ == "__main__":
  a = int(input("Enter the number to multiple: "))
  b = int(input("Enter the number of times to multiple: "))

  multi_table(a, b)
