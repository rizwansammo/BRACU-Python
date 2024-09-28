# Basic while loop
count = 0
while count < 5:
    print("Count is:", count)
    count += 1

# While loop with break statement
count = 0
while count < 10:
    print("Count is:", count)
    if count == 5:
        break
    count += 1

# While loop with continue statement
count = 0
while count < 10:
    count += 1
    if count % 2 == 0:
        continue
    print("Odd count is:", count)

# While loop with else statement
count = 0
while count < 5:
    print("Count is:", count)
    count += 1
else:
    print("Loop ended with count:", count)

# Nested while loops
outer_count = 0
while outer_count < 3:
    inner_count = 0
    while inner_count < 3:
        print(f"Outer count: {outer_count}, Inner count: {inner_count}")
        inner_count += 1
    outer_count += 1

# Advanced example: while loop to find the first 10 Fibonacci numbers
fib1, fib2 = 0, 1
count = 0
while count < 10:
    print(f"Fibonacci number {count + 1}: {fib1}")
    fib1, fib2 = fib2, fib1 + fib2
    count += 1

# Advanced example: while loop with user input
while True:
    user_input = input("Enter 'exit' to stop the loop: ")
    if user_input.lower() == 'exit':
        print("Exiting the loop.")
        break
    else:
        print(f"You entered: {user_input}")