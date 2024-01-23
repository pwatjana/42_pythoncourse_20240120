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
    #from rich import print
    import random
    hand = random.choices(["rock", "scissor", "paper"])[0]
    print(hand)
random()

# count round 
def count(round: int):
    count = 0
    while round < 3:
        print(round)
        round = round+1
    print("End game : your score = ")


# determine winner and count win round
def win(hand,user1):
    num=0 # initial score start 0
    # winning conditions
    if hand == 'rock' and user1 == 'p':
        num +=1
    elif hand == 'paper' and user1 == 's':
        num +=1
    elif hand == 'scissor' and user1 == 'r':
        num +=1  
    print(num)
    return num


def user1():
    my_list = ['r','s','p']
    if user1 not in my_list:
        print("You lose! Invalid Input. Please type r/p/s for rock/paper/scissor")
        



def main():
    user1 = input("Choose only one> r, s, p: ")
    print("Computer choose : ", random)


if __name__ == "__main__":
    main()




        
    
   

