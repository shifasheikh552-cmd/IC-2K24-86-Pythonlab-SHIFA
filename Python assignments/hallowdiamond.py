#Hollow Diamond

n = int(input("Enter odd n: "))
if n % 2 == 0:
    print("Please enter odd number")
else:
    mid = n // 2
    for i in range(n):
        outer = abs(mid - i)
        inner = 2 * (mid - outer) - 1

        # Outer spaces
        line = " " * outer

        if inner < 0:
            # First and last row - single star
            line = line + "*"
        else:
            # Hollow part - two stars with inner space
            line = line + "*" + " " * inner + "*"
        
        print(line)