# Jessica Grier

# 02/25/2024

# P1HW2

# Basic Math on Numbers Entered
 
print('This program calculates and displays travel expenses')
 
budget_num = int(input('Enter Budget:'))
 
travel_name = input('Enter your travel destination:')
 
gas_num = int(input('How much do you think you will spend on gas?'))
 
acc_num = int(input('Approximately, how much will you need for accommodation/hotel?'))
 
food_num = int(input('Last, how much do you need for food?'))

print('------------Travel Expenses------------')
print('Location:' , travel_name)
print('Initial Budget:' , budget_num)

print('Fuel:' , gas_num)
print('Accomodation:' , acc_num)
print('Food:' , food_num)
x = gas_num + acc_num + food_num
print('Remaining Balance:', budget_num - x)
 
