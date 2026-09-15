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


def main():
    while True:
        try:
            num = int(input("Enter a non-negative number: "))

            if num >= 0:
                break

            print("Please enter a non-negative number.")
        except ValueError:
            print("Invalid input.")

    if is_number_palindrome(num):
        print(num, "is a palindrome.")
    else:
        print(num, "is not a palindrome.")

    text = input("Enter a string: ")

    if is_string_palindrome(text):
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")


if __name__ == "__main__":
    main()