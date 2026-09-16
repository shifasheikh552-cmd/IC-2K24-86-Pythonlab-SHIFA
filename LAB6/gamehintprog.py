#GUESSING GAME HINT
import random

def get_hint(number):
    even_odd = "EVEN" if number % 2 == 0 else "ODD"
    multiple_5 = "is a multiple of 5" if number % 5 == 0 else "is NOT a multiple of 5"
    return f"Hint: Number is {even_odd} and {multiple_5}"

def play_game():
    # Fixed settings
    LOW = 1
    HIGH = 100
    MAX_ATTEMPTS = 7
    START_SCORE = 100
    PENALTY = 10

    secret = random.randint(LOW, HIGH)
    score = START_SCORE
    attempts = 0

    print("--- Guessing Game with Hints & Scoring ---")
    print(f"I have picked a number between {LOW} and {HIGH}.")
    print(f"You have {MAX_ATTEMPTS} attempts. Starting Score: {score}")

    while attempts < MAX_ATTEMPTS:
        try:
            print(f"\nAttempt {attempts + 1}/{MAX_ATTEMPTS} | Score: {score}")
            guess = int(input(f"Enter your guess ({LOW}-{HIGH}): "))

            if not (LOW <= guess <= HIGH):
                print(f"Error: Please guess between {LOW} and {HIGH} only.")
                continue

            attempts += 1

            if guess == secret:
                print(f"\nCorrect! The number was {secret}.")
                print(f"You guessed it in {attempts} attempt(s).")
                print(f"Final Score: {score}")
                return

            # Wrong guess
            score -= PENALTY
            if score < 0:
                score = 0

            if guess < secret:
                print("Too LOW!")
            else:
                print("Too HIGH!")

            # Extra hints after every wrong guess
            print(get_hint(secret))

            if attempts < MAX_ATTEMPTS:
                print(f"{MAX_ATTEMPTS - attempts} attempts left.")

        except ValueError:
            print("Error: Please enter a valid integer.")

    # If loop ends - limit reached
    print(f"\nYou lost! Maximum attempts ({MAX_ATTEMPTS}) reached.")
    print(f"The secret number was {secret}.")
    print(f"Final Score: 0")

if __name__ == "__main__":
    while True:
        play_game()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != 'y':
            print("Thanks for playing!")
            break