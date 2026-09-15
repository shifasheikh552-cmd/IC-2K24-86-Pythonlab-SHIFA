import random


def is_armstrong(num):
    if num < 0:
        return False

    digits = len(str(num))
    total = 0
    temp = num

    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10

    return total == num


def is_prime(num):
    if num < 2:
        return False

    divisor = 2

    while divisor * divisor <= num:
        if num % divisor == 0:
            return False
        divisor += 1

    return True


def is_perfect(num):
    if num <= 1:
        return False

    total = 1
    divisor = 2

    while divisor * divisor <= num:
        if num % divisor == 0:
            total += divisor

            other = num // divisor

            if other != divisor:
                total += other

        divisor += 1

    return total == num


def is_number_palindrome(num):
    if num < 0:
        return False

    original = num
    reversed_num = 0

    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10

    return original == reversed_num


def is_string_palindrome(text):
    left = 0
    right = len(text) - 1

    while left < right:
        if text[left] != text[right]:
            return False

        left += 1
        right -= 1

    return True


def fibonacci(n):
    series = []
    first = 0
    second = 1

    for _ in range(n):
        series.append(first)
        first, second = second, first + second

    return series


def print_patterns(n):
    print("\nStar Triangle:")

    for row in range(1, n + 1):
        for _ in range(row):
            print("*", end=" ")
        print()

    print("\nNumber Pattern:")

    for row in range(1, n + 1):
        for number in range(1, row + 1):
            print(number, end=" ")
        print()

    print("\nCentered Pyramid:")

    for row in range(1, n + 1):
        for _ in range(n - row):
            print(" ", end=" ")

        for _ in range(2 * row - 1):
            print("*", end=" ")

        print()


def get_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Enter an integer.")


def menu():
    while True:
        print("\n========== MENU ==========")
        print("1. Armstrong Number")
        print("2. Prime Number")
        print("3. Perfect Number")
        print("4. Number Palindrome")
        print("5. String Palindrome")
        print("6. Fibonacci Series")
        print("7. Pattern Printing")
        print("8. Number Guessing Game")
        print("0. Exit")
        print("==========================")

        choice = get_integer("Enter your choice: ")

        if choice == 0:
            print("Program ended.")
            break

        elif choice == 1:
            num = get_integer("Enter a number: ")

            if num < 0:
                print("Negative numbers are not accepted.")
            elif is_armstrong(num):
                print("Armstrong number")
            else:
                print("Not an Armstrong number")

        elif choice == 2:
            num = get_integer("Enter a number: ")

            if is_prime(num):
                print("Prime number")
            else:
                print("Not a prime number")

        elif choice == 3:
            num = get_integer("Enter a positive number: ")

            if num <= 0:
                print("Please enter a positive number.")
            elif is_perfect(num):
                print("Perfect number")
            else:
                print("Not a perfect number")

        elif choice == 4:
            num = get_integer("Enter a non-negative number: ")

            if num < 0:
                print("Negative numbers are not accepted.")
            elif is_number_palindrome(num):
                print("Palindrome")
            else:
                print("Not a palindrome")

        elif choice == 5:
            text = input("Enter a string: ")

            if is_string_palindrome(text):
                print("Palindrome")
            else:
                print("Not a palindrome")

        elif choice == 6:
            n = get_integer("Enter number of terms: ")

            if n <= 0:
                print("Please enter a positive number.")
            else:
                print("Fibonacci series:", fibonacci(n))

        elif choice == 7:
            n = get_integer("Enter number of rows: ")

            if n <= 0:
                print("Please enter a positive number.")
            else:
                print_patterns(n)

        elif choice == 8:
            secret = random.randint(1, 100)

            for attempt in range(1, 8):
                guess = get_integer("Guess the number (1-100): ")

                if guess < 1 or guess > 100:
                    print("Enter a number between 1 and 100.")
                    continue

                if guess < secret:
                    print("Too low!")

                elif guess > secret:
                    print("Too high!")

                else:
                    print("Correct!")
                    print("Attempts:", attempt)
                    break
            else:
                print("You ran out of attempts.")
                print("The number was:", secret)

        else:
            print("Invalid choice. Please select 0 to 8.")


if __name__ == "__main__":
    menu()