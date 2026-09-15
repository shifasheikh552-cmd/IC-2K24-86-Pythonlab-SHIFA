item1 = input("Enter first item: ")
price1 = float(input("Enter price of first item: "))

item2 = input("Enter second item: ")
price2 = float(input("Enter price of second item: "))

item3 = input("Enter third item: ")
price3 = float(input("Enter price of third item: "))

total = price1 + price2 + price3

print("\nRECEIPT")
print("-------------------------")
print("Item\t\tPrice")
print("-------------------------")
print(f"{item1}\t\t₹{price1}")
print(f"{item2}\t\t₹{price2}")
print(f"{item3}\t\t₹{price3}")
print("-------------------------")
print(f"Total\t\t₹{total}")
