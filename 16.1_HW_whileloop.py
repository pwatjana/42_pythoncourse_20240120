"""
    rock scissor paper
    Create a rock scissor paper game
    Player vs computer
    3 rounds only
    2 out of 3 wins
    input r,s,p
        other than r,s,p > = 0
    report score




"""
#from rich import print
import random

num=0
i = 0
while i < 3 :
     
    print("Round",i+1)

    hand = random.choices(["rock", "scissor", "paper"])[0]
    print(hand)
    user1 = input("type here : ")

    if num == 2:
        break
        print("You win 2 out of 3, Congrat !")

    if hand == 'rock' and user1 == 'p':
        num = num+1
        print(num)
    elif hand == 'paper' and user1 == 's':
        num = num+1
        print(num)
    elif hand == 'scissor' and user1 == 'r':
        num = num+1 
        print(num) 
    i+=1
print("Total win:lose" , num ,":",3-num)