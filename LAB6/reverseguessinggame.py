#REVERSE GUESSING GAME

def get_valid_range():
    while True:
        try:
            print("\nSet the range for your secret number.")
            low = int(input("Enter lower bound (e.g., 1): "))
            high = int(input("Enter upper bound (e.g., 100): "))
            if low >= high:
                print("Error: Lower bound must be smaller than upper bound.")
                continue
            return low, high
        except ValueError:
            print("Error: Please enter valid integers.")

def reverse_guessing_game():
    print("--- Reverse Guessing Game ---")
    print("Think of a number and I (computer) will guess it!")

    low, high = get_valid_range()
    print(f"\nGreat! Think of a number between {low} and {high}. Don't tell me!")
    input("Press Enter when you are ready...")

    guesses = 0
    original_low, original_high = low, high

    while True:
        # Binary search strategy
        if low > high:
            print("\nOops! You gave conflicting hints. You cheated or made a mistake!")
            print(f"Range became invalid: low={low}, high={high}")
            break

        guess = (low + high) // 2
        guesses += 1

        # Get user feedback with validation
        while True:
            print(f"\nMy guess #{guesses} is: {guess}")
            feedback = input("Is it (H)igh, (L)ow, or (C)orrect? : ").strip().lower()
            
            if feedback in ['h', 'high', 'too high']:
                high = guess - 1
                break
            elif feedback in ['l', 'low', 'too low']:
                low = guess + 1
                break
            elif feedback in ['c', 'correct', 'yes', 'y']:
                print(f"\nYay! I guessed your number {guess} in {guesses} attempts!")
                print(f"Range was {original_low} to {original_high}.")
                return
            else:
                print("Invalid input! Please enter only H for too high, L for too low, or C for correct.")

if __name__ == "__main__":
    while True:
        reverse_guessing_game()
        
        again = input("\nWant to play again? (y/n): ").strip().lower()
        if again != 'y':
            print("Thanks for playing! Goodbye!")
            break