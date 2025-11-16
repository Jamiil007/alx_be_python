
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use a while loop to print each row
while row < size:
    # Use a for loop to print asterisks in each row
    for _ in range(size):
        print("*", end="")
    
    print()  # Move to the next line after each row
    row += 1  # Increment row counter
