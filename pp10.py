user_string = input("Enter a string: ")
print("\nCharacter -> ASCII Value")
print("-" * 24)
for char in user_string:
    ascii_value = ord(char)
    print(f"    '{char}'   ->    {ascii_value}")
