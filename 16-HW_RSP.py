"""
    rock scissor paper
    Create a rock scissor paper game
    Player vs computer
    3 rounds only
    2 out of 3 wins
    input r,s,p
    report score
"""
def random():
    from rich import print
    import random
    hand = random.choices(["rock", "scissor", "paper"])[0]
    print(hand)
random()

def count(round: int):
    round = 0
    while round < 3:
        print(round)
        round = round+1
        if round == 3:
            break
    print("End 3 round")
count(round)

def win(hand,user1):
    num=0
    if hand == 'rock' and user1 == 'p':
        num +=1
    elif hand == 'paper' and user1 == 's':
        num +=1
    elif hand == 'scissor' and user1 == 'r':
        num +=1  
    print(num)


my_list = ['r','s','p']



def main():
    count(0)
    user1 = input("Choose only one> r, s, p: ")
    win(random(),user1())
    print(win)
if __name__ == "__main__":
    main()




        
    
   

