# Jessica Grier 

# 03/24/2024

# P3HW2_SALARY

# Write a program that dispays pay

# Asks the user to enter name of employee
# Ask user to enter number of hours the employee worked
# Ask user to enter employee's pay rate
# Display employee name
# If employee has worked 40 hours or less, consider as regular pay
# If employee has worked for 41 hours or more consider as overtime pay
# Calculate amount employee should be paid for regular hours worked
# Calculate amount employee should be paid for overtime hours worked
# Calculate gross pay
# Display hours worked, pay rate, overtime pay, regular pay, and gross pay


name = input("Enter employee's name: ")
hours = float(input("Enter number of hours worked: ") )
pay_rate = float(input("Enter employee's pay rate: ") )
print("---------------------------------------")
print("Employee's name:  " , name)
print(" ")
ot = hours - 40
reg_pay = hours * pay_rate
ot_pay = (ot * 1.5) * pay_rate

if hours <= 40:
   reg_play = hours * pay_rate 
    
else:
    ot_pay = (hours - 40)* (1.5 * pay_rate)
      
gross = ot_pay + (pay_rate * 40)
  
      
      

print("Hours Worked    Pay Rate    OverTime    OverTime Pay    RegHour Pay    Gross Pay")
print("-------------------------------------------------------------------------------------------------")
print(f'{hours:<16.1f}{pay_rate:<12.1f}{ot:<12.1f}{ot_pay:<16.2f}{reg_pay:<16.2f}{gross:.2f}')      
      
