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


def main():
    while True:
        try:
            num = int(input("Enter a positive number: "))

            if num > 0:
                break

            print("Please enter a positive number.")
        except ValueError:
            print("Invalid input.")

    if is_perfect(num):
        print(num, "is a perfect number.")
    else:
        print(num, "is not a perfect number.")

    while True:
        try:
            limit = int(input("Enter the limit: "))

            if limit > 0:
                break

            print("Please enter a positive number.")
        except ValueError:
            print("Invalid input.")

    print("Perfect numbers up to", limit, ":")

    for number in range(1, limit + 1):
        if is_perfect(number):
            print(number, end=" ")

    print()


if __name__ == "__main__":
    main()