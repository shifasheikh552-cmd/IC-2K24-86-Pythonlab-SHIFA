#COMBINED APP
import random

# ========== ATM MODULE ==========
def atm_check_balance(balance):
    print(f"\nYour current balance is: Rs. {balance}")

def atm_deposit(balance):
    try:
        amount = float(input("Enter amount to deposit: "))
        if amount <= 0:
            print("Error: Amount must be greater than 0.")
            return balance
        balance += amount
        print(f"Rs. {amount} deposited successfully.")
    except ValueError:
        print("Error: Please enter a valid number.")
    return balance

def atm_withdraw(balance):
    try:
        amount = float(input("Enter amount to withdraw: "))
        if amount <= 0:
            print("Error: Amount must be greater than 0.")
            return balance
        if amount > balance:
            print("Error: Insufficient balance. Withdrawal rejected.")
            return balance
        balance -= amount
        print(f"Rs. {amount} withdrawn successfully.")
    except ValueError:
        print("Error: Please enter a valid number.")
    return balance

def atm_change_pin(current_pin):
    old_pin = input("Enter old PIN: ")
    if old_pin != current_pin:
        print("Error: Old PIN is incorrect.")
        return current_pin
    new_pin = input("Enter new 4-digit PIN: ")
    if not (new_pin.isdigit() and len(new_pin) == 4):
        print("Error: PIN must be 4 digits.")
        return current_pin
    confirm_pin = input("Confirm new PIN: ")
    if new_pin != confirm_pin:
        print("Error: PINs do not match.")
        return current_pin
    print("PIN changed successfully.")
    return new_pin

def run_atm():
    balance = 10000.0
    pin = "1234"
    attempts = 3

    print("\n--- Welcome to ATM ---")
    while attempts > 0:
        entered_pin = input("Enter your 4-digit PIN: ")
        if entered_pin == pin:
            print("PIN verified successfully.")
            break
        else:
            attempts -= 1
            print(f"Incorrect PIN. Attempts left: {attempts}")
            if attempts == 0:
                print("Too many failed attempts. Returning to main menu.")
                return
    
    while True:
        print("\n------ ATM MENU ------")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Change PIN")
        print("5. Back to Main Menu")
        choice = input("Choose (1-5): ").strip()

        if choice == '1':
            atm_check_balance(balance)
        elif choice == '2':
            balance = atm_deposit(balance)
        elif choice == '3':
            balance = atm_withdraw(balance)
        elif choice == '4':
            pin = atm_change_pin(pin)
        elif choice == '5':
            print("Exiting ATM to Main Menu...")
            break
        else:
            print("Invalid choice.")

# ========== GRADE CALCULATOR MODULE ==========
def run_grade_calculator():
    last_student = None

    def get_grade(avg):
        if avg >= 90: return 'A+'
        elif avg >= 80: return 'A'
        elif avg >= 70: return 'B'
        elif avg >= 60: return 'C'
        elif avg >= 50: return 'D'
        else: return 'F'

    while True:
        print("\n------ GRADE CALCULATOR ------")
        print("1. Enter marks for a new student")
        print("2. View grade of last entered student")
        print("3. Back to Main Menu")
        choice = input("Choose (1-3): ").strip()

        if choice == '1':
            try:
                name = input("Enter student name: ").strip()
                if not name:
                    print("Error: Name cannot be empty.")
                    continue
                marks = []
                print("Enter marks for 5 subjects (0-100):")
                for i in range(1, 6):
                    while True:
                        try:
                            m = float(input(f"  Subject {i}: "))
                            if 0 <= m <= 100:
                                marks.append(m)
                                break
                            else:
                                print("  Error: Must be 0-100.")
                        except ValueError:
                            print("  Error: Enter valid number.")
                total = sum(marks)
                average = total / 5
                grade = get_grade(average)
                last_student = {"name": name, "marks": marks, "total": total, "average": average, "grade": grade}
                print(f"\nSaved! {name}'s Average: {average:.2f}, Grade: {grade}")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == '2':
            if last_student is None:
                print("\nNo data found. Enter marks first.")
            else:
                print(f"\n--- Last Student ---")
                print(f"Name: {last_student['name']}")
                print(f"Marks: {last_student['marks']}")
                print(f"Total: {last_student['total']}/500")
                print(f"Average: {last_student['average']:.2f}")
                print(f"Grade: {last_student['grade']}")

        elif choice == '3':
            print("Exiting to Main Menu...")
            break
        else:
            print("Invalid choice.")

# ========== GUESSING GAME MODULE ==========
def run_guessing_game():
    LOW, HIGH = 1, 100
    MAX_ATTEMPTS = 7
    START_SCORE = 100
    PENALTY = 10

    secret = random.randint(LOW, HIGH)
    score = START_SCORE
    attempts = 0

    print(f"\n--- Guessing Game ---")
    print(f"I picked a number between {LOW}-{HIGH}. You have {MAX_ATTEMPTS} attempts.")

    while attempts < MAX_ATTEMPTS:
        try:
            print(f"\nAttempt {attempts+1}/{MAX_ATTEMPTS} | Score: {score}")
            guess = int(input(f"Enter guess ({LOW}-{HIGH}): "))
            if not (LOW <= guess <= HIGH):
                print(f"Enter between {LOW}-{HIGH} only.")
                continue

            attempts += 1
            if guess == secret:
                print(f"\nCorrect! Number was {secret} in {attempts} attempts.")
                print(f"Final Score: {score}")
                return

            score = max(0, score - PENALTY)
            print("Too LOW!" if guess < secret else "Too HIGH!")
            even_odd = "EVEN" if secret % 2 == 0 else "ODD"
            mult5 = "is a multiple of 5" if secret % 5 == 0 else "is NOT a multiple of 5"
            print(f"Hint: Number is {even_odd} and {mult5}")

        except ValueError:
            print("Error: Enter a valid integer.")

    print(f"\nYou lost! Max attempts reached. Number was {secret}. Final Score: 0")

# ========== TOP-LEVEL MENU ==========
def main():
    while True:
        print("\n========== MAIN MENU ==========")
        print("1. ATM Simulation")
        print("2. Student Grade Calculator")
        print("3. Guessing Game with Hints & Scoring")
        print("4. Exit")
        choice = input("Choose (1-4): ").strip()

        if choice == '1':
            run_atm()
        elif choice == '2':
            run_grade_calculator()
        elif choice == '3':
            run_guessing_game()
        elif choice == '4':
            print("Thank you! Exiting Combined Application.")
            break
        else:
            print("Invalid choice. Please enter 1-4.")

if __name__ == "__main__":
    main()