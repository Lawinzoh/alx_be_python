size = int(input("Enter the size of the pattern: "))
row = 1
while row <= size:
    col = 1
    while col <= size:
        print("*", end="")
        col += 1
    print()  # Move to a new line after each row
    row += 1  # Move to the next row