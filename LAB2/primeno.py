def is_prime(num):
    if num < 2:
        return False

    divisor = 2

    while divisor * divisor <= num:
        if num % divisor == 0:
            return False
        divisor += 1

    return True


def main():
    while True:
        try:
            num = int(input("Enter a number: "))
            break
        except ValueError:
            print("Invalid input.")

    if is_prime(num):
        print(num, "is a prime number.")
    else:
        print(num, "is not a prime number.")

    while True:
        try:
            limit = int(input("Enter the limit: "))

            if limit < 0:
                print("Please enter a non-negative limit.")
            else:
                break
        except ValueError:
            print("Invalid input.")

    print("Prime numbers up to", limit, ":")

    for number in range(2, limit + 1):
        if is_prime(number):
            print(number, end=" ")

    print()


if __name__ == "__main__":
    main()
