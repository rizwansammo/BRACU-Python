import itertools

# Basic for loop
for i in range(5):
    print(f"Basic loop iteration {i}")

# Looping through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"Fruit: {fruit}")

# Looping through a string
for char in "hello":
    print(f"Character: {char}")

# Looping with index
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

# Nested loops
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")

# Looping through a dictionary
person = {"name": "John", "age": 30, "city": "New York"}
for key, value in person.items():
    print(f"{key}: {value}")

# List comprehension
squares = [x**2 for x in range(10)]
print(f"Squares: {squares}")

# Loop with condition
for i in range(10):
    if i % 2 == 0:
        print(f"Even number: {i}")

# Breaking out of a loop
for i in range(10):
    if i == 5:
        break
    print(f"Breaking loop at {i}")

# Continuing a loop
for i in range(10):
    if i % 2 == 0:
        continue
    print(f"Odd number: {i}")

# Looping with else
for i in range(5):
    print(f"Loop iteration {i}")
else:
    print("Loop completed")

# Advanced: Looping through multiple lists using zip
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

# Advanced: Using itertools for combinations
colors = ["red", "green", "blue"]
for combination in itertools.combinations(colors, 2):
    print(f"Combination: {combination}")

# Advanced: Using itertools for permutations
for permutation in itertools.permutations(colors):
    print(f"Permutation: {permutation}")