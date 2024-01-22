
#round 1
#from rich import print
import random

win = 0

for i in range(1,4):

    user1 = input("type here :")

    #Check user input , if not r,s,p warning with text.
    list_1 = ['r', 's', 'p']
    while  user1 not in list_1:
        print("Invalid Input! Please type r/p/s for rock/paper/scissor")
        break

    # computer random word from list.
    hand = random.choices(["rock", "paper", "scissor"])[0]
    #print(type(hand))
    print(("Computer choose:", hand))
    
    #Compare user input and computer choice and  collect score.
    if hand == "rock" and user1 =='p':
        win += 1
    elif hand == "scissor" and user1 == 'r':
        win += 1
    elif hand == "paper" and user1 == 's':
        win += 1    

    #if score reach 2 end game with message.
    if win ==2:
        break
print("End of the game \nYou have won ", win ,"out of 3 round")


'''Googlebard -> Here's a breakdown of how it works:
random.choices(["rock", "paper", "scissor"]):

This part of the code calls the random.choices() function, which randomly selects one or more elements from the provided list.
In this case, the list is ["rock", "paper", "scissor"], so it will randomly choose one of those options.
However, random.choices() always returns a class as list, even if you're only selecting a single element.
[0]:

This is where [0] comes into play. It's used to access the first element of the list returned by random.choices().
In Python, list indexing starts from 0, so [0] refers to the very first item in the list.
Assignment to hand:

The selected element (either "rock", "paper", or "scissor") is then assigned to the variable hand return class = str.
'''