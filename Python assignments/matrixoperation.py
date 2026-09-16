#MATRIX OPERATION
matrix = []
print("Enter 3x3 matrix - 9 numbers one by one:")

for i in range(3):
    row = []
    for j in range(3):
        num = int(input(f"Enter element [{i}][{j}]: "))
        row.append(num)
    matrix.append(row)

#Displaying the matrix
print("\nMatrix is:")
for i in range(3):
    print(matrix[i][0], matrix[i][1], matrix[i][2])

#sum of all matrix
total = 0
for i in range(3):
    for j in range(3):
        total = total + matrix[i][j]
print("\nSum of all elements:", total)

#diagonal of matrix
diag = matrix[0][0] + matrix[1][1] + matrix[2][2]
print("Sum of diagonal:", diag)

#Largest and smallest
largest = matrix[0][0]
smallest = matrix[0][0]
for i in range(3):
    for j in range(3):
        if matrix[i][j] > largest:
            largest = matrix[i][j]
        if matrix[i][j] < smallest:
            smallest = matrix[i][j]

print("Largest:", largest)
print("Smallest:", smallest)

#Transpose of a matrix
print("\nTranspose:")
for i in range(3):
    print(matrix[0][i], matrix[1][i], matrix[2][i])