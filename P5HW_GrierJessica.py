#Jessica Grier

# 4/28/2024

#P5HW

# Write a program giving simple math quiz, make the program a menu driven program.

import random

def main():
    print("Welcome to Math Quiz")
    print('')
    
    while True:
        display_menu()  
        choice = input("Please choose one of the menu options: ")

        if choice == "1":
            add_random_numbers()
        elif choice == "2":
            subtract_random_numbers()
        elif choice == "3":
            print("Thank you for playing...\nBye!!")
            break
        else:
            print("Invalid selection.")

def display_menu():
    print("MAIN MENU")
    print('----------------------')
    print("1. Add Random Numbers")
    print("2. Subtract Random Numbers")
    print("3. Exit")

def add_random_numbers():
    num1 = random.randint(1, 600) 
    num2 = random.randint(1, 600) 
    correct_answer = num1 + num2  
    guess_count = 0                

    print(f"{num1: >3}\n+{num2: >2}\nEnter answer.")

    
    while True:
        guess = int(input())
        guess_count += 1
        if guess < correct_answer:
            print("Sorry, guess is too low.\nTry again: ", end="")
        elif guess > correct_answer:
            print("Sorry, guess is too high.\nTry again: ", end="")
        else:
            print("Congratulations!!!! Your answer is correct.")
            print(f"Number of guesses: {guess_count}")
            break

def subtract_random_numbers():
    num1 = random.randint(1, 600)
    num2 = random.randint(1, 600)
    correct_answer = num1 - num2
    guess_count = 0

    print(f"{num1: >3}\n-{num2: >2}\nEnter answer.")

    while True:
        guess = int(input())
        guess_count += 1
        if guess < correct_answer:
            print("Sorry, guess is too low.\nTry again: ", end="")
        elif guess > correct_answer:
            print("Sorry, guess is too high.\nTry again: ", end="")
        else:
            print("Congratulations!!!! Your answer is correct.")
            print(f"Number of guesses: {guess_count}")
            break

if __name__ == "__main__":
    main()
