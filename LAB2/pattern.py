def star_triangle(n):
    print("\nRight-angled triangle:")

    for row in range(1, n + 1):
        for column in range(row):
            print("*", end=" ")
        print()


def number_pattern(n):
    print("\nNumber pattern:")

    for row in range(1, n + 1):
        for number in range(1, row + 1):
            print(number, end=" ")
        print()


def pyramid(n):
    print("\nCentered pyramid:")

    for row in range(1, n + 1):

        for space in range(n - row):
            print(" ", end=" ")

        for star in range(2 * row - 1):
            print("*", end=" ")

        print()


def main():
    while True:
        try:
            n = int(input("Enter number of rows: "))

            if n > 0:
                break

            print("Please enter a positive number.")
        except ValueError:
            print("Invalid input.")

    star_triangle(n)
    number_pattern(n)
    pyramid(n)


if __name__ == "__main__":
    main()