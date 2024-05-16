 # Jessia Grier

 # 4/28/2024

  # P4HW2

  # Ability to edit and enhance existing programs




# Initialize variables for totals
overtime_total = 0
regular_pay_total = 0
gross_pay_total = 0
employee_count = 0

while True:
    # Ask the user to enter the employee's name or "Done" to terminate
    employee_name = input("\nEnter employee's name or \"Done\" to terminate: ")

    if employee_name == "Done":
        # User wants to exit the program
        break

    # Ask the user to enter the number of hours worked and the pay rate
    hours_worked = float(input("How many hours did " + employee_name + " work? "))
    pay_rate = float(input("What is " + employee_name + " pay rate: "))

    # Calculate overtime hours and regular hours
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        regular_hours = 40
    else:
        overtime_hours = 0
        regular_hours = hours_worked

    # Calculate overtime pay and regular pay
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    regular_pay = regular_hours * pay_rate

    # Calculate gross pay
    gross_pay = regular_pay + overtime_pay

    # Update totals
    overtime_total += overtime_pay
    regular_pay_total += regular_pay
    gross_pay_total += gross_pay
    employee_count += 1

    # Display individual employee information
    print("\nEmployee Name:", employee_name)
    print('')
    print("Hours Worked    Pay Rate    OverTime    OverTime Pay    RegHour Pay    Gross Pay")
    print("-------------------------------------------------------------------------------------------------")
    print(f'{hours_worked:<16.1f}{pay_rate:<12.2f}{overtime_hours:<14.1f}{overtime_pay:<14.2f}{regular_pay:<14.2f}{gross_pay:.2f}')      


    
    
   

# Display totals and number of employees processed
print("\nTotal number of employees entered:", employee_count)
print("Total amount paid for overtime: $", overtime_total)
print("Total amount paid for regular hours: $", regular_pay_total)
print("Total amount pais in gross: $", gross_pay_total)

