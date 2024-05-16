# Jessica Grier

# 4/28/2024

# P4HW1

# Edit and enhance existing programs




# Ask user to enter an amount of scores
num_scores = int(input("How many scores do you want to enter? "))
print('')

# Initialize a list to store the valid scores
scores = []

# Add a Loop to collect scores
for i in range(1, num_scores + 1):
    while True:
        score=float(input(f"Enter score #{i}: "))
        if 0 <= score <= 100:
            # If Score is valid, add it to the list
            scores.append(score)
            break
        else:
            print('')
            print("INVALID score entered!!!!\nScore should be between 0 and 100.")
            score = float(input(f"Enter score #{i} again: "))
            break

# Calculate lowest score
lowest_score = min(scores)

# Remove the lowest score from the list
scores.remove(lowest_score)

# Calculate the average scores
average = sum(scores) / len(scores)

# Determine the Grade
if 90 <= average <= 100:
    grade = "A"
elif 80 <= average < 90:
    grade = "B"
elif 70 <= average < 80:
    grade = "C"
elif 60 <= average < 70:
    grade = "D"
else:
    grade = "F"

# Display results
print("--------------Results------------")
print(f'Lowest Score   : {lowest_score:.1f}')
print('Modified List  :', scores)
print(f'Score Average  : {average:.2f}')
print("Grade          :", grade)
print("-----------------------------------")
