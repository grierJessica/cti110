# Jessica Grier

# 03/15/2024

# P3LAB

# LAB: LEAP YEAR




is_leap_year = False
   
input_year = int(input('Enter a year: '))

if input_year % 400 == 0 and input_year % 100 == 0:
  print (f'{input_year} - leap year')
elif  input_year % 4 == 0 and input_year % 100 != 0:
   print (f'{input_year} - leap year')
else:
   print (f'{input_year} - not a leap year')
