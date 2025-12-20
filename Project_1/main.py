'''

Rock, Paper, Scissors Game

'''

import random

user_choice=input("Enter your choice (Rock, Paper, Scissors): ").lower()
print("User choice is: ",user_choice)

valid_choices=['rock','paper','scissors']

if user_choice not in valid_choices:
    print("Invalid choice! Please choose Rock, Paper, or Scissors.")
    exit()

computer_choice=random.choice(['rock','paper','scissors'])

print("Computer choice is: ",computer_choice)

if user_choice==computer_choice:
    print("It's a tie!")
elif user_choice=='rock':
    if computer_choice=='scissors':
        print("User wins!")
    else:
        print("Computer wins!")
else:
    if user_choice=='paper':
        if computer_choice=='rock':
            print("User wins!")
        else:
            print("Computer wins!")

