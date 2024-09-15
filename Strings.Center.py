print()
n = input("Enter Number: ")
print()

# Printing the original input
print(f"Original input: '{n}'")

# Centering the string with a specified width (example: 20)
centered_n = n.center(20)
print(f"Centered (width 20): '{centered_n}'")

# Stripping leading whitespace
lstrip_n = n.lstrip()
print(f"Leading whitespace removed: '{lstrip_n}'")

# Stripping trailing whitespace
rstrip_n = n.rstrip()
print(f"Trailing whitespace removed: '{rstrip_n}'")

print()
