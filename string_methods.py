# str.upper() and str.lower()

# text = "Hello, World!"
# uppercase_text = text.upper()
# lowercase_text = text.lower()

# print(uppercase_text)  # Output: "HELLO, WORLD!"
# print(lowercase_text)  # Output: "hello, world!"

# -----------------------------------------------------------------------------------

# str.strip()

# Removes leading and trailing whitespace (spaces, tabs, and newline characters) from a string.

# text = "   Hello, World!   "
# stripped_text = text.strip()

# print(stripped_text)  # Output: "Hello, World!"

# --------------------------------------------------------------------

# str.replace()

# Replaces a specified substring with another substring.

# text = "Hello, World!"
# new_text = text.replace("World", "Python")

# print(new_text)  # Output: "Hello, Python!"

# ------------------------------------------------------------------------

# str.split()

# Splits a string into a list of substrings based on a delimiter (default is whitespace).

# text = "apple,banana,cherry"
# fruits = text.split(",")

# print(fruits)  # Output: ['apple', 'banana', 'cherry']

# -----------------------------------------------------------------

# str.join()

# Joins a list of strings into one string using the specified string as a delimiter.

# fruits = ['apple', 'banana', 'cherry']
# text = ",".join(fruits)

# print(text)  # Output: "apple,banana,cherry"

# -----------------------------------------------------------

# str.find() and str.index()

# str.find(substring) returns the lowest index of the first occurrence of a substring in the string, or -1 if not found.
# str.index(substring) is similar to str.find(), but it raises a ValueError if the substring is not found.

# text = "Hello, World!"
# index1 = text.find("World")  # Returns 7
# index2 = text.index("Python")  # Raises ValueError

# ------------------------------------------------

# str.startswith() and str.endswith()

# str.startswith(prefix) checks if a string starts with a specified prefix.
# str.endswith(suffix) checks if a string ends with a specified suffix.


# text = "Hello, World!"
# starts_with_hello = text.startswith("Hello")  # True
# ends_with_world = text.endswith("World")  # False
