# Taking input from the user for the range
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

# Initialize a variable for the loop
num = start

# Loop through the range
while num <= end:
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")

    # Increment the number
    num += 1
