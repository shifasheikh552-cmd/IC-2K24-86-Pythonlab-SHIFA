def fibonacci_loop(n):
    series = []
    first = 0
    second = 1

    for _ in range(n):
        series.append(first)
        first, second = second, first + second

    return series


def fibonacci_recursive(n, counter):
    counter[0] += 1

    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibonacci_recursive(n - 1, counter) + fibonacci_recursive(n - 2, counter)


def recursive_series(n):
    series = []
    counter = [0]

    for i in range(n):
        series.append(fibonacci_recursive(i, counter))

    return series, counter[0]


def main():
    while True:
        try:
            n = int(input("Enter number of terms: "))

            if n > 0:
                break

            print("Please enter a positive number.")
        except ValueError:
            print("Invalid input.")

    loop_result = fibonacci_loop(n)
    recursive_result, calls = recursive_series(n)

    print("Fibonacci using loop:")
    print(loop_result)

    print("Fibonacci using recursion:")
    print(recursive_result)

    print("Recursive function calls:", calls)


if __name__ == "__main__":
    main()