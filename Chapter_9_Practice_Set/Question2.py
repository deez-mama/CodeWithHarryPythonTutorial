"""  
The game() function in a program lets a user play a game and returns the score as an integer. 
You need to read a file ‘Hi-score.txt’ which is either blank or contains the previous Hi-score. 
You need to write a program to update the Hiscore whenever the game() function breaks the Hi-score
"""

import random

def game():
    Highscore=random.randrange(1,10000)
    print(f"The current Highscore is {Highscore}\n")
    return Highscore

current_hi=game()

with open ("Hi-score.txt") as f:
    prev_hi=f.read()

with open ("Hi-score.txt" , "w") as f:
    if(prev_hi==""):
        f.write(str(current_hi))
        print("The file is empty, this it the first highscore saved!") 
    else:
        if int(prev_hi)>current_hi:
            print(f"The previous high score of {prev_hi} is greater.")
            f.write(prev_hi)  # Doing this because the previous highscore gets removed if new one isnt written for some reason
        else:
            f.write(str(current_hi))
            print("The current highschore has been saved.")







