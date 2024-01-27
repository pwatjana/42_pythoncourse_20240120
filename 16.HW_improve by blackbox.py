import random

def get_computer_hand():
    """Returns the computer's hand as a random choice from rock, scissor, paper."""
    return random.choice(["rock", "scissor", "paper"])

def display_hand(hand):
    """Displays the given hand on the console."""
    print(hand)

def play_round(user_hand):
    """Plays one round of the game with the given user hand. Returns True if the user wins, False otherwise."""
    computer_hand = get_computer_hand()
    display_hand(computer_hand)

    if (user_hand == "rock" and computer_hand == "scissor") or \
       (user_hand == "scissor" and computer_hand == "paper") or \
       (user_hand == "paper" and computer_hand == "rock"):
        return True
    elif user_hand == computer_hand:
        return None
    else:
        return False

def play_game():
    """Plays a game of rock, scissor, paper between the user and the computer. Returns True if the user wins, False otherwise."""
    user_wins = 0
    for round in range(1, 4):
        print(f"Round {round}")
        user_hand = input("Enter your hand (r, s, p): ").lower()
        result = play_round(user_hand)
        if result is True:
            user_wins += 1
        elif result is None:
            print("It's a tie!")
    
    if user_wins >= 2:
        print("Congratulations! You won 2 out of 3 rounds.")
        return True
    else:
        print("Sorry, you lost. Better luck next time!")
        return False

if __name__ == "__main__":
    play_game()