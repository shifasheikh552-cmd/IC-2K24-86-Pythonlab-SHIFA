#Atm_simulation

def check_balance(balance):
    print(f"\nYour current balance is: Rs. {balance}")

def deposit(balance):
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

def withdraw(balance):
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

def change_pin(current_pin):
    try:
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
    except Exception as e:
        print(f"Error: {e}")
        return current_pin

def main():
    # Fixed initial values
    balance = 10000.0
    pin = "1234"
    attempts = 3

    print("--- Welcome to ATM ---")
    # PIN verification before menu
    while attempts > 0:
        entered_pin = input("Enter your 4-digit PIN: ")
        if entered_pin == pin:
            print("PIN verified successfully.\n")
            break
        else:
            attempts -= 1
            print(f"Incorrect PIN. Attempts left: {attempts}")
            if attempts == 0:
                print("Too many failed attempts. Card blocked.")
                return
    while True:
        print("\n------ ATM MENU ------")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Change PIN")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            check_balance(balance)
        elif choice == '2':
            balance = deposit(balance)
        elif choice == '3':
            balance = withdraw(balance)
        elif choice == '4':
            pin = change_pin(pin)
        elif choice == '5':
            print("Thank you for using ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1 to 5.")

if __name__ == "__main__":
    main()