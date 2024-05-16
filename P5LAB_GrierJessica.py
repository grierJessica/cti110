def days_in_feb(user_year):
    if user_year % 400 == 0:
        return 29
    elif user_year % 4 == 0 and user_year% 100 != 0:
        return 29
    else:
        return 28
    

    return days

if __name__ == '__main__':
     user_input = int(input())
     days = days_in_feb(user_input)
     
     print(f'{user_input} has {days} days in February.')

