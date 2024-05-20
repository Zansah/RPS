import random
import time

# slashes are used for line continuation 
def rps():
    play_again = True
    user_wins = 0
    computer_wins = 0

    while play_again:
        user_choice = input('Please choose between Rock, Paper, Scissors: ').lower()

        print("Rock, Paper, Scissors, Shoot!")
        time.sleep(1)

        computer_choice = random.choice(["rock", "paper", "scissors"])
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
            user_wins += 1
        else:
            print("Computer wins!")
            computer_wins += 1

        print(f"Score: User {user_wins} - {computer_wins} Computer")

        play = input("Enter 'yes' if you want to play again, otherwise 'no': ").lower()

        if play != "yes":
            play_again = False

def main():
    rps()

main()
