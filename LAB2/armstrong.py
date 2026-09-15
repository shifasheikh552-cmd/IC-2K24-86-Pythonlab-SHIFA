def is_armstrong(num):
    if num < 0:
        return False

    digits = len(str(num))
    temp = num
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10

    return total == num


def main():
    while True:
        try:
            num = int(input("Enter a non-negative number: "))
            if num >= 0:
                break
            print("Please enter a non-negative number.")
        except ValueError:
            print("Invalid input.")

    if is_armstrong(num):
        print(num, "is an Armstrong number.")
    else:
        print(num, "is not an Armstrong number.")

    while True:
        try:
            start = int(input("Enter range start: "))
            end = int(input("Enter range end: "))

            if start < 0 or end < 0:
                print("Range values cannot be negative.")
            else:
                break
        except ValueError:
            print("Invalid input.")

    if start > end:
        start, end = end, start

    print("Armstrong numbers in the range:")
    for number in range(start, end + 1):
        if is_armstrong(number):
            print(number, end=" ")


if __name__ == "__main__":
    main()
