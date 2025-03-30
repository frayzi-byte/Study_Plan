def read_number(which):
  while True:  
    try:
      return float(input(f'Enter the {which} number:'))  
    except ValueError:
      print('You need to enter a number')
  
num1 = read_number("first")
num2 = read_number("second")
print('Division', num1 / num2)
print('Addition', num1 + num2)
print('Multiplication', num1 * num2)
print('Subtraction', num1 - num2)