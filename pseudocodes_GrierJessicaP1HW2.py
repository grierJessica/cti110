# Jessica Grier

# 02/25/2024

# P1HW2

# Pseudocode Basic Math on Numbers Entered
 

#Display "Enter Budget"
#Input the budget from the user and store it in a variable called budget_num 
#Display "Enter your travel destination"
#Input the destination from the user and store it in a variable called travel_name
#Display "How much do you think you will spend on gas?"
#Input the gas from the user and store it in a variable called gas_num
#Display "Approximately, how much will you need for accomodation/hotel?"
#Input the accomodation from the user and store it in a variable called acc_num
#Display "Last, how much do you need for food?"
#Input the food from the user and store it in a variable called food_num
#Add gas_num and acc_num and food_num and then subtract it from the budget_num as the remaining balance

print('This program calculates and displays travel expenses')

budget_num = int(input('Enter budget:') )

travel_name = input('Enter your travel destination:\n')
 
gas_num = int(input('How much do you think you will spend on gas?\n'))

acc_num = int(input('Approximately, how much will you need for accommodation/hotel?'))
 
food_num = int(input('Last, how much do you need for food?'))

print('------------Travel Expenses------------')
print('Location:' , travel_name)
print('Initial Budget:' , budget_num)

print('Fuel:' , gas_num)
print('Accomodation:' , acc_num)
print('Food:' , food_num)

print('Remaining Balance:', gas_num + acc_num + food_num - budget_num)
 
