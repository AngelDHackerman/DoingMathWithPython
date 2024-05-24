'''
Create a unit converter that not only can converte miles to kilometers and viceversa
add the conversion of mass such as: kilograms and pounds, celsius and Fahrenheit. 
'''

def print_menu():
  print('1. Kilometers to Miles')
  print('2. Miles to Kilometers')
  print('3. Kilograms to pounds')
  print('4. Pounds to Kilograms')
  print('5. Celcius to Fahrenheit')
  print('6. Fahrenheit to Celcius')

def km_miles():
  km = float(input('Enter distance in kilometers: '))
  miles = km / 1.609

  print('Distance in miles: {0}.'.format(miles))

def miles_km():
  miles = float(input('Enter distance in miles: '))
  km = miles * 1.609

  print('Distance in kilometers: {0}'.format(km))

def kilo_Pound():
  kilogram = float(input('Enter number of kilograms: '))
  pound = kilogram * 2.205

  print('Weight in pounds is: {0}'.format(pound))

def pound_kilo():
  pound = float(input('Enter the number of pounds: '))
  kilo = pound / 2.205

  print('Weight in kilograms is: {0}'.format(kilo))

def celsius_fahren():
  celsius = float(input('Enter the temperature in Celsius: '))
  fahrenheit = (celsius * (9/5)) + 32

  print('Temperature in Fahrenheit is: {0}'.format(fahrenheit))

def fahren_celsius():
  fahrenheit = float(input('Enter the temperature in Fahrenheit: '))
  celsius = (fahrenheit - 32) * (5/9)

  print('Temperature in Celsius is: {0}'.format(celsius))


if __name__ == "__main__":
  print_menu()
  choice = input('Which conversion would you like to do?: ')

  options = { 
    '1': km_miles,
    '2': miles_km,
    '3': kilo_Pound,
    '4': pound_kilo,
    '5': celsius_fahren,
    '6': fahren_celsius
  }

  if choice in options:
    options[choice]()
  else:
    print("Invalid choice. Please select a valid option.")