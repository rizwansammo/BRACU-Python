# Basic if-else example
x = 10
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")

# If-elif-else example
y = 20
if y < 10:
    print("y is less than 10")
elif y == 20:
    print("y is equal to 20")
else:
    print("y is greater than 10 but not equal to 20")

# Nested if-else example
z = 15
if z > 10:
    if z < 20:
        print("z is between 10 and 20")
    else:
        print("z is greater than or equal to 20")
else:
    print("z is 10 or less")

# Using logical operators
a = 25
b = 30
if a > 20 and b > 25:
    print("Both a and b are greater than their respective values")
else:
    print("Either a or b is not greater than their respective values")

# Ternary operator (conditional expression)
c = 5
result = "c is even" if c % 2 == 0 else "c is odd"
print(result)

# Advanced example with functions
def check_number(num):
    if num > 0:
        return "Positive"
    elif num == 0:
        return "Zero"
    else:
        return "Negative"

print(check_number(10))
print(check_number(0))
print(check_number(-5))