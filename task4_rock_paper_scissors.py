"""Task 4: Rock-Paper-Scissors Game with score tracking."""
import random

CHOICES = ["rock", "paper", "scissors"]
BEATS = {"rock": "scissors", "scissors": "paper", "paper": "rock"}


def get_user_choice():
    while True:
        c = input("Choose rock, paper or scissors: ").strip().lower()
        if c in CHOICES:
            return c
        print("Invalid choice. Please type rock, paper or scissors.")


def decide(user, comp):
    if user == comp:
        return "tie"
    return "user" if BEATS[user] == comp else "computer"


def main():
    print("=== ROCK - PAPER - SCISSORS ===")
    print("Rules: Rock beats Scissors, Scissors beats Paper, Paper beats Rock.\n")
    user_score = comp_score = ties = 0

    while True:
        user = get_user_choice()
        comp = random.choice(CHOICES)
        print(f"\nYou chose:      {user}")
        print(f"Computer chose: {comp}")

        result = decide(user, comp)
        if result == "tie":
            ties += 1
            print("It's a tie!")
        elif result == "user":
            user_score += 1
            print("You win this round!")
        else:
            comp_score += 1
            print("Computer wins this round!")

        print(f"Score -> You: {user_score} | Computer: {comp_score} | Ties: {ties}\n")

        if input("Play another round? (y/n): ").strip().lower() != "y":
            break
        print()

    print("\n--- Final Score ---")
    print(f"You: {user_score} | Computer: {comp_score} | Ties: {ties}")
    if user_score > comp_score:
        print("Overall winner: YOU!")
    elif comp_score > user_score:
        print("Overall winner: Computer")
    else:
        print("Overall: It's a draw!")


if __name__ == "__main__":
    main()
