"""
    rock scissor paper
    Create a rock scissor paper game
    Player vs computer
    3 rounds only
    2 out of 3 wins
    input r,s,p
    report score
"""

# random pick items in lists and return first arg of the list.
# return random value.
def random():
    from rich import print
    import random
    hand = random.choices(["rock", "scissor", "paper"])
    print(hand)
random()

# count round 
def count(round: int):
     while round < 3:
        print("Round ", round+1)
        round = round+1
        
# determine winner and count win round
def win(hand,user1):
    num=0 # initial score start 0
    while num ==2 :
        break
        print("Congrats! you win 2 out of 3 round ")
    # winning conditions.
    if hand == 'rock' and user1 == 'p':
        num +=1
    elif hand == 'paper' and user1 == 's':
        num +=1
    elif hand == 'scissor' and user1 == 'r':
        num +=1  
    print("End game : your score = ", num)


def user1(type):
    my_list = ['r','s','p']
    if user1 not in my_list:
        print("You lose! Invalid Input. Please type r/p/s for rock/paper/scissor")
    else:
        return 
        



def main():
    hand = random    
    user_choose = input("Enter your choice (r/p/s for rock/paper/) : ")
    user1(user_choose)
    win(hand,user1)

        
        



if __name__ == "__main__":
    main()




        
    
   

