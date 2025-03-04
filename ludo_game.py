import random

def roll_dice():
    return random.randint(1, 6)

def play_ludo():
    print("Welcome to the Ludo Dice Game!")
    while True:
        input("Press Enter to roll the dice...")
        result = roll_dice()
        print(f"You rolled a {result}!")
        
        play_again = input("Do you want to roll again? (yes/no): ").lower()
        if play_again != "yes":
            break

    print("Thanks for playing!")

if __name__ == "__main__":
    play_ludo()
