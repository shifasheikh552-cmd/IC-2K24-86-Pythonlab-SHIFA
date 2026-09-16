n = 4
size = 2 * n - 1

for i in range(size):
    row = ""
    for j in range(size):
        d = min(i, j, size-1-i, size-1-j)
        row += str(n - d)
    print(row)