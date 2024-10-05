<<<<<<< HEAD
=======
# Basic String Operations

# Creating strings
str1 = "Hello"
str2 = 'World'

# Concatenation
str3 = str1 + " " + str2
print("Concatenation:", str3)

# Repetition
str4 = str1 * 3
print("Repetition:", str4)

# Accessing characters
first_char = str1[0]
print("First character:", first_char)

# Slicing
substring = str1[1:4]
print("Slicing:", substring)

# Length of string
length = len(str1)
print("Length:", length)

# Advanced String Operations

# String methods
upper_str = str1.upper()
print("Uppercase:", upper_str)

lower_str = str2.lower()
print("Lowercase:", lower_str)

# Strip whitespace
str5 = "  Hello World  "
stripped_str = str5.strip()
print("Stripped:", stripped_str)

# Replace
replaced_str = str3.replace("World", "Python")
print("Replaced:", replaced_str)

# Split
split_str = str3.split()
print("Split:", split_str)

# Join
joined_str = "-".join(split_str)
print("Joined:", joined_str)

# Find
index = str3.find("World")
print("Find:", index)

# Format
formatted_str = "Hello, {}!".format("Python")
print("Formatted:", formatted_str)

# f-Strings (Python 3.6+)
name = "Python"
f_string = f"Hello, {name}!"
print("f-String:", f_string)

# Checking if a string contains a substring
contains = "Hello" in str3
print("Contains 'Hello':", contains)

# Checking if a string starts or ends with a substring
starts_with = str3.startswith("Hello")
print("Starts with 'Hello':", starts_with)

ends_with = str3.endswith("World")
print("Ends with 'World':", ends_with)

# Advanced formatting with f-Strings
value = 3.14159
formatted_value = f"Value: {value:.2f}"
print("Formatted value:", formatted_value)

# Multiline strings
multiline_str = """This is a
multiline string
in Python."""
print("Multiline string:", multiline_str)

# Raw strings (useful for regex)
raw_str = r"C:\Users\Rizwan\Desktop"
print("Raw string:", raw_str)
>>>>>>> origin/main
